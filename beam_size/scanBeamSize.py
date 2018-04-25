#!/usr/bin/python

import time
import epics
import numpy as np
import scipy.interpolate
import datetime
import h5py
import matplotlib
matplotlib.use('qt4agg')
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Scanning the beamsize.')
parser.add_argument('motor', help='The motor EPICS PV.')
parser.add_argument('ctr', help='The counter name (such as I0) to be used.')
parser.add_argument('start', type=float, help='The initial motor position (absolute, not relative).')
parser.add_argument('end', type=float, help='The final motor position (absolute, not relative).')
parser.add_argument('step', type=float, help='The step size to use in the scan.')
parser.add_argument('exp', type=float, default=0.2, nargs='?', help='The counting time at each scan point, optional (default: 0.2 s).')

args = parser.parse_args()

motorPV = args.motor
ctr = args.ctr
start = args.start
end = args.end
step = args.step
exp = args.exp

if start < end:
    motor_position = np.arange(start, end+step, step)
else:
    motor_position = np.arange(end, start+step, step)
    motor_position = motor_position[::-1]


PRESET_COUNT = exp * int(float('1E8'))

def MoveToX(posX):
  status = epics.caput(motorPV + '.VAL', posX, wait=True, timeout=60)

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
SCALER_PresetI0 = '18ID:scaler2.PR3'
SCALER_PresetI1 = '18ID:scaler2.PR4'
SCALER_PresetI2 = '18ID:scaler2.PR5'
SCALER_PresetI3 = '18ID:scaler2.PR6'

def initJoerger():
    status = epics.caput(SCALER_SET_TIME, exp, wait=True)
    status = epics.caput(SCALER_PresetI0, PRESET_COUNT, wait=True, timeout = 60)
    status = epics.caput(SCALER_PresetI1, PRESET_COUNT, wait=True, timeout = 60)
    status = epics.caput(SCALER_PresetI2, PRESET_COUNT, wait=True, timeout = 60)
    status = epics.caput(SCALER_PresetI3, PRESET_COUNT, wait=True, timeout = 60)


def getDark():
    status = epics.caput(SHUTTER, shutter_close, wait=1)
    #time.sleep(0.05) # Wait 50 ms for slow shutter to close

    # start scaler
    status = epics.caput(SCALER_START, 1, wait=True, timeout=60)
    # time.sleep(exp+0.1)   # Wait for scaler to complete
    # read scaler values
    I0 = epics.caget(SCALER_I0)
    I1 = epics.caget(SCALER_I1)
    I2 = epics.caget(SCALER_I2)
    I3 = epics.caget(SCALER_I3)
    return {'I0':I0, 'I1':I1, 'I2':I2, 'I3':I3}

def getIonChamber():
    # start scaler
    # status = epics.caput(SCALER_SET_TIME, exp, wait=1)
    status = epics.caput(SCALER_START, 1, wait=True, timeout=60)
    #time.sleep(exp+0.1)   # Wait for scaler to complete
    # read scaler values
    I0 = epics.caget(SCALER_I0)
    I1 = epics.caget(SCALER_I1)
    I2 = epics.caget(SCALER_I2)
    I3 = epics.caget(SCALER_I3)
    return {'I0':I0, 'I1':I1, 'I2':I2, 'I3':I3}


# step scan with defined grid points in space
incident_I = np.empty_like(motor_position)
knifeedge_I = np.empty_like(motor_position)
normalized_I = np.empty_like(motor_position)
diff_I = np.empty_like(motor_position)


raw_input('Please check SHUTTER OPEN switch on XiA, is it off? Type y to continue...')

initJoerger()
print 'Init Joerger preset counts for I0, I1, I2, I3'
print 'Taking dark background ...'
I_dark = getDark()
#print I_dark

print 'Move motor to the start position %.03f mm...' %start
MoveToX(start)

# Open shutter
status = epics.caput(SHUTTER, shutter_open, wait=1)
time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
print 'Open shutter'
time.sleep(3) #Wait for I0 to reach full counts

#Set up live plots
fig, axes = plt.subplots(2, 1)
ax0 = axes[0]
ax1 = axes[1]
ax0.set_xlim(min(motor_position), max(motor_position))
ax1.set_xlim(min(motor_position), max(motor_position))
ax0.set_title('Knife-edge step scan I1/I0')
ax0.set_ylabel('Intensity (arb.)')
ax1.set_title('Derivative')
ax1.set_xlabel('Position (mm)')
ax1.set_ylabel('$\Delta$I (arb.)')
plt.subplots_adjust(hspace=0.3, top=0.95,right =0.98)
plt.ion()
plt.show()
plt.draw()
ax0_bkg = fig.canvas.copy_from_bbox(ax0.bbox)
ax1_bkg = fig.canvas.copy_from_bbox(ax1.bbox)

print ('%9s %9s %9s %9s' %('Position', 'I0', ctr,
        ctr+'/I0'))

