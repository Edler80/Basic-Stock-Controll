# Import Modules
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import sqlite3
import datetime


# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Stock Controller")
main_window.resize(600, 600)

# App Objects
comp_name = QLabel("Company Name")

main_menu = QLabel("Main Menu")

button1 = QPushButton("View Stock")
button2 = QPushButton("Receipt")
button3 = QPushButton("Sales")
button4 = QPushButton("Alterations")
button5 = QPushButton("Product Details")
button6 = QPushButton("Exit")


# App Design
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()
row5 = QHBoxLayout()
row6 = QHBoxLayout()
row7 = QHBoxLayout()
row8 = QHBoxLayout()


row1.addWidget(comp_name, alignment=Qt.AlignCenter)
row2.addWidget(main_menu, alignment=Qt.AlignCenter)
row3.addWidget(button1)
row4.addWidget(button2)
row5.addWidget(button3)
row6.addWidget(button4)
row7.addWidget(button5)
row8.addWidget(button6)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
master_layout.addLayout(row4)
master_layout.addLayout(row5)
master_layout.addLayout(row6)
master_layout.addLayout(row7)

main_window.setLayout(master_layout)

# show / run main window
main_window.show()
app.exec_()
