from tkinter import *
from PIL import Image, ImageTk
import math,random
import os
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
from validate_email import validate_email
import qrcode
from playsound import playsound
import cv2
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")

        self.root.title("                                                                                                                                                                                     Smart Inventory Control System")
        bg_color="#031F3C"
        title=Label(self.root,text="Smart Inventory Management System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman ",30,"bold"),pady=2).pack(fill=X)
        playsound('purchase.mp3')
        #===========================================variables======================================
        #======================================Cosmetics===============================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        # ======================================Grocery===============================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        # ======================================Cold drink===============================
        self.maza=IntVar()
        self.cock=IntVar()
        self.thumbsup=IntVar()
        self.frooti=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        # ======================================Total Product Price & Tax Variable===============================
        self.cosmetic_price=StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ===========================================Customer========================
        self.c_name=StringVar()
        self.c_mail=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




        #===========================================Customer Detail Frame==================================

        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)


        def customer(cus):
            if cus.isalpha():
                return True
            elif cus is "":
                return True

            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error","Kindly enter character only, Invalid Input")
                return False
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        self.cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN)
        self.cname_txt.grid(row=0,column=1,pady=5,padx=10)
        reg = root.register(customer)
        self.cname_txt.config(validate="key", validatecommand=(reg, '%P'))

        def mail(self):
            valid=self.c_mail.get()
           is_valid = validate_email(valid)
           print(is_valid)
        cphn_lbl = Label(F1, text="Email", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        self.c_mail_txt = Entry(F1, width=20,textvariable=self.c_mail, font="arial 15", bd=7, relief=SUNKEN)
        self.c_mail_txt.grid(row=0, column=3, pady=5, padx=10)
        reg = root.register(mail)
        self.c_mail_txt.config(validate="key", validatecommand=(reg, '%P'))


        def Bill(Bi):
            if Bi.isdigit():
                return True
            elif Bi is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        self.c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN)
        self.c_bill_txt.grid(row=0, column=5, pady=5, padx=10)
        reg = root.register(Bill)
        self.c_bill_txt.config(validate="key", validatecommand=(reg, '%P'))


        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

        #=============================================Cosmetics Frame=================================
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=330,height=380)

        def bath(ba):
            if ba.isdigit():
                return True
            elif ba is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error","Kindly enter integer only, Invalid Input")
                return False

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        self.bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        self.bath_txt.grid(row=0,column=1,padx=10,pady=10)
        reg = root.register(bath)
        self.bath_txt.config(validate="key", validatecommand=(reg, '%P'))

        def f_cream(face):
            if face.isdigit():
                return True
            elif face is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error","Kindly enter integer only, Invalid Input")
                return False

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.Face_cream_txt.grid(row=1, column=1,padx=10, pady=10)
        reg = root.register(f_cream)
        self.Face_cream_txt.config(validate="key", validatecommand=(reg, '%P'))

        def f_wash(wash):
            if wash.isdigit():
                return True
            elif wash is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error","Kindly enter integer only, Invalid Input")
                return False
        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.Face_w_txt.grid(row=2, column=1,padx=10, pady=10)
        reg = root.register(f_wash)
        self.Face_w_txt.config(validate="key", validatecommand=(reg, '%P'))

        def hair_spray(spray):
            if spray.isdigit():
                return True
            elif spray is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.Hair_s_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.Hair_s_txt.grid(row=3, column=1,padx=10, pady=10)
        reg = root.register(hair_spray)
        self.Hair_s_txt.config(validate="key", validatecommand=(reg, '%P'))

        def hair_gel(gel):
            if gel.isdigit():
                return True
            elif gel is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.Hair_g_txt = Entry(F2, width=10,textvariable=self.gell, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.Hair_g_txt.grid(row=4, column=1,padx=10, pady=10)
        reg = root.register(hair_gel)
        self.Hair_g_txt.config(validate="key", validatecommand=(reg, '%P'))

        def body_lotion(lotion):
            if lotion.isdigit():
                return True
            elif lotion is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.body_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.body_txt.grid(row=5, column=1,padx=10, pady=10)
        reg = root.register(body_lotion)
        self.body_txt.config(validate="key", validatecommand=(reg, '%P'))


        # =============================================Grocery Frame=================================
        F3 = LabelFrame(self.root, text="Grocery", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=330, height=380)

        def Rice(Ri):
            if Ri.isdigit():
                return True
            elif Ri is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.g1_txt = Entry(F3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g1_txt.grid(row=0, column=1,padx=10, pady=10)
        reg = root.register(Rice)
        self.g1_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Food_Oil(Oil):
            if Oil.isdigit():
                return True
            elif Oil is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False

        g2_lbl = Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.g2_txt = Entry(F3, width=10,textvariable=self.food_oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g2_txt.grid(row=1,column=1, padx=10,pady=10)
        reg = root.register(Food_Oil)
        self.g2_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Pulse(Pu):
            if Pu.isdigit():
                return True
            elif Pu is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        g3_lbl = Label(F3, text="Pulse", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.g3_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g3_txt.grid(row=2,column=1,padx=10,pady=10)
        reg = root.register(Pulse)
        self.g3_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Wheat(Wh):
            if Wh.isdigit():
                return True
            elif Wh is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.g4_txt = Entry(F3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g4_txt.grid(row=3,column=1,padx=10,pady=10)
        reg = root.register(Wheat)
        self.g4_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Sugar(Su):
            if Su.isdigit():
                return True
            elif Su is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.g5_txt = Entry(F3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g5_txt.grid(row=4,column=1, padx=10,pady=10)
        reg = root.register(Sugar)
        self.g5_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Tea(Te):
            if Te.isdigit():
                return True
            elif Te is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.g6_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g6_txt.grid(row=5, column=1,padx=10, pady=10)
        reg = root.register(Tea)
        self.g6_txt.config(validate="key", validatecommand=(reg, '%P'))


        # =============================================Cold Drink Frame=================================
        F4 = LabelFrame(self.root, text="Cold Drink", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F4.place(x=675, y=180, width=330, height=380)

        def Maaza(Ma):
            if Ma.isdigit():
                return True
            elif Ma is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False

        c1_lbl = Label(F4, text="Maaza", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.c1_txt = Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c1_txt.grid(row=0, column=1,padx=10, pady=10)
        reg = root.register(Maaza)
        self.c1_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Cock(Co):
            if Co.isdigit():
                return True
            elif Co is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c2_lbl = Label(F4, text="Coke", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.c2_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c2_txt.grid(row=1,column=1,padx=10,pady=10)
        reg = root.register(Cock)
        self.c2_txt.config(validate="key", validatecommand=(reg, '%P'))

        def Frooti(Fr):
            if Fr.isdigit():
                return True
            elif Fr is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.c3_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c3_txt.grid(row=2,column=1, padx=10,pady=10)
        reg = root.register(Frooti)
        self.c3_txt.config(validate="key", validatecommand=(reg, '%P'))


        def Thumbs_Up(Thu):
            if Thu.isdigit():
                return True
            elif Thu is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c4_lbl = Label(F4, text="Thumbs Up", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.c4_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c4_txt.grid(row=3,column=1,padx=10,pady=10)
        reg = root.register(Thumbs_Up)
        self.c4_txt.config(validate="key", validatecommand=(reg, '%P'))


        def Limca(Li):
            if Li.isdigit():
                return True
            elif Li is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.c5_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c5_txt.grid(row=4,column=1,padx=10,pady=10)
        reg = root.register(Limca)
        self.c5_txt.config(validate="key", validatecommand=(reg, '%P'))


        def Sprite(Sp):
            if Sp.isdigit():
                return True
            elif Sp is "":
                return True
            else:
                playsound('NameError.mp3')
                messagebox.showerror("Error", "Kindly enter integer only, Invalid Input")
                return False
        c6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"), bg=bg_color,fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.c6_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.c6_txt.grid(row=5, column=1,padx=10, pady=10)
        reg = root.register(Sprite)
        self.c6_txt.config(validate="key", validatecommand=(reg, '%P'))

        #=================================Bill Area===================================================

        F5 = Frame(self.root,bd=10,relief=GROOVE )
        F5.place(x=1010, y=180, width=340, height=380)
        bill_title=Label(F5,text="Bill",font=("Arial 15 bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # =================================Button Frame==================================================
        F6=LabelFrame(self.root, text="Bill Menu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=240)


        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        self.m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN)
        self.m1_txt.grid(row=0,column=1,padx=10,pady=10)




        m2_lbl = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        self.m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_price, bd=7, relief=SUNKEN)
        self.m2_txt.grid(row=1, column=1, padx=10, pady=10)



        m3_lbl = Label(F6, text="Total Cold Drinks Price", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        self.m3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_price, bd=7, relief=SUNKEN)
        self.m3_txt.grid(row=2, column=1, padx=10, pady=10)



        cm1_lbl = Label(F6, text=" Cosmetic Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        self.cm1_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=7, relief=SUNKEN)
        self.cm1_txt.grid(row=0, column=3, padx=10, pady=1)



        cm2_lbl = Label(F6, text=" Grocery Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        cm2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.grocery_tax, bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        cm3_lbl = Label(F6, text=" Cold Drinks Tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        cm3_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=840,width=650,height=150)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="Cadetblue",fg="white",bd=5,pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill",command=self.bill_area, bg="Cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear",command=self.clear_data, bg="Cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit",command=self.Exit_app, bg="Cadetblue", fg="white", bd=5, pady=15, width=11,font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()
    def total(self):
        self.c_s_p=(self.soap.get()*40)
        self.c_fc_p=(self.face_cream.get()*120)
        self.c_fw_p=(self.face_wash.get()*60)
        self.c_hs_p=(self.spray.get()*180)
        self.c_hg_p=(self.gell.get()*140)
        self.c_bl_p=(self.lotion.get()*180)
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=(self.rice.get()*80)
        self.g_f_p= (self.food_oil.get()*120)
        self.g_d_p=(self.daal.get()*60)
        self.g_w_p=(self.wheat.get()*240)
        self.g_s_p=(self.sugar.get()*45)
        self.g_t_p=(self.tea.get()*150)
        self.total_grocery_price = float(
                                           self.g_r_p+
                                           self.g_f_p+
                                           self.g_d_p+
                                           self.g_w_p+
                                           self.g_s_p+
                                           self.g_t_p
                                         )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.d_m_p=(self.maza.get()*60)
        self.d_c_p=(self.cock.get()*60)
        self.d_f_p=(self.frooti.get()*50)
        self.d_t_p=(self.thumbsup.get()*45)
        self.d_l_p=(self.limca.get()*40)
        self.d_s_p=(self.sprite.get()*60)
        self.total_drinks_price = float(
                                          self.d_m_p+
                                          self.d_c_p+
                                          self.d_f_p+
                                          self.d_t_p+
                                          self.d_l_p+
                                          self.d_s_p
                                        )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price * 0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                             )

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome IMS Retail\n")
        self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_mail.get()}")
        self.textarea.insert(END, f"\n=====================================")
        self.textarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
        self.textarea.insert(END, f"\n=====================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_mail.get()=="":
           messagebox.showerror("Error","Customer details are must ")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
             messagebox.showerror("Error", "No Product Purchased ")
        else:

          self.welcome_bill()
          #===========Cosmetics=================
          if self.soap.get()!=0:
            self.textarea.insert(END, f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

          if self.face_cream.get()!=0:
            self.textarea.insert(END, f"\n Face Cream \t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

          if self.face_wash.get()!=0:
            self.textarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

          if self.spray.get()!=0:
            self.textarea.insert(END, f"\n Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")

          if self.gell.get()!=0:
            self.textarea.insert(END, f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")

          if self.lotion.get()!=0:
            self.textarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

          # ===========Grocery=================
          if self.rice.get() != 0:
            self.textarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

          if self.food_oil.get() != 0:
            self.textarea.insert(END, f"\n Food Oil \t\t{self.food_oil.get()}\t\t{self.g_f_p}")

          if self.daal.get() != 0:
            self.textarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

          if self.wheat.get() != 0:
            self.textarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

          if self.sugar.get() != 0:
            self.textarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

          if self.tea.get() != 0:
            self.textarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

           # ===========Cold Drinks=================
          if self.maza.get() != 0:
            self.textarea.insert(END, f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")

          if self.cock.get() != 0:
            self.textarea.insert(END, f"\n Cock \t\t{self.cock.get()}\t\t{self.d_c_p}")

          if self.frooti.get() != 0:
            self.textarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

          if self.thumbsup.get() != 0:
            self.textarea.insert(END, f"\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")

          if self.limca.get() != 0:
            self.textarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

          if self.sprite.get() != 0:
            self.textarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

          self.textarea.insert(END, f"\n-------------------------------------")
          if self.cosmetic_tax.get()!="Rs. 0.0":
            self.textarea.insert(END, f"\nCosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

          if self.grocery_tax.get()!="Rs. 0.0":
            self.textarea.insert(END, f"\nGrocery Tax\t\t\t{self.grocery_tax.get()}")

          if self.cold_drink_tax.get()!="Rs. 0.0":
            self.textarea.insert(END, f"\nCold Drink Tax\t\t\t{self.cold_drink_tax.get()}")

          self.textarea.insert(END, f"\nTotal Bill : \t\t\t Rs. {self.Total_bill}")
          self.textarea.insert(END, f"\n-------------------------------------")
          self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
          self.bill_data=self.textarea.get('1.0',END)
          f1=open("bill/" +str(self.bill_no.get())+".txt","w")
          f1.write(self.bill_data)
          f1.close()
          messagebox.showinfo("Saved",f"Bill No.:{self.bill_no.get()} saved Successfully")
          messagebox.showinfo("Send Mail",f"Bill No.:{self.bill_no.get()}?")
          self.e_mail()
          messagebox.showinfo("Sent", f"Bill No.:{self.bill_no.get()} sent Successfully")
          messagebox.showinfo("Scan","Kindly Scan Qr code displayed")
          self.Qrcode_bill()


        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.search_bill.get():
                 f1=open(f"bill/{i}","r")
                 self.textarea.delete('1.0',END)
                 for d in f1:
                   self.textarea.insert(END,d)
                 f1.close()
                 present="yes"
        if present=="no":
            playsound('NameError.mp3')
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op < 0:


         # ======================================Cosmetics===============================
          self.soap.set(0)
          self.face_cream.set(0)
          self.face_wash.set(0)
          self.spray.set(0)
          self.gell.set(0)
          self.lotion.set(0)
         # ======================================Grocery===============================
          self.rice.set(0)
          self.food_oil.set(0)
          self.daal.set(0)
          self.wheat.set(0)
          self.sugar.set(0)
          self.tea.set(0)
         # ======================================Cold drink===============================
          self.maza.set(0)
          self.cock.set(0)
          self.thumbsup.set(0)
          self.frooti.set(0)
          self.limca.set(0)
          self.sprite.set(0)
         # ======================================Total Product Price & Tax Variable===============================
          self.cosmetic_price.set("")
          self.grocery_price.set("")
          self.cold_drink_price.set("")

          self.cosmetic_tax.set("")
          self.grocery_tax.set("")
          self.cold_drink_tax.set("")

          # ===========================================Customer========================
          self.c_name .set("")
          self.c_mail .set("")

          self.bill_no.set("")
          x = random.randint(1000, 9999)
          self.bill_no.set(str(x))
          self.search_bill.set("")
          self.welcome_bill()

    def e_mail(self):
        email_user = 'svyas_me20@thapar.edu'
        email_send = self.c_mail.get()
        subject = 'IMS !'
        msg = MIMEMultipart()
        msg['from'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = 'Hi there I am sending this email from Smart Inventory Control System!'
        msg.attach(MIMEText(body, 'plain'))

        filename = ("bill/" + str(self.bill_no.get()) + ".txt")
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment;filename= " + filename)

        msg.attach(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, 'vyas@123')

        server.sendmail(email_user, email_send, text)
        server.quit()

    def Qrcode_bill(self):
        img = qrcode.make('https://rzp.io/l/MIr2hiBbC')
        img.save('myQR.png')
        img = cv2.QRCodeDetector()
        val, points, straight_qrcode = img.detectAndDecode(cv2.imread('myQR.png'))
        img = cv2.imread('myQR.png')
        cv2.imshow("kindly scan the QrCode",img)



    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
           root.destroy()

root=Tk()
obj=Bill_App(root)
root.mainloop()
