import sys
import csv
from sqlite3 import *
from datetime import date

from PyQt5 import QtSql
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


from mainengFunctions import *



#---------------------------------------------------------------------------------------

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Stock Control")


class Language(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap("images/Bennie2.jpg")
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setStyleSheet("margin-top: 50px 50px;")
        widgets["logo"].append(self.logo)

        self.comp_name = QLabel("Laeveld Agrochem Prieska")
        self.comp_name.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_name.setStyleSheet(''' 
            *{
                font-size: 45px;
                padding: 25px 0;
                margin: 100px 100px;
            }''')        
        widgets["comp_name"].append(self.comp_name)


        self.button1 = QPushButton("English")
        self.button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.resize(200, 32)
        self.button2 = QPushButton("Afrikaans")
        self.button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.resize(200, 32 )
        

        # Place Global widgets on grid
        grid.addWidget(self.logo, 0, 0, 2, 4)
        grid.addWidget(self.button1, 3, 0, 1, 2)
        grid.addWidget(self.button2, 2, 0, 1, 2)
        grid.addWidget(self.comp_name, 4, 0, 2, 4)


        # Buttons callback
        self.button1.clicked.connect(MainMenu)
        widgets["button1"].append(self.button1)     
        #self.button2.clicked.connect(hoofkieslys)
        widgets["button2"].append(self.button2)

Language()


main_window.setLayout(grid)

# show / run main window
main_window.show()
sys.exit(app.exec_())
