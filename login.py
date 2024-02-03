from tkinter import* 
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from login import *
from main import *
from panel import AdminPanel
import tkinter as tk
from tkinter import ttk
import logging
from admin_features import adminfeat
import re


logging.basicConfig(filename='user_actions.log', level=logging.INFO)

class Login:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")
        self.root.attributes('-fullscreen',True)

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        # eto lumang code
        self.bg = ImageTk.PhotoImage(file=r"Images_GUI\newbg.jpg")
        
        # Create a Label with this image
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame2= Frame(self.root,bg="#6A8CC9")
        frame2.place(x=900, y=170, width=340, height=480)
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
        loginbtn=Button(frame2,command=self.login,text="LOGIN",font=("times new roman",20,"bold"),bd=0,relief=RIDGE,fg="white",bg="#3B3935",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=390,width=270,height=35)


        # Creating Button Registration
        # loginbtn=Button(frame2,command=self.reg,text="Don't have an account? Sign up.",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        # loginbtn.place(x=33,y=430,width=270,height=35)


        # Creating Button Forget
        loginbtn=Button(frame2,command=self.forget_pwd,text="Forget password?",font=("times new roman",13),bd=0,relief=RIDGE,fg="white",bg="#6A8CC9",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=350,width=120,height=25)

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
            
   


    # def open_windows1(self):
    #     self.root.withdraw()
    #     self.window1 = tk.Toplevel(self.root)
    #     self.disable_close_button(self.window1)
    #     self.app1 = Register(self.window1, self.show_main_app)

  
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
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                
                self.root2.title("Forget Password")
                self.root2.geometry("1366x768+0+0")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)
                
                

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
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ssq=%s and sa=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                self.root2.withdraw()
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
            
                self.root.withdraw()
                self.window1 = tk.Toplevel(self.root)
                self.disable_close_button(self.window1)
                self.app1 = Login(self.window1, self.show_main_app)
                

