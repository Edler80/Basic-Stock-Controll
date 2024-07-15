import sys
import csv
import sqlite3
from datetime import date

from PyQt5 import QtGui, QtCore, QtWidgets, QtSql

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *



comp_name1 = "Laeveld Agrochem Prieska"


# ---- SQL Tables (creat new tables if not exist) ----
# Create a product details table
stockcontrol = sqlite3.connect('productdetails.db')
cursor = stockcontrol.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS productdetails(
            prod_num    VARCHAR     NOT NULL,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL
);""")
stockcontrol.commit()
stockcontrol.close()

#Creat 1 database for test
stockcontrol1  = sqlite3.connect('stockcontrol1.db')
cursor = stockcontrol1.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stockcontrol1(
        prod_num    VARCHAR     NOT NULL,
        prod_name   VARCHAR     NOT NULL,
        supplier    VARCHAR     NOT NULL,
        uom         VARCHAR     NOT NULL,
        date        DATE,
        qty_r       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_s       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_ad      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_b       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        inv_num     VARCHAR,
        customer    VARCHAR,
        reason      VARCHAR,
        type        VARCHAR      NOT NULL ON CONFLICT REPLACE DEFAULT 0
);""")

stockcontrol1.commit()
stockcontrol1.close()

#------------------------------------------------------------------------------------------

# App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Stock Controller")
main_window.resize(700, 700)

#---------------------------------------------------------------------------------------
# Global Dictionary of dynamically changing widgets
widgets = {
    "logo": [],
    "comp_name": [],
    "menu_name": [],
    "button1": [],
    "button2": [],
    "button3": [],
    "button4": [],
    "button5": [],
    "button6": [],
    "product_table": [],
    "product_code": [],
    "product_name": [],
    "product_supplier": [],
    "product_code1": [],
    "product_name1": [],
    "product_supplier1": [],
    "uom": [],
    "uom1": [],
    "date": [],
    "date1": [],
    "qty": [],
    "qty1": [],
    "receipt_table": []

}
#-------------------------------------------------------------------------------------
# initiallize grid layout
grid = QGridLayout()

# To clear widget for the next menu
def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

#------------------------------------------------------------------------------------
# Create Main Menu 
class MainMenu(QWidget):
    clear_widgets()
    def __init__(self):
        super().__init__()
        clear_widgets()
        self.image = QPixmap("images/Bennie2.jpg")
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setStyleSheet("margin-top: 100px;")
        widgets["logo"].append(self.logo)

        self.comp_name = QLabel(comp_name1)
        self.comp_name.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_name.setStyleSheet(''' 
            *{
                font-size: 45px;
                padding: 25px 0;
                margin: 100px 100px;
            }''')
        widgets["comp_name"].append(self.comp_name)

        self.menu_name = QLabel("Main Menu")
        self.menu_name.setAlignment(QtCore.Qt.AlignLeft)
        self.menu_name.setStyleSheet(''' 
            *{
                font-size: 25px;
                padding: 25px 0;
                margin: 10px 50px;
            }
            ''')
        widgets["menu_name"].append(self.menu_name)


        self.button1 = QPushButton("View Stock")
        self.button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button2 = QPushButton("Receipt")
        self.button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button3 = QPushButton("Sales")
        self.button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button4 = QPushButton("Alterations")
        self.button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button5 = QPushButton("Product Details")
        self.button5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button6 = QPushButton("Exit")
        self.button6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


        # Buttons callback
        self.button1.clicked.connect(view_stock_menu)
        widgets["button1"].append(self.button1)
        self.button2.clicked.connect(receipt_menu)
        widgets["button2"].append(self.button2)
        self.button3.clicked.connect(sales_menu)
        widgets["button3"].append(self.button3)
        self.button4.clicked.connect(alterations_menu)
        widgets["button4"].append(self.button4)
        self.button5.clicked.connect(product_details_menu)
        widgets["button5"].append(self.button5)
        self.button6.clicked.connect(exit_menu)
        widgets["button6"].append(self.button6)

        # Place Global widgets on grid
        grid.addWidget(widgets["logo"][-1], 6, 0, 1, 4)
        grid.addWidget(widgets["comp_name"][-1], 1, 0, 1, 3)
        grid.addWidget(widgets["menu_name"][-1], 2, 0, 1, 2)
        grid.addWidget(widgets["button1"][-1], 3, 0, 1, 1)
        grid.addWidget(widgets["button2"][-1], 3, 1, 1, 1)
        grid.addWidget(widgets["button3"][-1], 3, 2, 1, 1)
        grid.addWidget(widgets["button4"][-1], 4, 0, 1, 1)
        grid.addWidget(widgets["button5"][-1], 4, 1, 1, 1)
        grid.addWidget(widgets["button6"][-1], 4, 2, 1, 1)


