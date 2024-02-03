from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from login import *
from panel import AdminPanel



class Adminlogin:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")
        self.root.attributes('-fullscreen',True)

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()


        self.bg=ImageTk.PhotoImage(file=r"Images_GUI\adminpanel.jpg")        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)


        # frame2= Frame(self.root,bg="#002B53")
        # frame2.place(x=260,y=170,width=340,height=450)

        # img1=Image.open(r"Images_GUI\log1.png")
        # img1=img1.resize((100,100),Image.LANCZOS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        # lb1img1.place(x=690,y=175, width=100,height=100)

      
        return_button = tk.Button(self.root, text="Return to Login Panel", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)

        # admin login frame2
        frame2= Frame(self.root,bg="#6A8CC9")
        frame2.place(x=600,y=280,width=340,height=400)

        # img1=Image.open(r"Images_GUI\log1.png")
        # img1=img1.resize((100,100),Image.LANCZOS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        # lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame2,text="ADMIN",font=("times new roman",30,"bold"),fg="white",bg="#6A8CC9")
        get_str.place(x=95,y=50)

        #label1 
        username =lb1= Label(frame2,text="Username:",font=("times new roman",20,"bold"),fg="white",bg="#6A8CC9")
        username.place(x=30,y=140)

        #entry1 
        self.admintxtuser=ttk.Entry(frame2,font=("times new roman",20,"bold"))
        self.admintxtuser.place(x=33,y=180,width=270)


        #label2 
        pwd =lb1= Label(frame2,text="Password:",font=("times new roman",20,"bold"),fg="white",bg="#6A8CC9")
        pwd.place(x=30,y=230)

        #entry2 
        self.admintxtpwd=ttk.Entry(frame2, show='*',font=("times new roman",20,"bold"))
        self.admintxtpwd.place(x=33,y=270,width=270)


        # Creating Button Login
        adminloginbtn=Button(frame2,command=self.adminlogin,text="LOGIN",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="white",bg="#244194",activeforeground="white",activebackground="#007ACC")
        adminloginbtn.place(x=33,y=330,width=270,height=45)


        # Creating Button Registration
        # loginbtn=Button(frame2,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        # loginbtn=Button(frame2,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=50,y=370,width=50,height=20)


    def open_windows1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = AdminPanel(self.window1, self.show_main_app)

    # def open_window2(self):
    #     self.root.withdraw()
    #     self.window2 = tk.Toplevel(self.root)
    #     self.disable_close_button(self.window2)
    #     self.app2 = AdminLogin(self.window2, self.show_main_app)
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
    #     if hasattr(self, 'window2'):
    #         self.window2.destroy()

    #  THis function is for open register window

    # login function for admin
    def adminlogin(self):
        if (self.admintxtuser.get()=="" or self.admintxtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.admintxtuser.get()=="admin" and self.admintxtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
    
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            mycursor.execute("select * from admin where email=%s and pwd=%s",(
                self.admintxtuser.get(),
                self.admintxtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("Yes or No","Access only Admin")
                if open_min>0:
                   self.root.withdraw()
                   self.window1 = tk.Toplevel(self.root)
                   self.disable_close_button(self.window1)
                   self.app1 = AdminPanel(self.window1, self.show_main_app)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

# =====================Forget window=========================================
    





def main():
    root = tk.Tk()
    app = Adminlogin(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()

