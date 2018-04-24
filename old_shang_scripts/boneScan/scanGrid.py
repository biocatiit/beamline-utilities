import os
import sys
import datetime
import time
from PySide.QtCore import *
from PySide.QtGui import *

from epics import *
#PilatusImageFolder = '/nas_data/Pilatus1M/20160810Jasiuk/'
#CCDImageFolder = '/nas_data/MarCCD/...'
#XrayIntensityFolder = '/data/XrayIntensity/20160810Jasiuk/'
XrayIntensityFolder = '/home/biocat/Shang/20160810Jasiuk/'

# Pilatus 1M parameters
N_FRAMES =1
EXPOSURE_TIME = 3 #s
FRAME_PERIOD = 3.01 #s

# Newport PV names
npX_Position = '18ID:n:m15.VAL'
npY_Position = '18ID:n:m16.VAL'

# Shutter PV name
SHUTTER = '18ID:bo0:ch6'
shutter_open = 0
shutter_close = 1

# APS ring current
RING_CURRENT = 'S:SRcurrentAI'

# Joerger scaler PV names
SCALER_SET_TIME = '18ID:scaler2.TP'
SCALER_START = '18ID:scaler2.CNT'
SCALER_I0 = '18ID:scaler2.S3'
SCALER_I1 = '18ID:scaler2.S4'
SCALER_I2 = '18ID:scaler2.S5'
SCALER_I3 = '18ID:scaler2.S6'


# Pilatus 1M PV names
PV_PILATUS = '18IDpil1M:cam1:'
filename_pv = PV(PV_PILATUS+'FileName')
frameno_pv  = PV(PV_PILATUS+'FileNumber')
acquire_pv  = PV(PV_PILATUS+'Acquire')
acqmode_pv  = PV(PV_PILATUS+'AcquireMode')
expp_pv     = PV(PV_PILATUS+'AcquirePeriod')
expt_pv     = PV(PV_PILATUS+'AcquireTime')
nimg_pv     = PV(PV_PILATUS+'NumImages')

LogFile = 'ScanGridLogFile.txt'
run = 0
scanName = ''
X_start = 0.0
X_end = 0.1
X_step = 0.01
Y_start = 0.0
Y_end = 0.1
Y_step = 0.01

def MoveToXY(posX, posY):
  status = caput(npX_Position, posX, wait=1)
  status = caput(npY_Position, posY, wait=1)

def GetDataAtPosition(posX, posY, image_prefix, fIonChamber):
	#time.sleep(1)
  filename_pv.put(image_prefix)
  frameno_pv.put(1)
  acqmode_pv.put(0)
  expp_pv.put(FRAME_PERIOD) # acquire period
  expt_pv.put(EXPOSURE_TIME) # exposure time
  nimg_pv.put(N_FRAMES)    # number of frames

  totalTime = N_FRAMES*FRAME_PERIOD

  status = caput(SHUTTER, shutter_open, wait=1)
  time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
  # start scaler 
  status = caput(SCALER_SET_TIME, totalTime, wait=1)
  status = caput(SCALER_START, 1)
  acquire_pv.put(1) # Start Pilatus 1M
  time.sleep(totalTime+0.2)   # Wait for detector&scaler to complete
  status = caput(SHUTTER, shutter_close, wait=1)

  # set default I values
  I0 = 1
  I1 = 1
  I2 = 1
  I3 = 1
  # read scaler values
  try:
    I0 = caget(SCALER_I0)
    I1 = caget(SCALER_I1)
    I2 = caget(SCALER_I2)
    I3 = caget(SCALER_I3)
  except Exception:
    sys.exc_clear()
  print I0, I1, I2, I3
  # save intensity values to EMBL radaver header file format
  #fout = open(os.path.join(XrayIntensityFolder, image_prefix + '.txt'), "w")
  #fout.writelines('Exposure time [s]: %s\n' %totalTime)
  #fout.writelines('Incident Beam: %d\n' %I0)
  #fout.writelines('Transmitted Beam: %d\n' %I1)
  #fout.writelines('Code: %s\n' %image_prefix)
  #fout.writelines('Concentration [mg/ml]: 1\n')
  #fout.writelines('Run Number: %s\n' %image_prefix[:4])
  #fout.close
  f = open(os.path.join(XrayIntensityFolder, fIonChamber+'.txt'), "a")
  f.write('%f %f %d %d %d %d\n' %(posX, posY, I0, I1, I2, I3))
  f.close()

class AbortNow(Exception): pass

def readRunNumber():
	runNumberFile = 'last-run-number'
	try:
		with open(runNumberFile, 'r') as fRunNumber:
			CurrentRunNumber = int(fRunNumber.read())
	except IOError:
		CurrentRunNumber = 1
	return CurrentRunNumber

