import sys
import csv
import sqlite3
import datetime

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *


comp_name1 = "Laeveld Agrochem Prieska"


# ---- SQL Tables (creat new tables if not exist) ----
# Create a product details table
stockcontroll = sqlite3.connect('stockcontroll.db')
cursor = stockcontroll.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_details (
            prod_num    VARCHAR     RIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL
)""")
stockcontroll.commit()
stockcontroll.close()

# Create a receive table
stockcontroll = sqlite3.connect('stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute("""
        CREATE TABLE IF NOT EXISTS receipt(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_r       INTERGER    NOT NULL
);""")

stockcontroll.commit()
stockcontroll.close()

# Create a sold table
stockcontroll = sqlite3.connect('stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_s       INTERGER    NOT NULL,
            inv_num     VARCHAR     NOT NULL,
            customer    VARCHAR     NOT NULL
);""")

stockcontroll.commit()
stockcontroll.close()

# Create a Stock alteration table
stockcontroll = sqlite3.connect('stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alterration(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_ad      INTERGER    NOT NULL,
            reason      VARCHAR     NOT NULL
);""")

stockcontroll.commit()
stockcontroll.close()

# Create a stock balance table
stockcontroll = sqlite3.connect('stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_balance(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            qty_r       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_s       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_ad      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_b       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0
);""")

stockcontroll.commit()
stockcontroll.close()


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
    "product_supplier1": []

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
    button1.clicked.connect(new_stock_received)
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

def new_stock_received():
   pass

def view_received_stock():
    pass

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
    pass

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
    stockcontroll = sqlite3.connect('stockcontroll.db')
    cursor = stockcontroll.cursor()
    
    # Add detail to table
    cursor.execute("SELECT * FROM product_details")
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

        self.product_code1 = QLineEdit()
        widgets["product_code"].append(self.product_code1)
        self.product_name1 = QLineEdit()
        widgets["product_name"].append(self.product_name1)
        self.product_supplier1 = QLineEdit()
        widgets["product_supplier"].append(self.product_supplier1)

        
        self.button1 = QPushButton("Add new Product")
        self.button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button4 = QPushButton("Product Detail Menu")
        self.button4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.button1.clicked.connect(self.add_product)
        widgets["button1"].append(self.button1)
        self.button4.clicked.connect(product_details_menu)
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
            
    def add_product(self):
        clear_widgets()
        code = self.product_code1.text()
        name = self.product_name1.text()
        supplier = self.product_supplier1.text()   
        
        if len(code) and len(name) >= 1:
            product_details = sqlite3.connect('stockcontroll.db')
            cursor = product_details.cursor()

            cursor = QSqlQuery
            cursor.prepare("""
                INSERT INTO product_details(prod_num, prod_name, supplier)
                VALUES (?, ?, ?)""")
            cursor.addBindValue(code)
            cursor.addBindValue(name)
            cursor.addBindValue(supplier)
            cursor.exec_()

            product_details.commit()
            product_details.close()

            self.product_code1.clear()
            self.product_name1.clear()
            self.product_supplier1.clear()
            
            product_details.commit()
            product_details.close()

        



def import_items():
    clear_widgets()
    QMessageBox.warning(None, "Note", "Import new CSV file will overide all current products details")
    
    confirm = QMessageBox.question(None, "Import", "Would you like to continue the import?", QMessageBox.Yes | QMessageBox.No )

    if confirm == QMessageBox.No:
        product_details_menu()
    
    product_details = sqlite3.connect('stockcontroll.db')
    cursor = product_details.cursor()

    cursor.execute("DELETE FROM product_details;")

    with open('productdetails.csv') as f:
        reader = csv.reader(f)
        data = list(reader)

    for row in data:
        cursor.execute("""
                       INSERT INTO product_details(prod_num, prod_name, supplier)
                       VALUES(?, ?, ?)""", row)
    
    product_details.commit()
    

    product_details_menu()

#----------------------------------------------------------------------------------------
# --- Exit Section ---
def exit_menu():

    """stockcontroll.commit()
    stockcontroll.close()"""
    sys.exit(app.exec_())

#----------------------------------------------------------------------------------------
