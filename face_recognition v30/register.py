# from tkinter import* 
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import tkinter as tk   
# import mysql.connector
# from login import *
# from tkinter import* 
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector

# class Register:
#     def __init__(self,root,show_main_app_callback):
#         self.root=root
#         self.root.title("Register")
#         self.root.geometry("1366x768+0+0")

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
#         frame.place(x=200,y=80,width=900,height=580)
        

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
#         loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
#         loginbtn.place(x=533,y=520,width=270,height=35)

#         return_button = tk.Button(self.root, text="Login", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
#         return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)

#     # def login(self):
#     #     self.root.withdraw()
#     #     self.new_window=Toplevel(self.root)
#     #     self.app=Login(self.new_window)
        

#     def show_terms(self):
#         self.terms_popup.deiconify()  # Show the popup
#         self.show_button.config(state=tk.DISABLED)

#     def hide_terms(self):   
#         self.terms_popup.withdraw()  # Hide the popup
#         self.show_button.config(state=tk.NORMAL)


#     def return_to_main_app(self):
#         self.root.withdraw()  # Hide the child window
#         if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
#             self.show_main_app_callback()  # Call the callback to show MainApp

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
#         else:
#             messagebox.showinfo("Successfully", "Successfully Register!")
#             try:
#                 conn = mysql.connector.connect(
#                     user="root", password="", host="localhost", database="face_recognition"
#                 )
#                 mycursor = conn.cursor()
#                 query = "SELECT * FROM regteach WHERE email=%s"
#                 value = (self.var_email.get(),)
#                 mycursor.execute(query, value)
#                 row = mycursor.fetchone()
#                 if row is not None:
#                     messagebox.showerror("Error", "User already exists, please try another email")
#                 else:
#                     insert_query = "INSERT INTO regteach (fname, lname, cnum, email, ssq, sa, pwd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#                     insert_values = (
#                         self.var_fname.get(),
#                         self.var_lname.get(),
#                         self.var_cnum.get(),
#                         self.var_email.get(),
#                         self.var_ssq.get(),
#                         self.var_sa.get(),
#                         self.var_pwd.get(),
#                     )

#                     mycursor.execute(insert_query, insert_values)

#                     open_min = messagebox.askyesno("Yes or No", "Please Login")

#                     if open_min > 0:
#                         self.new_window = Toplevel(self.root)
#                         self.app = Login(self.return_to_main_app)
#                         self.root.withdraw()
#                     else:
#                         if not open_min:
#                             return
#                     conn.commit()
#                     conn.close()

#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




# def main():
#     root = tk.Tk()
#     app = Register(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()