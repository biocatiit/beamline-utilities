import sys
from PySide.QtCore import *
from PySide.QtGui import *

import epics

topBladePV = '18ID:e:m29'
bottomBladePV = '18ID:e:m30'
inboardBladePV = '18ID:e:m31' # confirmed: inboard direction is -
outboardBladePV = '18ID:e:m32'

import uiSlit

class MainDialog(QDialog, uiSlit.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.updatePositions)
        
        self.connect(self.tbTopOpen, SIGNAL("clicked()"), self.openTopBlade)
        self.connect(self.tbTopClose, SIGNAL("clicked()"), self.closeTopBlade)
        self.connect(self.tbBottomOpen, SIGNAL("clicked()"), self.openBottomBlade)
        self.connect(self.tbInboardOpen, SIGNAL("clicked()"), self.openInboardBlade)
        self.connect(self.tbOutboardOpen, SIGNAL("clicked()"), self.openOutboardBlade)
        self.connect(self.tbBottomClose, SIGNAL("clicked()"), self.closeBottomBlade)
        self.connect(self.tbInboardClose, SIGNAL("clicked()"), self.closeInboardBlade)
        self.connect(self.tbOutboardClose, SIGNAL("clicked()"), self.closeOutboardBlade)

        self.connect(self.pbOpenAll, SIGNAL("clicked()"), self.openAllBlade)
        self.connect(self.pbCloseAll, SIGNAL("clicked()"), self.closeAllBlade)
        timer.start(100)

    def openTopBlade(self):
        epics.caput(topBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(topBladePV + '.TWF', 1, wait=True)

    def closeTopBlade(self):
        epics.caput(topBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(topBladePV + '.TWR', 1, wait=True)


    def closeBottomBlade(self):
        epics.caput(bottomBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(bottomBladePV + '.TWF', 1, wait=True)

    def openBottomBlade(self):
        epics.caput(bottomBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(bottomBladePV + '.TWR', 1, wait=True)


    def closeInboardBlade(self):
        epics.caput(inboardBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(inboardBladePV + '.TWF', 1, wait=True)

    def openInboardBlade(self):
        epics.caput(inboardBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(inboardBladePV + '.TWR', 1, wait=True)

    def openOutboardBlade(self):
        epics.caput(outboardBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(outboardBladePV + '.TWF', 1, wait=True)

    def closeOutboardBlade(self):
        epics.caput(outboardBladePV + '.TWV', float(self.spinBox.value())/1000, wait=True)
        epics.caput(outboardBladePV + '.TWR', 1, wait=True)

    def updatePositions(self):
        self.labelTopPosition.setText('%.03f' %epics.caget(topBladePV + '.RBV'))        
        self.labelBottomPosition.setText('%.03f' %epics.caget(bottomBladePV + '.RBV'))        
        self.labelInboardPosition.setText('%.03f' %epics.caget(inboardBladePV + '.RBV'))        
        self.labelOutboardPosition.setText('%.03f' %epics.caget(outboardBladePV + '.RBV'))        

    def openAllBlade(self):
        self.openTopBlade()
        self.openBottomBlade()
        self.openInboardBlade()
        self.openOutboardBlade()

    def closeAllBlade(self):
        self.closeTopBlade()
        self.closeBottomBlade()
        self.closeInboardBlade()
        self.closeOutboardBlade()

def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.setWindowTitle('Guard slit blades control')
    form.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