def getRunNumber():
	runNumberFile = 'last-run-number'
	try:
		with open(runNumberFile, 'r') as fRunNumber:
			CurrentRunNumber = int(fRunNumber.read())
	except IOError:
		CurrentRunNumber = 1

	with open(runNumberFile, 'w') as f:
		f.write('%d' %(CurrentRunNumber +1))

	return CurrentRunNumber

def writeLineToLog(line):
	with open(LogFile, 'a') as fLog:
		fLog.write(line + '\n')
		print line
class Worker(QThread):
	def __init__(self):
		QThread.__init__(self)
	def update(self, s):
		print  s
		self.emit(SIGNAL("statusUpdate(QString)"), s)
	def run(self):
		self.abortnow = False
		global X_start
		global X_end
		global X_step
		global Y_start
		global Y_end
		global Y_step
		global scanName
		# start motor scan
		try:
			posX = X_start
			while (posX <= X_end):
				posY = Y_start
				while (posY <= Y_end):
					# Check if user clicked the Abort button
					if self.abortnow:
						raise AbortNow # break from nested loops
					# Update GUI status and stdout
					s = 'Position (%.03f,%.03f) mm requested.' %(posX, posY)
					self.update(s)
					# Move Newport stage to requested positions
					MoveToXY(posX, posY)
					# Confirm motor positions reached
					x = caget(npX_Position)
					y = caget(npY_Position)
					s = 'Position (%.03f, %.03f) mm reached.' %(x, y)
					self.update(s)
					s = 'Motor: X = %.03f mm, Y = %.03f mm' %(x,y)
					self.emit(SIGNAL("motorUpdate(QString)"), s)
					# Update GUI status and stdout
					tifName = '%s_x%.03fy%.03f' %(scanName, posX, posY)
					s = 'Start Pilatus 1M for image %s.tif' %tifName
					self.update(s)
					# Start Pilatus detector
					GetDataAtPosition(x,y,tifName, scanName)
					# Update GUI status and stdout
					s = 'Pilatus 1M complete!\n'
					self.update(s)
					posY += Y_step
				posX += X_step
			s = 'Scan complete!'
			self.update(s)
      #visualize tif file with adxv
      #os.system('/home/biocat/bin/adxv %s'%os.path.join(PilatusImageFolder, tifName)
			# add complete to the log file
			writeLineToLog('Scan complete!\n')

		except AbortNow:
			s = 'Scan aborted!'
			self.update(s)
			writeLineToLog('Scan aborted!\n')

import uiScanGrid
class MainDialog(QDialog, uiScanGrid.Ui_dlgScanGrid):
	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		
		self.worker = Worker()
		
		#self.connect(timer, SIGNAL("timeout()"), self.updatePositions)
		self.connect(self.worker, SIGNAL("statusUpdate(QString)"), self.updateStatus, Qt.DirectConnection)
		self.connect(self.worker, SIGNAL("motorUpdate(QString)"), self.updateMotor, Qt.DirectConnection)
		
		self.connect(self.pbStartScan, SIGNAL("clicked()"), self.startScan)
		self.connect(self.pbAbortScan, SIGNAL("clicked()"), self.abortScan)
		
	def startScan(self):
		global scanName
		# get Run number
		run = getRunNumber()
		scanName = '%04d_%s' %(run, self.leScanName.text())
		self.lblScanName.setText(scanName)
		print 'start scan %s' %scanName
				
		# put an entry to the Log file
		startTime = datetime.datetime.now().strftime("%Y%m%d-%H:%M")
		writeLineToLog('%s: %s' %(startTime, scanName))
		writeLineToLog('X: [%.03f, %.03f] %03f mm' %(self.dsbXstart.value(), self.dsbXend.value(), self.dsbXstep.value()))
		writeLineToLog('Y: [%.03f, %.03f] %03f mm' %(self.dsbYstart.value(), self.dsbYend.value(), self.dsbYstep.value()))
		writeLineToLog('%s' %self.leScanRemark.text())

		global X_start
		global X_end
		global X_step
		global Y_start
		global Y_end
		global Y_step
		
		X_start = self.dsbXstart.value()
		X_end = self.dsbXend.value()
		X_step = self.dsbXstep.value()
		Y_start = self.dsbYstart.value()
		Y_end = self.dsbYend.value()
		Y_step = self.dsbYstep.value()
		
		print X_start, X_end, X_step, Y_start, Y_end, Y_step
		self.worker.start()
		
	def abortScan(self):
		self.worker.abortnow = True
	
	def updateStatus(self, status):
		self.lblStatusText.setText(status)

	def updateMotor(self, position):
		self.lblMotorPosition.setText(position)

#def updateScanName(self, scanName):
#		self.lblScanName.setText(scanName)

def main():
	app = QApplication(sys.argv)
	form = MainDialog()
	form.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
