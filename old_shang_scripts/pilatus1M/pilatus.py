import os
import sys
import datetime
import time
from PySide.QtCore import *
from PySide.QtGui import *

from epics import *

SAMPLES_LOG = 'samples.log' # to be saved in the user data folder

PV_RING_CURRENT = 'S:SRcurrentAI'
PILATUS_STATUS_IDLE = 0
PILATUS_STATUS_COLLECTING = 1

# Pilatus 1M PV
PV_PILATUS1M = '18IDpil1M:cam1:'
acquire_pv = PV(PV_PILATUS1M + 'Acquire')
pv_ExposureTime = PV(PV_PILATUS1M + 'AcquireTime')
pv_AcquirePeriod = PV(PV_PILATUS1M + 'AcquirePeriod')
pv_NumImages = PV(PV_PILATUS1M + 'NumImages')
pv_FileName= PV(PV_PILATUS1M + 'FileName')
pv_FullFileName= PV(PV_PILATUS1M + 'FullFileName_RBV')
pv_FileNumber= PV(PV_PILATUS1M + 'FileNumber')

import inspect

#===================================================================
# save "ui" controls and values to registry "setting"
# currently only handles comboboxes editlines & checkboxes
# ui = qmainwindow object
# settings = qsettings object
#===================================================================

def GUIsave(ui, settings):

    #for child in ui.children():  # works like getmembers, but because it traverses the hierarachy, you would have to call guisave recursively to traverse down the tree

    for name, obj in inspect.getmembers(ui):
        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)    # save ui values, so they can be restored next time

        if isinstance(obj, QSpinBox):
            name = obj.objectName()
            v = obj.value()
            settings.setValue(name, v)

        if isinstance(obj, QDoubleSpinBox):
            name = obj.objectName()
            v = obj.value()
            settings.setValue(name, v)

#===================================================================
# restore "ui" controls with values stored in registry "settings"
# currently only handles comboboxes, editlines &checkboxes
# ui = QMainWindow object
# settings = QSettings object
#===================================================================

def GUIrestore(ui, settings):

    for name, obj in inspect.getmembers(ui):
        if isinstance(obj, QLineEdit):
            name = obj.objectName()
            value = unicode(settings.value(name))  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QSpinBox):
            name = obj.objectName()
            value = settings.value(name)   # get stored value from registry
            if value != None:
                obj.setValue(int(value))   # restore checkbox

        if isinstance(obj, QDoubleSpinBox):
            name = obj.objectName()
            value = settings.value(name)   # get stored value from registry
            if value != None:
                obj.setValue(float(value))   # restore checkbox

################################################################

def getRunNumber(folder):
	runNumberFile = os.path.join(folder, 'lastest-run-number')
	try:
		with open(runNumberFile, 'r') as fRunNumber:
			CurrentRunNumber = int(fRunNumber.read())
	except IOError:
		CurrentRunNumber = 1
		
	with open(runNumberFile, 'w') as f:
		f.write('%d' %(CurrentRunNumber +1))
		
	return CurrentRunNumber

def writeLineToLog(logfile, line):
	with open(logfile, 'a') as fLog:
		fLog.write(line + '\n')
		print line

import uiPilatus1M

class MainDialog(QDialog, uiPilatus1M.Ui_dlgPilatus):

	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		
		self.connect(self.pbStartPilatus, SIGNAL("clicked()"), self.startPilatus)
		self.connect(self.pbStopPilatus, SIGNAL("clicked()"), self.stopPilatus)
		
		settings = QSettings("biocat",  "pilatus1M")
		GUIrestore(self, settings)

		timer = QTimer(self)
		self.connect(timer, SIGNAL("timeout()"), self.updateUI)
		timer.start(500)

	def closeEvent(self, event):
		settings = QSettings("biocat",  "pilatus1M")
		GUIsave(self, settings)
		sys.exit()
		
	def updateUI(self):
		current = caget(PV_RING_CURRENT)
		self.lblStorageRingCurrent.setText('%.01f' %current)
		if current < 50.0:
			self.lblStorageRingCurrent.setStyleSheet("color:red")
		else:
			self.lblStorageRingCurrent.setStyleSheet("color:green")
		
		#update Time
		self.dteNow.setDateTime(QDateTime.currentDateTime())

		#update detector Status
		status = acquire_pv.get()
		if status == PILATUS_STATUS_IDLE:
			self.lblDetectorStatus.setStyleSheet("color:green")
			self.lblDetectorStatus.setText('Idle')
			#self.lblDetectorStatus.setText(pv_FullFileName.get(as_string=True))
		else:
			self.lblDetectorStatus.setStyleSheet("color:red")
			self.lblDetectorStatus.setText('Collecting...')


	def stopPilatus(self):
		# stop detector
		acquire_pv.put(0)

	def startPilatus(self):
		# get Run number
		run = getRunNumber(self.leDataFolder.text())
		self.lblRunNumber.setText('%04d'%run)
		fileName = '%04d_%s' %(run, self.leSampleCode.text())
		print 'start measurement %s' %fileName
		
		# put an entry to the Log file
		startTime = datetime.datetime.now().strftime("%Y%m%d-%H:%M")
		logFile = os.path.join(self.leDataFolder.text(), SAMPLES_LOG)
		writeLineToLog(logFile, '%s: %s' %(startTime, fileName))
		writeLineToLog(logFile, '%s' %self.leSampleDescription.text())
		writeLineToLog(logFile, 'Exposure time: %.03f second;  Number of frames: %d\n'%(self.dsbExposureTime.value(), self.sbNumberOfFrames.value()))
		
		# set parameters
		pv_ExposureTime.put(self.dsbExposureTime.value())
		pv_AcquirePeriod.put(self.dsbExposureTime.value() + self.dsbWaitTime.value())
		pv_NumImages.put(self.sbNumberOfFrames.value())
		pv_FileName.put(fileName)
		pv_FileNumber.put(1) # frame always start from 1

		# start detector
		acquire_pv.put(1)

def main():
	app = QApplication(sys.argv)
	form = MainDialog()
	form.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()