#---------------------------------------------------------------------------------------
# --- view stock Balance section ---
def view_stock_menu():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("View Stock Menu")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("View Stock Balance")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Main Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(view_stock)
    widgets["button1"].append(button1)
    button4.clicked.connect(MainMenu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)
    grid.addWidget(widgets["logo"][-1], 6, 0, 1, 4)  


def view_stock():
    pass

#----------------------------------------------------------------------------------------
# --- Receipt Section ---
def receipt_menu():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("Receipt Menu")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("Add New Stock")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2 = QPushButton("View Receipt")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Main Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(NewReceipts)
    widgets["button1"].append(button1)
    button2.clicked.connect(view_received_stock)
    widgets["button2"].append(button2)
    button4.clicked.connect(MainMenu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button2"][-1], 2, 2, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)
    grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

class NewReceipts(QWidget):
    def __init__(self):
        super().__init__()
        clear_widgets()
        self.image = QPixmap("images/Bennie2.jpg")
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setStyleSheet("margin-top: 100px;")
        widgets["logo"].append(self.logo)

        self.menu_name = QLabel("Add new Receipt")
        self.menu_name.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_name.setStyleSheet(''' 
            *{
                font-size: 25px;
                padding: 25px 0;
                margin: 10px 50px;
            }
            ''')
        widgets["menu_name"].append(self.menu_name)


        self.button4 = QPushButton("Back to Receipt Menu")
        self.button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button4.clicked.connect(receipt_menu)
        widgets["button4"].append(self.button4)

        grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
        grid.addWidget(widgets["logo"][-1], 9, 0, 1, 4)
        grid.addWidget(widgets["button4"][-1], 8, 2, 1, 2)

        def product_code_def():
            self.product_code1 = QLineEdit()
            widgets["product_code1"].append(self.product_code1)
            self.product_code = QLabel("Product Code:")
            widgets["product_code"].append(self.product_code)
            grid.addWidget(widgets["product_code"][-1], 2, 0, 1, 1)
            grid.addWidget(widgets["product_code1"][-1], 2, 1, 1, 2)

        product_code_def()
        
        def product_name_def():
            self.product_name1 = QLineEdit()
            widgets["product_name1"].append(self.product_name1)
            self.product_name = QLabel("Product Name:")
            widgets["product_name"].append(self.product_name)
            grid.addWidget(widgets["product_name"][-1], 3, 0, 1, 1)
            grid.addWidget(widgets["product_name1"][-1], 3, 1, 1, 2)

        product_name_def()

        def supplier_def():
            self.product_supplier1 = QLineEdit()
            widgets["product_supplier1"].append(self.product_supplier1)
            self.product_supplier = QLabel("Supplier:")
            widgets["product_supplier"].append(self.product_supplier)
            grid.addWidget(widgets["product_supplier"][-1], 4, 0, 1, 1)
            grid.addWidget(widgets["product_supplier1"][-1], 4, 1, 1, 2)
        
        supplier_def()
        
        def uom_def():
            self.uom1 = QLineEdit()
            widgets["uom1"].append(self.uom1)
            self.uom = QLabel("UOM:")
            widgets["uom"].append(self.uom)
            grid.addWidget(widgets["uom"][-1], 5, 0, 1, 1)
            grid.addWidget(widgets["uom1"][-1], 5, 1, 1, 2)

        uom_def()

        def date_def():
            self.date1 = QLineEdit()
            widgets["date1"].append(self.date1)
            self.date = QLabel("Date(dd/mm/yyyy):")
            widgets["date"].append(self.date)
            grid.addWidget(widgets["date"][-1], 6, 0, 1, 1)
            grid.addWidget(widgets["date1"][-1], 6, 1, 1, 2)

        date_def()

        def qty_r_def():
            self.qty1 = QLineEdit()
            widgets["qty1"].append(self.qty1)
            self.qty = QLabel("QTY Received:")
            widgets["qty"].append(self.qty)
            grid.addWidget(widgets["qty"][-1], 7, 0, 1, 1)
            grid.addWidget(widgets["qty1"][-1], 7, 1, 1, 2)
        
        qty_r_def()

        def button():
            button1 = QPushButton('Add Receipt', self)
            button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            button1.clicked.connect(self.addReceipt1)
            widgets["button1"].append(button1)
            grid.addWidget(widgets["button1"][-1], 8, 0, 1, 2)
        
        button()
         
    def addReceipt1(self):
        product_receipt = sqlite3.connect('Stockcontrol1.db')
        cursor = product_receipt.cursor()
        
        code = self.product_code1.text()
        name = self.product_name1.text()
        supplier = self.product_supplier1.text()  
        uom = self.uom1.text()
        date = self.date1.text()
        qty_r = self.qty1.text()

        cursor.execute('''INSERT INTO stockcontrol1(prod_num, prod_name,supplier, 
            uom, date, qty_r) VALUES(?,?,?,?,?,?)''',
            (code, name, supplier, uom, date,qty_r))
        
        product_receipt.commit()
        product_receipt.close()

def view_received_stock():
    clear_widgets()
    menu_name = QLabel("Receipts")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button4 = QPushButton("Receipt Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button4.clicked.connect(receipt_menu)
    widgets["button4"].append(button4)

    receipt_table = QTableWidget()
    receipt_table.setColumnCount(6) #Code, Name, Supplier, uom, date, qty_r
    receipt_table.setHorizontalHeaderLabels(["Code", "Product Name", "Supplier",
                "UOM", "Date", "qty_r"])
    receipt_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    receipt_table.setSortingEnabled(True)
    receipt_table.sortByColumn(1, QtCore.Qt.AscendingOrder)

    scroll_bar = QScrollBar()
    scroll_bar.setStyleSheet("background : lightgreen;")
    receipt_table.addScrollBarWidget(scroll_bar, Qt.AlignLeft)
    widgets["receipt_table"].append(receipt_table)
    
    
    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button4"][-1], 1, 2, 1, 2) 
    grid.addWidget(receipt_table, 3, 0)

    receipt_table.setRowCount(0)
    receipttable = sqlite3.connect('stockcontrol1.db')
    cursor = receipttable.cursor()
    
    view_type = "Receipt"
    # Add detail to table
    cursor.execute('''SELECT * FROM stockcontrol1 
                WHERE type = ?''',(view_type,))
    products = cursor.fetchall()

    row = 0
    for prod_rec in products:
        product_code =  prod_rec[0]
        product_name = prod_rec[1]
        prod_supplier = prod_rec[2]
        prod_uom = prod_rec[3]
        prod_date = prod_rec[4]
        prod_qtyr = prod_rec[5]

        #add values to Product details Table
        receipt_table.insertRow(row)

        receipt_table.setItem(row, 0, QTableWidgetItem(product_code))
        receipt_table.setItem(row, 1, QTableWidgetItem(product_name))
        receipt_table.setItem(row, 2, QTableWidgetItem(prod_supplier))
        receipt_table.setItem(row, 3, QTableWidgetItem(prod_uom))
        receipt_table.setItem(row, 4, QTableWidgetItem(prod_date))
        receipt_table.setItem(row, 5, QTableWidgetItem(prod_qtyr))

        row += 1

#----------------------------------------------------------------------------------------
# Sales Section
def sales_menu():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("Sold Menu")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("Add new Sales")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2 = QPushButton("view Sales")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Main Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(new_sales)
    widgets["button1"].append(button1)
    button2.clicked.connect(view_sales)
    widgets["button2"].append(button2)
    button4.clicked.connect(MainMenu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button2"][-1], 2, 2, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)  
    grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

def new_sales():
    pass

def view_sales():
    clear_widgets()
    menu_name = QLabel("Receipts")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button4 = QPushButton("Receipt Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button4.clicked.connect(receipt_menu)
    widgets["button4"].append(button4)

    receipt_table = QTableWidget()
    receipt_table.setColumnCount(6) #Code, Name, Supplier, uom, date, qty_r
    receipt_table.setHorizontalHeaderLabels(["Code", "Product Name", "Supplier",
                "UOM", "Date", "qty_r"])
    receipt_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    receipt_table.setSortingEnabled(True)
    receipt_table.sortByColumn(1, QtCore.Qt.AscendingOrder)

    scroll_bar = QScrollBar()
    scroll_bar.setStyleSheet("background : lightgreen;")
    receipt_table.addScrollBarWidget(scroll_bar, Qt.AlignLeft)
    widgets["receipt_table"].append(receipt_table)
    
    
    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button4"][-1], 1, 2, 1, 2) 
    grid.addWidget(receipt_table, 3, 0)

    receipt_table.setRowCount(0)
    receipttable = sqlite3.connect('stockcontrol1.db')
    cursor = receipttable.cursor()
    
    view_type = "Receipt"
    # Add detail to table
    cursor.execute('''SELECT * FROM stockcontrol1 
                WHERE type = ?''',(view_type,))
    products = cursor.fetchall()

    row = 0
    for prod_rec in products:
        product_code =  prod_rec[0]
        product_name = prod_rec[1]
        prod_supplier = prod_rec[2]
        prod_uom = prod_rec[3]
        prod_date = prod_rec[4]
        prod_qtyr = prod_rec[5]

        #add values to Product details Table
        receipt_table.insertRow(row)

        receipt_table.setItem(row, 0, QTableWidgetItem(product_code))
        receipt_table.setItem(row, 1, QTableWidgetItem(product_name))
        receipt_table.setItem(row, 2, QTableWidgetItem(prod_supplier))
        receipt_table.setItem(row, 3, QTableWidgetItem(prod_uom))
        receipt_table.setItem(row, 4, QTableWidgetItem(prod_date))
        receipt_table.setItem(row, 5, QTableWidgetItem(prod_qtyr))

        row += 1

#-----------------------------------------------------------------------------------------
# --- Alterations Section ---
def alterations_menu():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("Alterations Menu")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("Reduce Stock")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2 = QPushButton("Increase Stock")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button3 = QPushButton("View Alterations")
    button3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Main Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(reduce_stock)
    widgets["button1"].append(button1)
    button2.clicked.connect(increase_stock)
    widgets["button2"].append(button2)
    button3.clicked.connect(view_alterations)
    widgets["button3"].append(button3)
    button4.clicked.connect(MainMenu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button2"][-1], 2, 2, 1, 2)
    grid.addWidget(widgets["button3"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)    
    grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

def reduce_stock():
    pass

def increase_stock():
    pass

def view_alterations():
    pass

#---------------------------------------------------------------------------------------
# --- Product Details Section ---
def product_details_menu():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("Product Details")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
            *{
                font-size: 25px;
                padding: 25px 0;
                margin: 10px 50px;
                }''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("View all Product Items")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2 = QPushButton("Add New Stock Item")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Main Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(view_product_items)
    widgets["button1"].append(button1)
    button2.clicked.connect(add_new_item)
    widgets["button2"].append(button2)
    button4.clicked.connect(MainMenu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button2"][-1], 2, 2, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)  
    grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

def view_product_items():
    clear_widgets()
    menu_name = QLabel("Product Details List")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button4 = QPushButton("Back to Product Details Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button4.clicked.connect(product_details_menu)
    widgets["button4"].append(button4)

    product_table = QTableWidget()
    product_table.setColumnCount(3) #Code, Name, Supplier
    product_table.setHorizontalHeaderLabels(["Code", "Product Name", "Supplier"])
    product_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    product_table.setSortingEnabled(True)
    product_table.sortByColumn(1, QtCore.Qt.AscendingOrder)

    scroll_bar = QScrollBar()
    scroll_bar.setStyleSheet("background : lightgreen;")
    product_table.addScrollBarWidget(scroll_bar, Qt.AlignLeft)
    widgets["product_table"].append(product_table)
    
    
    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button4"][-1], 1, 2, 1, 2) 
    grid.addWidget(product_table, 3, 0)

    product_table.setRowCount(0)
    stockcontroll = sqlite3.connect('productdetails.db')
    cursor = stockcontroll.cursor()
    
    # Add detail to table
    cursor.execute("SELECT * FROM productdetails")
    products = cursor.fetchall()

    row = 0
    for prod_det in products:
        product_code =  prod_det[0]
        product_name = prod_det[1]
        prod_supplier = prod_det[2]

        #add values to Product details Table
        product_table.insertRow(row)

        product_table.setItem(row, 0, QTableWidgetItem(product_code))
        product_table.setItem(row, 1, QTableWidgetItem(product_name))
        product_table.setItem(row, 2, QTableWidgetItem(prod_supplier))

        row += 1

def add_new_item():
    clear_widgets()
    image = QPixmap("images/Bennie2.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    menu_name = QLabel("Add New Product detail")
    menu_name.setAlignment(QtCore.Qt.AlignCenter)
    menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 50px;
        }
        ''')
    widgets["menu_name"].append(menu_name)


    button1 = QPushButton("Add Single Product")
    button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button2 = QPushButton("Import CSV file")
    button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button4 = QPushButton("Back to Product Details Menu")
    button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Buttons callback
    button1.clicked.connect(NewProduct)
    widgets["button1"].append(button1) 
    button2.clicked.connect(import_items)
    widgets["button2"].append(button2)
    button4.clicked.connect(product_details_menu)
    widgets["button4"].append(button4)
    

    # Place Global widgets on grid
    grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)
    grid.addWidget(widgets["button1"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["button2"][-1], 2, 2, 1, 2)
    grid.addWidget(widgets["button4"][-1], 3, 2, 1, 2)
    grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

class NewProduct(QWidget):
    clear_widgets()
    def __init__(self):
        clear_widgets()
        super().__init__()
        clear_widgets()
        self.image = QPixmap("images/Bennie2.jpg")
        self.logo = QLabel()
        self.logo.setPixmap(self.image)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setStyleSheet("margin-top: 100px;")
        widgets["logo"].append(self.logo)

        self.menu_name = QLabel("Add New Product detail")
        self.menu_name.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_name.setStyleSheet(''' 
        *{
            font-size: 25px;
            padding: 25px 0;
            margin: 10px 20px;
        }
        ''')
        widgets["menu_name"].append(self.menu_name)

        self.product_code1 = QLineEdit(self)
        widgets["product_code1"].append(self.product_code1)
        self.product_name1 = QLineEdit(self)
        widgets["product_name1"].append(self.product_name1)
        self.product_supplier1 = QLineEdit(self)
        widgets["product_supplier1"].append(self.product_supplier1)

        self.button1 = QPushButton("Add new Product")
        self.button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button4 = QPushButton("Product Detail Menu")
        self.button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        widgets["button1"].append(self.button1)
        widgets["button4"].append(self.button4)
              
        self.product_code = QLabel("Product Code:")
        widgets["product_code"].append(self.product_code)
        self.product_name = QLabel("Product Name:")
        widgets["product_name"].append(self.product_name)
        self.product_supplier = QLabel("Supplier:")
        widgets["product_supplier"].append(self.product_supplier)
    
        grid.addWidget(widgets["menu_name"][-1], 0, 0, 1, 4)

        grid.addWidget(widgets["product_code"][-1], 2, 0, 1, 1)
        grid.addWidget(widgets["product_code1"][-1], 2, 1, 1, 2)
        grid.addWidget(widgets["product_name"][-1], 3, 0, 1, 1)
        grid.addWidget(widgets["product_name1"][-1], 3, 1, 1, 2)
        grid.addWidget(widgets["product_supplier"][-1], 4, 0, 1, 1)
        grid.addWidget(widgets["product_supplier1"][-1], 4, 1, 1, 2)
        
        grid.addWidget(widgets["button1"][-1], 6, 0, 1, 2)
        grid.addWidget(widgets["button4"][-1], 6, 2, 1, 2) 

        grid.addWidget(widgets["logo"][-1], 7, 0, 1, 4)

        self.button1.clicked.connect(self.add_product)
        self.button4.clicked.connect(product_details_menu)
            
    def add_product(self):
        product_details = sqlite3.connect('productdetails.db')
        cursor = product_details.cursor()
        
        code = self.product_code1.text()
        name = self.product_name1.text()
        supplier = self.product_supplier1.text()   
        
              
        cursor.execute('''INSERT INTO productdetails(prod_num, prod_name, ) 
                    VALUES(?, ?, ?)''', (code, name, supplier,))
            

        QMessageBox.warning(None, "Note", "New Item was added")

        product_details.commit()
        product_details.close()
            
        self.product_code1.clear()
        self.product_name1.clear()
        self.product_supplier1.clear()
    
        add_new_item()
     
def import_items():
    clear_widgets()
    QMessageBox.warning(None, "Note", "Import new CSV file will overide all current products details")
    
    confirm = QMessageBox.question(None, "Import", "Would you like to continue the import?", QMessageBox.Yes | QMessageBox.No )

    if confirm == QMessageBox.No:
        product_details_menu()
    
    product_details = sqlite3.connect('productdetails.db')
    cursor = product_details.cursor()

    cursor.execute("DELETE FROM productdetails;")

    with open('productdetails.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

    for row in data:
        cursor.execute("""
                       INSERT INTO pproductdetails(prod_num, prod_name, supplier)
                       VALUES(?, ?, ?)""", row)
    
    product_details.commit()  
    product_details.close()

    QMessageBox.warning(None, "Note", "Import done")  

    product_details_menu()

#----------------------------------------------------------------------------------------
# --- Exit Section ---
def exit_menu():
    exit()


#----------------------------------------------------------------------------------------

.





# Create a PyQt5 QSQLITE database
#product details database
stockcontrol = QSqlDatabase.addDatabase("QSQLITE1") 
stockcontrol.setDatabaseName("productdetails.db")
if not stockcontrol.open():
    QMessageBox.critical(None, "Error","Could not open your Database")
    sys.exit(1)

query = QSqlQuery()
query.exec_("""
        CREATE TABLE IF NOT EXISTS productdetails (
            prod_num    VARCHAR     NOT NULL,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL
);""")

#Create database for all receipt, sales and adjustment
stockcontrol1 = QSqlDatabase.addDatabase("QSQLITE2")
stockcontrol1.setDatabaseName("stockcontrol1.db")
if not stockcontrol1.open():
    QMessageBox.critical(None, "Error","Could not open your Database")
    sys.exit(1)

query = QSqlQuery()
query.exec_(""" 
    CREATE TABLE IF NOT EXISTS stockcontrol1(
        prod_num    VARCHAR     NOT NULL,
        prod_name   VARCHAR     NOT NULL,
        supplier    VARCHAR     NOT NULL,
        uom         VARCHAR     NOT NULL,
        date        DATE,
        qty_r       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_s       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_ad      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_b       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        inv_num     VARCHAR,
        customer    VARCHAR,
        reason      VARCHAR,
        type        VARCHAR      NOT NULL ON CONFLICT REPLACE DEFAULT 0
);""")

#Create database for Stock Balance
stockbalance = QSqlDatabase.addDatabase("QSQLITE3")
stockbalance.setDatabaseName("stockbalance.db")
if not stockbalance.open():
    QMessageBox.critical(None, "Error","Could not open your Database")
    sys.exit(1)

query = QSqlQuery()
query.exec_("""
    CREATE TABLE IF NOT EXISTS stockbalance(
        prod_num    VARCHAR     NOT NULL,
        prod_name   VARCHAR     NOT NULL,
        supplier    VARCHAR     NOT NULL,
        uom         VARCHAR     NOT NULL,
        qty_tr      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_ts      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_tad     INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
        qty_bal     INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0
);""")






















