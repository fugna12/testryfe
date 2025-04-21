from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidaqtor, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *        

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment():
    def __init__(self, person, test1, test2, test3):
        self.person = person
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.connects()

        self.set_appear()

        self.show()

        


win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = ''
txt_next = ''
txt_instruction = '' 
txt_title = ''
txt_name = 'Введите ФИО:'
txt_hintname = ""
txt_hintage = "Полных лет:"
txt_test1 = ''
txt_test2 = ''
txt_test3 = ''
txt_sendresults = ''
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = ''
txt_starttest2 = ''
txt_starttest3 = ''

txt_age = 'Полных лет:'
txt_finalwin = ''
txt_index = ''
txt_workheart = ''