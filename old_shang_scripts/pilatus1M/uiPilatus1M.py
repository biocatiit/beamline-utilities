# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiPilatus1M.ui'
#
# Created: Tue Apr 12 15:10:54 2016
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dlgPilatus(object):
    def setupUi(self, dlgPilatus):
        dlgPilatus.setObjectName("dlgPilatus")
        dlgPilatus.resize(594, 541)
        font = QtGui.QFont()
        font.setPointSize(12)
        dlgPilatus.setFont(font)
        self.groupBox_2 = QtGui.QGroupBox(dlgPilatus)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 571, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(22, 26, 261, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 381, 16))
        self.label_8.setObjectName("label_8")
        self.leSampleDescription = QtGui.QLineEdit(self.groupBox_2)
        self.leSampleDescription.setGeometry(QtCore.QRect(20, 70, 541, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.leSampleDescription.setFont(font)
        self.leSampleDescription.setObjectName("leSampleDescription")
        self.leSampleCode = QtGui.QLineEdit(self.groupBox_2)
        self.leSampleCode.setGeometry(QtCore.QRect(430, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.leSampleCode.setFont(font)
        self.leSampleCode.setObjectName("leSampleCode")
        self.groupBox_3 = QtGui.QGroupBox(dlgPilatus)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 571, 241))
        self.groupBox_3.setAutoFillBackground(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(50, 40, 201, 16))
        self.label_11.setObjectName("label_11")
        self.dsbExposureTime = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.dsbExposureTime.setGeometry(QtCore.QRect(290, 38, 111, 31))
        self.dsbExposureTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbExposureTime.setDecimals(3)
        self.dsbExposureTime.setMinimum(0.01)
        self.dsbExposureTime.setMaximum(99999.99)
        self.dsbExposureTime.setProperty("value", 1.0)
        self.dsbExposureTime.setObjectName("dsbExposureTime")
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(50, 130, 201, 16))
        self.label_12.setObjectName("label_12")
        self.sbNumberOfFrames = QtGui.QSpinBox(self.groupBox_3)
        self.sbNumberOfFrames.setGeometry(QtCore.QRect(290, 120, 111, 31))
        self.sbNumberOfFrames.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sbNumberOfFrames.setMinimum(1)
        self.sbNumberOfFrames.setMaximum(99999)
        self.sbNumberOfFrames.setObjectName("sbNumberOfFrames")
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(53, 170, 141, 16))
        self.label_14.setObjectName("label_14")
        self.lblDetectorStatus = QtGui.QLabel(self.groupBox_3)
        self.lblDetectorStatus.setGeometry(QtCore.QRect(290, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.lblDetectorStatus.setFont(font)
        self.lblDetectorStatus.setStyleSheet("color:green")
        self.lblDetectorStatus.setObjectName("lblDetectorStatus")
        self.pbStartPilatus = QtGui.QPushButton(self.groupBox_3)
        self.pbStartPilatus.setGeometry(QtCore.QRect(130, 190, 141, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pbStartPilatus.setFont(font)
        self.pbStartPilatus.setStyleSheet("")
        self.pbStartPilatus.setAutoDefault(False)
        self.pbStartPilatus.setObjectName("pbStartPilatus")
        self.dsbWaitTime = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.dsbWaitTime.setGeometry(QtCore.QRect(290, 78, 111, 31))
        self.dsbWaitTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dsbWaitTime.setDecimals(3)
        self.dsbWaitTime.setMinimum(0.01)
        self.dsbWaitTime.setMaximum(99999.99)
        self.dsbWaitTime.setProperty("value", 1.0)
        self.dsbWaitTime.setObjectName("dsbWaitTime")
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(50, 80, 181, 16))
        self.label_13.setObjectName("label_13")
        self.pbStopPilatus = QtGui.QPushButton(self.groupBox_3)
        self.pbStopPilatus.setGeometry(QtCore.QRect(310, 190, 141, 41))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pbStopPilatus.setFont(font)
        self.pbStopPilatus.setStyleSheet("")
        self.pbStopPilatus.setAutoDefault(False)
        self.pbStopPilatus.setObjectName("pbStopPilatus")
        self.lblRunNumber = QtGui.QLabel(dlgPilatus)
        self.lblRunNumber.setGeometry(QtCore.QRect(480, 480, 101, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lblRunNumber.setFont(font)
        self.lblRunNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblRunNumber.setObjectName("lblRunNumber")
        self.label_15 = QtGui.QLabel(dlgPilatus)
        self.label_15.setGeometry(QtCore.QRect(330, 510, 221, 31))
        self.label_15.setObjectName("label_15")
        self.dteNow = QtGui.QDateTimeEdit(dlgPilatus)
        self.dteNow.setGeometry(QtCore.QRect(10, 482, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.dteNow.setFont(font)
        self.dteNow.setReadOnly(True)
        self.dteNow.setDate(QtCore.QDate(2016, 3, 10))
        self.dteNow.setTime(QtCore.QTime(13, 0, 0))
        self.dteNow.setMaximumTime(QtCore.QTime(22, 59, 59))
        self.dteNow.setObjectName("dteNow")
        self.label_9 = QtGui.QLabel(dlgPilatus)
        self.label_9.setGeometry(QtCore.QRect(330, 480, 171, 21))
        self.label_9.setObjectName("label_9")
        self.lblStorageRingCurrent = QtGui.QLabel(dlgPilatus)
        self.lblStorageRingCurrent.setGeometry(QtCore.QRect(470, 500, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.lblStorageRingCurrent.setFont(font)
        self.lblStorageRingCurrent.setStyleSheet("color:green")
        self.lblStorageRingCurrent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblStorageRingCurrent.setIndent(0)
        self.lblStorageRingCurrent.setObjectName("lblStorageRingCurrent")
        self.line = QtGui.QFrame(dlgPilatus)
        self.line.setGeometry(QtCore.QRect(10, 460, 571, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtGui.QGroupBox(dlgPilatus)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 571, 71))
        self.groupBox.setObjectName("groupBox")
        self.leDataFolder = QtGui.QLineEdit(self.groupBox)
        self.leDataFolder.setGeometry(QtCore.QRect(20, 30, 531, 29))
        self.leDataFolder.setObjectName("leDataFolder")

        self.retranslateUi(dlgPilatus)
        QtCore.QMetaObject.connectSlotsByName(dlgPilatus)

    def retranslateUi(self, dlgPilatus):
        dlgPilatus.setWindowTitle(QtGui.QApplication.translate("dlgPilatus", "Pilatus1M Detector control for Size Exclusion Chromatography SAXS", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("dlgPilatus", "Sample Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlgPilatus", "Sample code ( < 8 characters):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dlgPilatus", "Sample description (< 80 characters):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("dlgPilatus", "Pilatus 1M detector", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("dlgPilatus", "Exposure time (s):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("dlgPilatus", "Number of frames:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("dlgPilatus", "Detector status:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDetectorStatus.setText(QtGui.QApplication.translate("dlgPilatus", "Idle", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStartPilatus.setText(QtGui.QApplication.translate("dlgPilatus", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("dlgPilatus", "Wait time (s):", None, QtGui.QApplication.UnicodeUTF8))
        self.pbStopPilatus.setText(QtGui.QApplication.translate("dlgPilatus", "STOP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRunNumber.setText(QtGui.QApplication.translate("dlgPilatus", "----", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("dlgPilatus", "Ring current (mA):", None, QtGui.QApplication.UnicodeUTF8))
        self.dteNow.setDisplayFormat(QtGui.QApplication.translate("dlgPilatus", "MM/dd/yyyy hh:mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("dlgPilatus", "Run number:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStorageRingCurrent.setText(QtGui.QApplication.translate("dlgPilatus", "102.2", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("dlgPilatus", "Log file full path", None, QtGui.QApplication.UnicodeUTF8))

