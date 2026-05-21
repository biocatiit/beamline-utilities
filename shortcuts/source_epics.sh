# EPICS BASE
export EPICS_BASE=/opt/epics/base
export EPICS_HOST_ARCH=$(${EPICS_BASE}/startup/EpicsHostArch)
export PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}
if [ "x${LD_LIBRARY_PATH}" = x ]; then
    export LD_LIBRARY_PATH=${EPICS_BASE}/lib/${EPICS_HOST_ARCH}
else
    export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${EPICS_BASE}/lib/${EPICS_HOST_ARCH}
fi

# caQtDM
export QT_PLUGIN_PATH=/opt/epics/extensions/lib/${EPICS_HOST_ARCH}
export CAQTDM_DISPLAY_PATH=/opt/epics/extensions/caqtdm-4.5.0/caQtDM_Tests
export PATH=/opt/epics/extensions/bin/${EPICS_HOST_ARCH}:${PATH}

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/epics/synApps_6_3/support/areaDetector-master/ADSupport/lib/${EPICS_HOST_ARCH}

