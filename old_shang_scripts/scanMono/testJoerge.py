import time
import epics

# Joerger scaler PV names
SCALER_SET_TIME = '18ID:scaler2.TP'
SCALER_START = '18ID:scaler2.CNT'
SCALER_I0 = '18ID:scaler2.S3'
SCALER_I1 = '18ID:scaler2.S4'
SCALER_I2 = '18ID:scaler2.S5'
SCALER_I3 = '18ID:scaler2.S6'
SCALER_PresetI0 = '18ID:scaler2.PR3'
SCALER_PresetI1 = '18ID:scaler2.PR4'
SCALER_PresetI2 = '18ID:scaler2.PR5'
SCALER_PresetI3 = '18ID:scaler2.PR6'


EXPOSURE_TIME = 0.5

status = epics.caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
status = epics.caput(SCALER_START, 1, wait=True, timeout=60)

time.sleep(EXPOSURE_TIME+0.2) 

I0 = epics.caget(SCALER_I0)
I1 = epics.caget(SCALER_I1)

print I0
