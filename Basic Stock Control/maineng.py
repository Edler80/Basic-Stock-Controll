import sys
import csv
import sqlite3
import datetime

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

from mainengFunctions import *



#---------------------------------------------------------------------------------------

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Stock Control")



MainMenu()



main_window.setLayout(grid)

# show / run main window
main_window.show()
sys.exit(app.exec_())




