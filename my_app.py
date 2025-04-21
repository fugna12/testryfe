from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoudleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import(
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListView, QLineEdit)


from instr import *
from second_win import *




class MainWin(QWidget):
    def __init__(self):
        ssuper().__init__()


        self.initUI()

        self.connects()


        self.set_appear()

        self.show()

    def initUI(self):
        self.dtn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)