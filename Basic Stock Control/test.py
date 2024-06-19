import sys
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5 import *

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        mylist = [['Admin',['int a','int b','int c'],
['Student',['int a','int b','int c','int d','int e']]]]


        for i in range(len(mylist)):
                table = QTableWidget()
                table.setColumnCount(1)
                table.setRowCount(len(mylist[i][1]))
                for j in range(len(mylist[i][1])):
                    table.setItem(j,0,QTableWidgetItem(mylist[i][1][j]))
                vBox = QVBoxLayout()
                vBox.addWidget(table)
                grid.addLayout(vBox,i,0)
    
        self.setWindowTitle('Basic Grid Layout')

 
app = QApplication(sys.argv)
windowExample = basicWindow()
windowExample.show()
sys.exit(app.exec_())