import time
from datetime import *
from math import *
from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import Image, ImageTk, ImageDraw
from playsound import playsound


class Login_window:

     def __init__(self, root):
         self.root = root
         self.root.title(" Inventory Login")
         self.root.geometry("1350x700+0+0")
         self.root.config(bg="#021e2f")
 
 
         # ===================Frames=========================================================
         login_frame = Frame(self.root, bg="white")
         login_frame.place(x=250, y=100, width=800, height=500)
 

         title = Label(
             login_frame,
             text="LOGIN HERE",
             font=("Times New Roman", 30, "bold"),
             bg="white",
             fg="#08A3D2",
         ).place(x=250, y=50)
 

         email = Label(
             login_frame,
             text="EMAIL ADDRESS",
             font=("Times New Roman", 18, "bold"),
             bg="white",
             fg="gray",
         ).place(x=250, y=150)
         self.txt_email = Entry(
             login_frame, font=("Times New Roman", 15), bg="lightgray"
         )
         self.txt_email.place(x=250, y=180, width=350, height=35)
 

         pass_ = Label(
             login_frame,
             text="PASSWORD",
             font=("Times New Roman", 18, "bold"),
             bg="white",
             fg="gray",
         ).place(x=250, y=250)
         self.txt_pass_ = Entry(
             login_frame, font=("Times New Roman", 15), bg="lightgray"
         )
         self.txt_pass_.place(x=250, y=280, width=350, height=35)
 

         btn_reg = Button(
             login_frame,
             cursor="hand2",
             command=self.register_window,
             text="Register new Account?",
             font=("times new roman", 14),
             bg="white",
             bd=0,
             fg="#B00857",
         ).place(x=250, y=320)
 

         btn_login = Button(
             login_frame,
             text="Login",
             command=self.login,
             font=("times new roman", 20, "bold"),
             fg="white",
             bg="#B00857",
             cursor="hand2",
         ).place(x=250, y=380, width=180, height=40)
 

IMS Clock", font=("Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="#081923", bd=0)
         playsound("Login.mp3")
         # ===================Clock=========================================================
         self.lbl = Label(
             self.root,
             text="
IMS Clock",
             font=("Book Antiqua", 25, "bold"),
             fg="white",
             compound=BOTTOM,
             bg="#081923",
             bd=0,
         )
         self.lbl.place(x=90, y=120, height=450, width=350)
         self.working()
 
     def register_window(self):
         self.root.destroy()
         import inventorylogin
 
     def login(self):
         if self.txt_email.get() == "" or self.txt_pass_.get() == "":
             playsound("Nameerror.mp3")
             messagebox.showerror("Error", "All fields are required", parent=self.root)
         else:
             try:

                 con = pymysql.connect(
                     host="localhost", user="root", password="", database="employee"
                 )
                 cur = con.cursor()
                 cur.execute(
                     "select * from employee where email=%s and ***",
                     (self.txt_email.get(), self.txt_pass_.get()),
                 )
                 row = cur.fetchone()
                 print(row)

                 if row == None:
                     playsound("Nameerror.mp3")
                     messagebox.showerror(
                         "Error", "Invalid USERNAME & PASSWORD", parent=self.root
                     )
 
                 else:
 
                     messagebox.showinfo("Success", "Welcome", parent=self.root)

                     playsound("Inven.mp3")
                     self.root.destroy()
                     import Bill

                     con.close()
             except Exception as es:

                 messagebox.showerror(
                     "Error", f"Error Due to: {str(es)}", parent=self.root
                 )
 
     
 
root = Tk()
obj = Login_window(root)
 root.mainloop()
