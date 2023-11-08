import sys
from random import random
from tokenize import String

from PyQt6.QtWidgets import QDialog, QApplication

from sprawdzian import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.internista.toggled.connect(self.QRadioButton)
        self.ui.pediatra.toggled.connect(self.QRadioButton)
        self.ui.dermatolog.toggled.connect(self.QRadioButton)
        self.ui.pushButton.clicked.connect(self.QRadioButton)
        self.ui.checkBox.clicked.connect(self.QCheckBox)
        self.show()



    def QRadioButton(self):

        wybrany_lekarz = ""

        if self.ui.internista.isChecked():
            wybrany_lekarz = "internista"
        elif self.ui.pediatra.isChecked():
            wybrany_lekarz = "pediatra"
        elif self.ui.dermatolog.isChecked():
            wybrany_lekarz = "dermatolog"

        self.ui.lekarz_result.setText('wybrany lekarz: ' + wybrany_lekarz)



            


    def QCheckBox(self):
        if self.ui.checkBox.isChecked:
            self.ui.cena.setText('czas oczekiwania:' + random(int(0, 14)))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MyForm()
    windows.show()
    sys.exit(app.exec())
