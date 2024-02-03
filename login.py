from tkinter import* 
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from panel import AdminPanel
import tkinter as tk
from tkinter import ttk
import logging
from admin_features import adminfeat
import re
from main import MainApp

logging.basicConfig(filename='user_actions.log', level=logging.INFO)

class Login:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")
        self.root.attributes('-fullscreen',True)

        # variables 
        self.var_ID=tk.StringVar()
        self.var_pwd=StringVar()

        bg_img = Image.open("Images_GUI/login.jpg")
        self.bg = ImageTk.PhotoImage(bg_img.resize((1550,870)))

        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame2= Frame(self.root,bg="#6A8CC9")
        frame2.place(x=949, y=165, width=340, height=480)
        # hanggang dito

        # img1=Image.open(r"Images_GUI\log1.png")
        # img1=img1.resize((100,100),Image.LANCZOS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        # lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame2,text="LOGIN",font=("times new roman",40,"bold"),fg="white",bg="#6A8CC9")
        get_str.place(x=40,y=35)

        #label1 
        username =lb1= Label(frame2,text="Email:",font=("times new roman",20),fg="white",bg="#6A8CC9")
        username.place(x=30,y=150)

        #entry1 
        self.txtuser=ttk.Entry(frame2,font=("times new roman",20))
        self.txtuser.place(x=33,y=185,width=270)


        #label2 
        pwd =lb1= Label(frame2,text="Password:",font=("times new roman",20),fg="white",bg="#6A8CC9")
        pwd.place(x=30,y=250)

        #entry2 
        self.txtpwd=ttk.Entry(frame2, show='*',font=("times new roman",20))
        self.txtpwd.place(x=33,y=285,width=270)
        
        self.show_pwd_var = tk.BooleanVar()
        style = ttk.Style()
        style.configure("TCheckbutton", background="#6A8CC9")  # Replace "your_background_color" with the color you want
        self.show_pwd_var.set(False)
        show_pwd_button1 = ttk.Checkbutton(frame2, text="Show Password", variable=self.show_pwd_var, command=self.toggle_show_password, style="TCheckbutton")
        show_pwd_button1.place(x=33,y=325)
        


        # Creating Button Login
        loginbtn=Button(frame2,command=self.login,text="LOGIN",font=("times new roman",20,"bold"),bd=0,relief=RIDGE,fg="white",bg="#244194",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=350,width=270,height=40)


        # Creating Button Registration
        # loginbtn=Button(frame2,command=self.reg,text="Don't have an account? Sign up.",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=33,y=430,width=270,height=35)


        # Creating Button Forget
        loginbtn=Button(frame2,command=self.forget_pwd,text="Forget password?",font=("times new roman",13),bd=0,relief=RIDGE,fg="white",bg="#6A8CC9",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=400,width=120,height=25)

        return_button = Button(self.root, text="QUIT", command=self.open_window10, font=("arial",12,"bold"),fg="white", bg="#002B53")
        return_button.grid(row=0,column=1,padx=1455,pady=820,sticky=E)


        # Creating Button Registration
        # loginbtn=Button(frame2,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=33,y=370,width=50,height=20)


        # # Creating Button Forget
        # loginbtn=Button(frame2,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=50,y=370,width=50,height=20)

    def toggle_show_password(self):
        if self.show_pwd_var.get():
          
            self.txtpwd.config(show='')
            
        else:
            
            self.txtpwd.config(show='*')


    def open_window10(self):
        self.root.withdraw()
        self.window10 = tk.Toplevel(self.root)
        self.disable_close_button(self.window10)
        self.app10 = (self.window10, self.show_main_app)
        self.root.destroy()
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked


    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def return_to_main_app(self):
        self.root.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp


    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window10'):
            self.window10.destroy()

    #  THis function is for open register window

    

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin@balii.edu.ph" and self.txtpwd.get()=="admin123"):
            if self.txtuser.get()!="admin@balii.edu.ph" and self.txtpwd.get()!="admin123":
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("Yes or No","Access only Admin")
                if open_min>0:
                   self.root.withdraw()
                   self.window1 = tk.Toplevel(self.root)
                   self.disable_close_button(self.window1)
                   self.app1 = adminfeat(self.window1, self.show_main_app)
                   messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
    
    
        else:
            try:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM regteach WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpwd.get()))
                row = mycursor.fetchone()

                if row is not None:
                    open_min = messagebox.askyesno("Yes or No", "Access only Teachers")
                    if open_min:
                        # If Yes was clicked, then proceed to Main App
                        self.root.withdraw()
                        self.window1 = tk.Toplevel(self.root)
                        self.disable_close_button(self.window1)

                        # Instantiate MainApp
                        self.app1 = MainApp(self.window1, self.show_main_app)
                        logging.info(f"User Login: {self.txtuser.get()}")
                        
                    else:
                        # If No was clicked, then just return
                        conn.commit()
                        conn.close()
                        logging.info("User decided not to proceed to MainApp.")
                else:
                    logging.warning("Invalid login attempt detected.")
                    messagebox.showerror("Error", "Please Check Username or Password !")

            except mysql.connector.Error as e:
                logging.error("Failed to connect to MySQL database: {}".format(e))
                print(f"Error: {e}")
                messagebox.showerror("Error", "An error occurred during login.")

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

# =====================Forget window=========================================
    
 
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            self.root.withdraw()
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()

            if row is None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                employee_id = row[1]  # replace id_index with the index of ID in your row
                conn.close()
                self.root2=Toplevel()
                
                self.root2.title("Forget Password")
                self.root2.geometry("1366x768+0+0")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                employeeID =lb1= Label(self.root2,text="Enter your ID:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                employeeID.place(x=70,y=80)

                self.txtID=ttk.Entry(self.root2,textvariable=self.var_ID,font=("times new roman",15,"bold"))
                self.txtID.place(x=70,y=150,width=270)
                
        
                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)
                
               
        


#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ID.get()=="Select":
            messagebox.showerror("Error","Enter your ID!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                query=("select * from regteach where employee_id=%s")
                value=(self.var_ID.get(), )
                mycursor.execute(query,value)
                row = mycursor.fetchone()

                if mycursor.with_rows:
                    mycursor.fetchall()  # Read all remaining rows to clear the previous query result

            except mysql.connector.Error as err:
                print(f"Error: {err}")
                conn.rollback()
            else:
                if row==None:
                    messagebox.showerror("Error","Invalid ID!",parent=self.root2)
                else:
                    try:
                        query=("update regteach set password=%s where employee_id=%s")
                        value=(self.var_pwd.get(), self.var_ID.get())
                        mycursor.execute(query,value)
                        conn.commit()
                        messagebox.showinfo("Info","Successfully Your password has been reset, Please login with new Password!",parent=self.root2)

                        self.root2.withdraw()
                        self.window1 = tk.Toplevel(self.root2)
                        self.login = Login(self.window1, self.show_main_app)
                    except mysql.connector.Error as err:
                        print(f"Error: {err}")
                        conn.rollback()
                    finally:
                        conn.close()
                    
def main():
    root = tk.Tk()
    app = Login(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()

