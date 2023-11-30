from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

try:
    cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
else:
    print("Connection established successfully")
    cnx.close()
