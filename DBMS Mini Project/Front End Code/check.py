import mysql.connector

try:
    cnx = mysql.connector.connect(host="127.0.0.1", username="root", password="Sayyam@123", database="mydata")
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
else:
    print("Connection established successfully")
    cnx.close()

import tkinter as tk

root = tk.Tk()
width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()
root.destroy()

print("Width: {} px, Height: {} px".format(width_px, height_px))