for i, posX in enumerate(motor_position):
    try:
        MoveToX(posX)
        I_values = getIonChamber()

        incident_I[i] = I_values['I0'] - I_dark['I0']
        knifeedge_I[i] = I_values[ctr] - I_dark[ctr]
        normalized_I[i] = knifeedge_I[i]/incident_I[i]

        if i>0:
            diff_I[:i+1] = np.gradient(incidient_I[:i+1], motor_position[:i+1])
            diff_I[np.isnan(diff_I[:i+1])] = 0

        print ('%9.03f %9.03f %9.03f %9.03f' %(posX, incident_I[i], knifeedge_I[i],
            normalized_I[i]))

        #Live plot
        if i==0:
            intensity = ax0.plot(motor_position[0], knifeedge_I[0], 'o', animated=True)[0]
            ax0_lim = ax0.get_ylim()

        elif i==1:
            diff = ax1.plot(motor_position[:i+1], diff_I[:i+1], 'o-', animated=True)[0]
            ax1_lim = ax1.get_ylim()

            redraw = False
            intensity.set_data(motor_position[:i+1], knifeedge_I[:i+1])

            if knifeedge_I[i]<ax0_lim[0] or  knifeedge_I[i]>ax0_lim[1]:
                ax0.relim()
                ax0.autoscale_view(scalex=False)
                ax0_lim = ax0.get_ylim()
                redraw = True

            fig.canvas.restore_region(ax0_bkg)

            ax0.draw_artist(intensity)
            fig.canvas.blit(ax0.bbox)

        else:
            redraw = False

            intensity.set_data(motor_position[:i+1], knifeedge_I[:i+1])
            diff.set_data(motor_position[:i+1], diff_I[:i+1])

            if knifeedge_I[i]<ax0_lim[0] or  knifeedge_I[i]>ax0_lim[1]:
                ax0.relim()
                ax0.autoscale_view(scalex=False)
                ax0_lim = ax0.get_ylim()
                redraw = True
            if diff_I[i]<ax1_lim[0] or diff_I[i]>ax1_lim[1]:
                ax1.relim()
                ax1.autoscale_view(scalex=False)
                ax1_lim = ax1.get_ylim()
                redraw = True
            if redraw:
                fig.canvas.draw()

            fig.canvas.restore_region(ax0_bkg)
            fig.canvas.restore_region(ax1_bkg)

            ax0.draw_artist(intensity)
            fig.canvas.blit(ax0.bbox)

            ax1.draw_artist(diff)
            fig.canvas.blit(ax1.bbox)

        plt.pause(0.00001)
    except KeyboardInterrupt:
        incident_I[i:] = 0
        knifeedge_I[i:] = 0
        normalized_I[i:]=0
        diff_I[i:] = 0
        break

#Turn live plot into a persistant plot
plt.ioff()
ax0.clear()
ax1.clear()
ax0.plot(motor_position, knifeedge_I, 'o')
ax0.set_title('Knife-edge step scan I1/I0')
ax0.set_ylabel('Intensity (arb.)')
ax1.set_xlabel('Position (mm)')
ax1.set_ylabel('$\Delta$I (arb.)')


# Close shutter
status = epics.caput(SHUTTER, shutter_close, wait=1)
print 'Closed shutter'

if normalized_I[:5].mean() > normalized_I[-5:].mean():
    diff_I = diff_I*-1

y = diff_I - np.max(diff_I)/2


if motor_position[0]>motor_position[1]:
    spline = scipy.interpolate.UnivariateSpline(motor_position[::-1], y[::-1], s=0)
else:
    spline = scipy.interpolate.UnivariateSpline(motor_position, y, s=0)

try:
    roots = spline.roots()
    if roots.size == 2:
        r1 = roots[0]
        r2 = roots[1]
    elif roots.size>2:
        rmax = np.argmax(abs(np.diff(roots)))
        r1 = roots[rmax]
        r2 = roots[rmax+1]
    else:
        r1 = 0
        r2 = 0
except Exception:
  r1 = 0
  r2 = 0

fwhm = np.fabs(r2-r1)


ax1.plot(motor_position, diff_I)
if fwhm>0:
    if r1<r2:
        ax1.axvspan(r1, r2, facecolor='g', alpha=0.5)
    else:
        ax1.axvspan(r2, r1, facecolor='g', alpha=0.5)
    ax1.hlines(np.max(diff_I)/2, np.min(motor_position), np.max(motor_position))
    ax1.set_title('FWHM = %.02f $\mu$m' %(fwhm*1000))
else:
    ax1.set_title('FWHM not found')

plt.draw()
plt.show()

logName = 'knife-edge-scan.log'

print 'FWHM = %.02f um' %(fwhm*1000)

scanName = datetime.datetime.now().strftime("%Y%m%d-%H%M") + '.h5'
remark = raw_input('Add remark to the current scan (max. 80 characters):\n')

with open(logName, 'a') as flog:
    flog.write('%s, %s, [%.03f, %.03f] %.03f, %.05f mm, %s\n' %(scanName, motorPV, start, end, step, fwhm, remark))


raw_scan = np.array(zip(motor_position, incident_I, knifeedge_I))
derivative = np.array(zip(motor_position, y))
h5remark = np.array(remark)
h5fwhm = np.array(fwhm)

with h5py.File(scanName, 'w') as fscan:
    dset_raw = fscan.create_dataset("raw-scan", data=raw_scan)
    dset_raw.attrs['column names'] = ['motor position (mm)', 'incident I', 'knife edge I']
    dset_derivative = fscan.create_dataset("derivative", data=derivative)
    dset_derivative.attrs['column names'] = ['motor position (mm)', 'derivative of normalized I']
    dset_remark = fscan.create_dataset("remark", data=h5remark)
    dset_fwhm = fscan.create_dataset("FWHM", data=h5fwhm)
print 'File %s saved!' %scanName

###########How to read out the h5 data with python
#f = h5py.File(scanName, 'r')
#raw = np.array(f['raw-scan'])
#print raw
#remark = np.array(f['remark'])
#print remark
################################################
