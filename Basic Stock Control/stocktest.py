# Import Modules
import sys
import sqlite3
import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

# ---- SQL Tables (creat new tables if not exist) ----
# Create a product details table
stockcontroll = sqlite3.connect('/database/Stockcontroll.db')
cursor = stockcontroll.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product_details(
            prod_num    VARCHAR     RIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL
);''')

stockcontroll.commit()
stockcontroll.close()

# Create a receive table
stockcontroll = sqlite3.connect('/database/Stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS receipt(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_r       INTERGER    NOT NULL,
);''')

stockcontroll.commit()

# Create a sold table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_s       INTERGER    NOT NULL,
            inv_num     VARCHAR     NOT NULL,
            customer    VARCHAR     NOT NULL
);''')

stockcontroll.commit()
stockcontroll.close()

# Create a Stock alteration table
stockcontroll = sqlite3.connect('/database/Stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alterration(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            date        DATE        NOT NULL,
            qty_ad      INTERGER    NOT NULL,
            reason      VARCHAR     NOT NULL
);''')

stockcontroll.commit()
stockcontroll.close()

# Create a stock balance table
stockcontroll = sqlite3.connect('/database/Stockcontroll.db')
cursor = stockcontroll.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS control(
            prod_num    VARCHAR     PRIMARY KEY,
            prod_name   VARCHAR     NOT NULL,
            supplier    VARCHAR     NOT NULL,
            uom         VARCHAR     NOT NULL,
            qty_r       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_s       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_ad      INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0,
            qty_b       INTERGER    NOT NULL ON CONFLICT REPLACE DEFAULT 0
);''')

stockcontroll.commit()
stockcontroll.close()

#---------------------------------------------------------------------------------------
# define functions

def main_menu():
    print("1.   View Stock Balance")
    print("2.   Enter Receipt")
    print("3.   Selling")
    print("4.   Stock Controll")
    print("5.   Product Details")
    print("6.   Exit")

    global mainmenu_s
    mainmenu_s = ""