def main():
    root = tk.Tk()
    app = Login(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()



# from tkinter import* 
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# from login import Login

# class Register:
#     def __init__(self,root,show_main_app_callback):
#         self.root=root
#         self.root.title("Register")
#         self.root.geometry("1366x768+0+0")
#         self.root.attributes('-fullscreen',True)

#         # ============ Variables =================
#         self.var_fname=StringVar()
#         self.var_lname=StringVar()
#         self.var_cnum=StringVar()
#         self.var_email=StringVar()
#         self.var_ssq=StringVar()
#         self.var_sa=StringVar()
#         self.var_pwd=StringVar()
#         self.var_cpwd=StringVar()
#         self.var_check=IntVar()

#         self.bg=ImageTk.PhotoImage(file=r"Images_GUI\bgReg.jpg")
        
#         lb1_bg=Label(self.root,image=self.bg)
#         lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

#         frame= Frame(self.root,bg="#F2F2F2")
#         frame.place(x=300,y=80,width=900,height=580)
        

#         # img1=Image.open(r"Images_GUI\reg1.png")
#         # img1=img1.resize((450,100),Image.LANCZOS)
#         # self.photoimage1=ImageTk.PhotoImage(img1)
#         # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
#         # lb1img1.place(x=300,y=100, width=500,height=100)
        

#         get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
#         get_str.place(x=350,y=130)

#         #label1 
#         fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         fname.place(x=100,y=200)

#         #entry1 
#         self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
#         self.txtuser.place(x=103,y=225,width=270)


#         #label2 
#         lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         lname.place(x=100,y=270)

#         #entry2 
#         self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
#         self.txtpwd.place(x=103,y=295,width=270)

#         # ==================== section 2 -------- 2nd Columan===================

#         #label1 
#         cnum =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         cnum.place(x=530,y=200)

#         #entry1 
#         self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("times new roman",15,"bold"))
#         self.txtuser.place(x=533,y=225,width=270)


#         #label2 
#         email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         email.place(x=530,y=270)

#         #entry2 
#         self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
#         self.txtpwd.place(x=533,y=295,width=270)

#         # ========================= Section 3 --- 1 Columan=================

#         #label1 
#         ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         ssq.place(x=100,y=350)

#         #Combo Box1
#         self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
#         self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
#         self.combo_security.current(0)
#         self.combo_security.place(x=103,y=375,width=270)


#         #label2 
#         sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         sa.place(x=100,y=420)

#         #entry2 
#         self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
#         self.txtpwd.place(x=103,y=445,width=270)

#         # ========================= Section 4-----Column 2=============================

#         #label1 
#         pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         pwd.place(x=530,y=350)

#         #entry1 
#         self.txtuser=ttk.Entry(frame,show='*',textvariable=self.var_pwd,font=("times new roman",15,"bold"))
#         self.txtuser.place(x=533,y=375,width=270)


#         #label2 
#         cpwd =lb1= Label(frame, text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
#         cpwd.place(x=530,y=420)

#         #entry2 
#         self.txtpwd=ttk.Entry(frame,show='*',textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
#         self.txtpwd.place(x=533,y=445,width=270)



#         # Checkbutton
#         # checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
#         # checkbtn.place(x=100,y=480,width=270)
        
#         self.show_pwd_var = tk.BooleanVar()
#         self.show_pwd_var.set(False)
#         show_pwd_button = ttk.Checkbutton(frame, text="Show Password", variable=self.show_pwd_var, command=self.toggle_show_password,style="TCheckbutton")
#         show_pwd_button.place(x=533,y=475)
        
        
#         # self.level_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
#         # self.level_bar.place(x=533,y=495)




#         self.terms_text = (
           
# "Terms and Conditions\n"

# "1. Acceptance of Terms\n"
# "By using this software, you agree to be bound by these terms and conditions.\n"

# "2. Use of the Software\n"
# "You are granted a non-exclusive, non-transferable license to use the software for personal or commercial purposes.\n"

# "3. Restrictions\n"
# "You may not modify, adapt, reverse engineer, decompile, or disassemble the software.\n"

# "4. Intellectual Property\n"
# "All intellectual property rights in the software are owned by the developer.\n"

# "5. Warranty Disclaimer\n"
# "The software is provided without any warranty, express or implied.\n"

# "6. Limitation of Liability\n"
# "The developer shall not be liable for any direct, indirect, incidental, special, or consequential damages.\n"

# "7. Governing Law\n"
# "These terms and conditions are governed by the laws of [your jurisdiction].\n"

# "8. Changes to Terms\n"
# "The developer reserves the right to update these terms and conditions at any time.\n"

# "9. Contact Information\n"
# "For questions or concerns regarding these terms, please contact [your contact information].\n"

# )
        
#         essay_widget = Text(wrap="word", width=180, height=30,  font=("verdana", 12, "bold"), fg="black")
#         essay_widget.insert("135.5", self.terms_text)

#         self.terms_popup = tk.Toplevel(root)
#         self.terms_popup.title("Terms and Conditions")
#         self.terms_popup.withdraw()  # Hide the popup initially

#         self.terms_text_widget = tk.Text(self.terms_popup, wrap=tk.WORD, height=20, width=70, font=("verdana",13,"bold"),fg="black",highlightthickness=-1)
#         self.terms_text_widget.pack(padx=10, pady=10)
#         self.terms_text_widget.insert(tk.END, self.terms_text)

#         self.checkbtn = tk.Checkbutton(self.terms_popup, text="I agree to the terms", variable=self.var_check)
#         self.checkbtn.pack()

#         # Bind the X button (closing) to the hide_terms method
#         self.terms_popup.protocol("WM_DELETE_WINDOW", self.hide_terms)

#         self.show_button = tk.Button(frame, text="Show Terms", command=self.show_terms,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
#         self.show_button.place(x=103,y=480,width=270)

   

#         # Creating Button Register
#         loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
#         loginbtn.place(x=103,y=520,width=270,height=35)

#         # Creating Button Login
#         self.left_arrow_icon = PhotoImage(file=r"Images_GUI\left_arrow_icon.png")  # Replace with the actual path to your left arrow icon image

#         # Create login button with left arrow icon
#         # loginbtn = Button(frame, command=self.login, text="Login", image=self.left_arrow_icon,
#         #                   compound="left", font=("times new roman", 15, "bold"), bd=0, relief=RIDGE,
#         #                   fg="#fff", bg="#002B53", activeforeground="white", activebackground="#007ACC")

#         # loginbtn.place(x=50, y=50, width=100, height=100)

#         return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
#         return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)


#     def login(self):
#         self.root.withdraw()
#         self.window1 = tk.Toplevel(self.root)
#         self.disable_close_button(self.window1)
#         self.app1 = Login(self.window1, self.show_main_app)

#     def disable_close_button(self, window): 
#         window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked


#     def show_main_app(self):
#         self.root.deiconify()  # Show the main window
#         # Destroy child windows when returning to MainApp
#         if hasattr(self, 'window1'):
#             self.window1.destroy()

#     def show_terms(self):
#         self.terms_popup.deiconify()  # Show the popup
#         self.show_button.config(state=tk.DISABLED)

#     def hide_terms(self):   
#         self.terms_popup.withdraw()  # Hide the popup
#         self.show_button.config(state=tk.NORMAL)


#     def toggle_show_password(self):
#         if self.show_pwd_var.get():
#             self.txtuser.config(show='')
#             self.txtpwd.config(show='')
#             self.var_pwd.config(show='')
#         else:
#             self.txtuser.config(show='*')
#             self.txtpwd.config(show='*')
#             self.var_pwd.config(show='*')
   

#     def reg(self):
#         if (
#             self.var_fname.get() == ""
#             or self.var_lname.get() == ""
#             or self.var_cnum.get() == ""
#             or self.var_email.get() == ""
#             or self.var_ssq.get() == "Select"
#             or self.var_sa.get() == ""
#             or self.var_pwd.get() == ""
#             or self.var_cpwd.get() == ""
#         ):
#             messagebox.showerror("Error", "All Field Required!")
#         elif self.var_pwd.get() != self.var_cpwd.get():
#             messagebox.showerror("Error", "Please Enter Password & Confirm Password are Same!")
#         elif self.var_check.get() == 0:
#             messagebox.showerror("Error", "Please Check the Agree Terms and Conditions!")
#         # Check if password contains at least one uppercase letter, one special character, and has a minimum length of 8
#         if not any(char.isupper() for char in self.var_pwd.get()) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.var_pwd.get()) or len(self.var_pwd.get()) < 8:
#             messagebox.showerror("Error", "Password must be at least 8 characters long and include at least one uppercase letter and one special character")
#             return

#         # Check for phone number (cnum) format
#         if not re.match(r'^\d{11}$', self.var_cnum.get()):
#             messagebox.showerror("Error", "Phone number must be 11 digits")
#             return
        
#         if '@' not in self.var_email.get():
#             messagebox.showerror("Error", "Invalid email format, please enter a valid email")
#             return
#         try:
#             conn = mysql.connector.connect(
#                 user="root", password="", host="localhost", database="face_recognition"
#             )
#             mycursor = conn.cursor()
            
#             # Check if email already exists
#             query_email = "SELECT * FROM regteach WHERE email=%s"
#             value_email = (self.var_email.get(),)
#             mycursor.execute(query_email, value_email)
#             row_email = mycursor.fetchone()
#             if row_email is not None:
#                 messagebox.showerror("Error", "User Email exists, please try another email")
#                 return

#             # Check if first name already exists
#             query_fname = "SELECT * FROM regteach WHERE fname=%s"
#             value_fname = (self.var_fname.get(),)
#             mycursor.execute(query_fname, value_fname)
#             row_fname = mycursor.fetchone()
#             if row_fname is not None:
#                 messagebox.showerror("Error", "User with this first name already exists")
#                 return

#             # Check if password is at least 8 characters long
#             if len(self.var_pwd.get()) < 8:
#                 messagebox.showerror("Error", "Password must be at least 8 characters long")
#                 return

#             # Check for phone number (cnum) format
#             if not re.match(r'^\d{11}$', self.var_cnum.get()):
#                 messagebox.showerror("Error", "Phone number must be 11 digits")
#                 return
                    
#             password_strength = self.check_password_strength(self.var_pwd.get())       
#             if password_strength == "weak":
#                 messagebox.showerror("Error", "Weak Password. Please choose a stronger password.")
#                 return
#             elif password_strength == "medium":
#                 messagebox.showwarning("Warning", "Medium Password. Consider choosing a stronger password.")
                
#             # Registration successful
#             insert_query = "INSERT INTO regteach (fname, lname, cnum, email, ssq, sa, pwd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             insert_values = (
#                 self.var_fname.get(),
#                 self.var_lname.get(),
#                 self.var_cnum.get(),
#                 self.var_email.get(),
#                 self.var_ssq.get(),
#                 self.var_sa.get(),
#                 self.var_pwd.get(),
#             )

#             mycursor.execute(insert_query, insert_values)

#             open_min = messagebox.askyesno("Yes or No", "Registration successful. Please Login")

#             if open_min > 0:
#                 self.root.withdraw()
#                 self.window1 = tk.Toplevel(self.root)
#                 self.disable_close_button(self.window1)
#                 self.app1 = Login(self.window1, self.show_main_app)
#             else:
#                 if not open_min:
#                     return
#             conn.commit()
#             conn.close()

#         except Exception as es:
#             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            
#     def check_password_strength(self, password):
#         password = self.var_pwd.get()
#         # Check if password contains at least one uppercase letter, one special character, and has a minimum length of 8
#         has_uppercase = any(char.isupper() for char in password)
#         has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
#         is_length_valid = len(password) >= 8

#         if has_uppercase and has_special_char and is_length_valid:
#             return "strong"
#         elif has_uppercase or has_special_char or is_length_valid:
#             return "medium"
#         else:
#             return "weak"
        
#         self.display_strength(strength)

#     def display_strength(self, strength):
#         if strength == "strong":
#             self.level_bar["value"] = 100
#         elif strength == "medium":
#             self.level_bar["value"] = 50
#         else:
#             self.level_bar["value"] = 0

#         self.root.update_idletasks()

#     def return_to_main_app(self):
#         self.master.withdraw()  # Hide the child window
#         if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
#             self.show_main_app_callback()  # Call the callback to show MainApp

def main():
    root = tk.Tk()
    app = Login(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()

