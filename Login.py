from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from tkinter import messagebox
from playsound import playsound
import pymysql
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("                                                                                                                                                                       Inventory Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        # ===================Background Colours=========================================================
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0, relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # ===================Frames=========================================================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("Times New Roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("Times New Roman", 18, "bold"), bg="white",fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame,font=("Times New Roman", 15),bg="lightgray")
        self.txt_email.place(x=250, y=180,width=350,height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("Times New Roman", 18, "bold"), bg="white",fg="gray").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("Times New Roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)

        btn_login = Button(login_frame, text="Login",command=self.login, font=("times new roman", 20,"bold"), fg="white", bg="#B00857",cursor="hand2").place(x=250, y=380,width=180,height=40)

        btn_Adminlogin=Button(login_frame, text="Admin Login",command=self.adminlogin, font=("times new roman", 20,"bold"), fg="white", bg="#B00857",cursor="hand2").place(x=440, y=380,width=180,height=40)
        playsound('Login.mp3')
        #===================Clock=========================================================
        self.lbl=Label(self.root,text="\nIMS Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120, height=450,width=350)
        self.working()

    def register_window(self):
        self.root.destroy()
        import inventorylogin


    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            playsound('Nameerror.mp3')
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                    playsound('Nameerror.mp3')
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)

                else:

                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    playsound('Inven.mp3')
                    self.root.destroy()
                    import Bill
                    con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

    def adminlogin(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="admin")
                cur=con.cursor()
                cur.execute("select * from admin where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)

                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    import Bill
                    con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)


    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #=====================For clock image
        bg=Image.open("C:/Users/DELL/Desktop/images/cl5.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #formula to rotate the anticlock
        #angle_in_radians = angle_in_degree * math.pi/180
        #line length=100
        #center_x=100
        #center_y=100
        # end_x=center_x + line_length * math.cos(angle_in_radians)
        # end_y=center_y - line_length * math.sin(angle_in_radians)

        #==========Hour  line image========
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        # ==========Minute   line image========
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="black",width=3)
        # ==========Second  line image========
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("C:/Users/DELL/Desktop/images/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="C:/Users/DELL/Desktop/images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)





root= Tk()
obj= Login_window(root)
root.mainloop()
