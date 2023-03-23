from PyQt5.QtWidgets import QMainWindow, QApplication, QStyledItemDelegate, QLineEdit
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.uic import loadUi
from PyQt5.QtCore import QRegExp
import pyqtgraph as pg
import sys
import qdarktheme

import os
import pyuac
from distutils.core import setup

class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("^-?[0-9]\d*(\.\d+)?$")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor
    


class MainUI(QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        
        loadUi("dns_changer_ui.ui", self)
        
        self.setFixedSize(380, 200)
        self.setWindowTitle("DNS Changer")

        onlyInteger = QIntValidator()
        self.etDNS11.setValidator(onlyInteger)
        self.etDNS12.setValidator(onlyInteger)
        self.etDNS13.setValidator(onlyInteger)
        self.etDNS14.setValidator(onlyInteger)

        self.etDNS21.setValidator(onlyInteger)
        self.etDNS22.setValidator(onlyInteger)
        self.etDNS23.setValidator(onlyInteger)
        self.etDNS24.setValidator(onlyInteger)

        self.btnApply.clicked.connect(self.btnApplyClickHandler)
        self.btnApply.setStyleSheet("background-color: gray")
    
    def btnApplyClickHandler(self):
        btnText = self.btnApply.text()
        if btnText == "Disabled":
            DNS1 = ""
            DNS1 += self.etDNS11.text() + "."
            DNS1 += self.etDNS12.text() + "."
            DNS1 += self.etDNS13.text() + "."
            DNS1 += self.etDNS14.text()

            DNS2 = ""
            DNS2 += self.etDNS21.text() + "."
            DNS2 += self.etDNS22.text() + "."
            DNS2 += self.etDNS23.text() + "."
            DNS2 += self.etDNS24.text()

            os.system(f'netsh interface ip set dns name="Wi-Fi" static {DNS1}')
            os.system(f'netsh interface ip add dns name="Wi-Fi"  {DNS2} index=2')

            self.btnApply.setText('Enabled')
            self.btnApply.setStyleSheet("background-color: green")
        else:
            os.system('netsh interface ip set dnsservers name="Wi-Fi" source=dhcp')
            self.btnApply.setText('Disabled')
            self.btnApply.setStyleSheet("background-color: gray")

    
    
if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin()
    else:        
        qdarktheme.enable_hi_dpi()
        app = QApplication(sys.argv)
        qdarktheme.setup_theme(corner_shape="rounded")
        ui = MainUI()
        ui.show()
        app.exec_()