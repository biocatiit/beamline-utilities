import os
import sys
import datetime
import time
from PySide.QtCore import *
from PySide.QtGui import *

from epics import *

SAMPLES_LOG = 'samples.log' # to be saved in the user data folder

PV_RING_CURRENT = 'S:SRcurrentAI'

MARCCD_READOUT_TIME = 4 # seconds
IMAGE_MODE_MULTIPLE = 1
FRAME_TYPE_NORMAL = 0 # Frame Type 0 = Normal
FRAME_TYPE_BACKGROUND = 1 # Frame Type 1 = Background

# MarCCD PV
PV_MARCCD = 'Mar165:cam1:'
acquire_pv = PV(PV_MARCCD + 'Acquire')
pv_ExposureTime = PV(PV_MARCCD + 'AcquireTime')
pv_AcquirePeriod = PV(PV_MARCCD + 'AcquirePeriod')
pv_NumImages = PV(PV_MARCCD + 'NumImages')
pv_ImageMode = PV(PV_MARCCD + 'ImageMode')
pv_FileName = PV(PV_MARCCD + 'FileName')
pv_FileNumber = PV(PV_MARCCD + 'FileNumber')
pv_AutoIncrement = PV(PV_MARCCD + 'AutoIncrement')
pv_DetectorStatus = PV(PV_MARCCD + 'DetectorState_RBV')
pv_FrameType = PV(PV_MARCCD + 'FrameType')
detectorStatusDict = {0:'Idle', 1:'Acquire', 2:'Readout', 3:'Correct', 4:'Saving', 5:'Aborting', 6:'Error', 7:'Waiting', 8:'Initializing'}

#===================================================================
# Module with functions to save & restore qt widget values
# Written by: Alan Lilly 
# Website: http://panofish.net
#===================================================================

#~ import sys
#~ from PyQt4.QtCore import *
#~ from PyQt4.QtGui import *
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

import uiMarCCD

class MainDialog(QDialog, uiMarCCD.Ui_dlgSampleCCD):

	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		
		self.connect(self.pbStartMarCCD, SIGNAL("clicked()"), self.startMarCCD)
		self.connect(self.pbTakeDark, SIGNAL("clicked()"), self.takeDark)
		
		settings = QSettings("biocat",  "marccd")
		GUIrestore(self, settings)

		timer = QTimer(self)
		self.connect(timer, SIGNAL("timeout()"), self.updateUI)
		timer.start(1000)
		
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
		stat = pv_DetectorStatus.get()
		if stat == 2:
			self.lblDetectorStatus.setStyleSheet("color:blue")
		elif stat == 1:
			self.lblDetectorStatus.setStyleSheet("color:red")
		elif stat == 0:
			self.lblDetectorStatus.setStyleSheet("color:green")
		else:
			self.lblDetectorStatus.setStyleSheet("color:black")

		self.lblDetectorStatus.setText(detectorStatusDict[stat])
	
	def startMarCCD(self):
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
		
		# set MarCCD parameters
		pv_FrameType.put(FRAME_TYPE_NORMAL) 
		pv_ExposureTime.put(self.dsbExposureTime.value())
		pv_AcquirePeriod.put(self.dsbExposureTime.value() + MARCCD_READOUT_TIME)
		pv_NumImages.put(self.sbNumberOfFrames.value())
		pv_FileName.put(fileName)
		pv_FileNumber.put(1) # frame always start from 1
		pv_AutoIncrement.put(1) # Enable autoincrement for multiple frames
		caput('Mar165:cam1:ShutterMode', 0) # Disable shutter for debug

		# start MarCCD detector
		acquire_pv.put(1)
		
	def takeDark(self):
		print 'Take dark background'
		# put an entry to the Log file
		startTime = datetime.datetime.now().strftime("%Y%m%d-%H:%M")
		logFile = os.path.join(self.leDataFolder.text(), SAMPLES_LOG)
		writeLineToLog(logFile, '%s: %s' %(startTime, 'Background'))
		writeLineToLog(logFile, 'Take dark background (no file saved).')
		writeLineToLog(logFile, 'Exposure time: %.03f second;  Number of frames: %d\n'%(self.dsbExposureTime.value(), self.sbNumberOfFrames.value()))

		# set MarCCD to take background
		pv_FrameType.put(FRAME_TYPE_BACKGROUND) 
		caput('Mar165:cam1:ShutterMode', 0) # Disable shutter for debug

		# start MarCCD detector
		acquire_pv.put(1)

	def closeEvent(self, event):
		settings = QSettings("biocat",  "marccd")
		GUIsave(self, settings)
		sys.exit()
		
def main():
	app = QApplication(sys.argv)
	form = MainDialog()
	form.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
