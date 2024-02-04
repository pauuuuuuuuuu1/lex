from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
# from login import Login
import tkinter as tk
import re

class Register:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")
        self.root.attributes('-fullscreen',True)
        

        # ============ Variables =================
        self.var_employee_id = StringVar()
        self.var_fname=StringVar()
        self.var_mname = StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_gender=StringVar()
        self.var_department = StringVar()
        self.var_email=StringVar() 
        self.var_password=StringVar()
        self.var_check=IntVar()

        bg1=Image.open(r"Images_GUI\regcover.png")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        frame= Frame(self.root,bg="lightgray")
        frame.place(x=510,y=230,width=600,height=500)

        # employee ID
        employee_label =lb1= Label(frame,text="Employee ID:",font=("Arial",15,"bold"),fg="#002B53",bg="lightgray")
        employee_label.place(x=20,y=50)

        self.employee_entry=ttk.Entry(frame,textvariable=self.var_employee_id,font=("Arial",15))
        self.employee_entry.place(x=165,y=46,width=200,height=35)
        
        # first name
        fname =lb1= Label(frame,text="First Name:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        fname.place(x=20,y=130)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",12))
        self.txtuser.place(x=20,y=165,width=210,height=35)
        
        # middle name
        mname =lb1= Label(frame,text="M.I.",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        mname.place(x=240,y=130)

        self.txtmiddlename=ttk.Entry(frame,textvariable=self.var_mname,font=("arial",15,"bold"))
        self.txtmiddlename.place(x=240,y=165,width=120,height=35)

        # last name
        lname =lb1= Label(frame,text="Last Name:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        lname.place(x=370,y=130)

        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15,"bold"))
        self.txtpwd.place(x=370,y=165,width=210,height=35)

        # contact no.
        cnum =lb1= Label(frame,text="Contact No.:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        cnum.place(x=20,y=220)

        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("arial",15,"bold"))
        self.txtuser.place(x=150,y=215,width=160,height=35)

        # gender
        gender =lb1= Label(frame,text="Gender:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        gender.place(x=320,y=220)

        self.gender_entry = ttk.Combobox(frame, textvariable=self.var_gender, font=("arial", 15), state="readonly")
        self.gender_entry["values"] = ("Male", "Female")
        self.gender_entry.place(x=410,y=215,width=165,height=35)

        # email
        email =lb1= Label(frame,text="Email:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        email.place(x=20,y=285)

        self.txtemail=ttk.Entry(frame,textvariable=self.var_email,font=("arial",12))
        self.txtemail.place(x=85,y=280,width=215,height=35)

        # department
        dep_label =lb1= Label(frame,text="Department:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        dep_label.place(x=310,y=285)

        self.dep_entry = ttk.Combobox(frame, textvariable=self.var_department, font=("arial", 15), state="readonly")
        self.dep_entry["values"] = ("Kinder", "Elementary", "High School")
        self.dep_entry.place(x=435,y=280,width=140,height=35)

        # default password
        password =lb1= Label(frame,text="Default Password:",font=("arial",15,"bold"),fg="#002B53",bg="lightgray")
        password.place(x=20,y=350)

        self.txtpassword=ttk.Entry(frame,textvariable=self.var_password,font=("arial",15))
        self.txtpassword.place(x=210,y=345,width=225,height=35)

        self.terms_text = (            
            "Terms and Conditions\n"

            "1. Acceptance of Terms\n"
            "By using this software, you agree to be bound by these terms and conditions.\n"

            "2. Use of the Software\n"
            "You are granted a non-exclusive, non-transferable license to use the software for personal or commercial purposes.\n"

            "3. Restrictions\n"
            "You may not modify, adapt, reverse engineer, decompile, or disassemble the software.\n"

            "4. Intellectual Property\n"
            "All intellectual property rights in the software are owned by the developer.\n"

            "5. Warranty Disclaimer\n"
            "The software is provided without any warranty, express or implied.\n"

            "6. Limitation of Liability\n"
            "The developer shall not be liable for any direct, indirect, incidental, special, or consequential damages.\n"

            "7. Governing Law\n"
            "These terms and conditions are governed by the laws of [your jurisdiction].\n"

            "8. Changes to Terms\n"
            "The developer reserves the right to update these terms and conditions at any time.\n"

            "9. Contact Information\n"
            "For questions or concerns regarding these terms, please contact [your contact information].\n"

        )
        
        essay_widget = Text(wrap="word", width=180, height=30,  font=("arial", 15), fg="black")
        essay_widget.insert("135.5", self.terms_text)

        self.terms_popup = tk.Toplevel(root)
        self.terms_popup.title("Terms and Conditions")
        self.terms_popup.withdraw()  # Hide the popup initially

        self.terms_text_widget = tk.Text(self.terms_popup, wrap=tk.WORD, height=20, width=70, font=("arial",15),fg="black",highlightthickness=-1)
        self.terms_text_widget.pack(padx=10, pady=10)
        self.terms_text_widget.insert(tk.END, self.terms_text)

        self.checkbtn = tk.Checkbutton(self.terms_popup, text="I agree to the terms", variable=self.var_check)
        self.checkbtn.pack()

        # Bind the X button (closing) to the hide_terms method
        self.terms_popup.protocol("WM_DELETE_WINDOW", self.hide_terms)

        self.show_button = tk.Button(frame, text="Show Terms", command=self.show_terms,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        self.show_button.place(x=160,y=400,width=270)

   

        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=160,y=450,width=270,height=35)


        return_button = tk.Button(self.root, text="Return to Dashboard", command=show_main_app_callback, font=("arial",12,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked


    def show_main_app(self):
        self.root.deiconify()
        if hasattr(self, 'window1'):
            self.window1.destroy()

    def show_terms(self):
        self.terms_popup.deiconify()  # Show the popup
        self.show_button.config(state=tk.DISABLED)

    def hide_terms(self):   
        self.terms_popup.withdraw()  # Hide the popup
        self.show_button.config(state=tk.NORMAL)

   
    def reg(self):
        if (
            self.var_employee_id.get() == ""
            or self.var_fname.get() == ""
            or self.var_lname.get() == ""
            or self.var_mname.get() == ""
            or self.var_cnum.get() == ""
            or self.var_email.get() == ""
            or self.var_department.get() == ""
            or self.var_password.get() == ""
        ):
            messagebox.showerror("Error", "All Field Required!")
            return

        # Check for phone number (cnum) format
        if not re.match(r'^\d{11}$', self.var_cnum.get()):
            messagebox.showerror("Error", "Phone number must be 11 digits")
            return
        
        if '@' not in self.var_email.get():
            messagebox.showerror("Error", "Invalid email format, please enter a valid email")
            return
        try:
            conn = mysql.connector.connect(
                user="root", password="", host="localhost", database="face_recognition"
            )
            mycursor = conn.cursor()
            
            # Check if email already exists
            query_email = "SELECT * FROM regteach WHERE email=%s"
            value_email = (self.var_email.get(),)
            mycursor.execute(query_email, value_email)
            row_email = mycursor.fetchone()
            if row_email is not None:
                messagebox.showerror("Error", "User Email exists, please try another email")
                return

            # Check if first name already exists
            query_fname = "SELECT * FROM regteach WHERE fname=%s"
            value_fname = (self.var_fname.get(),)
            mycursor.execute(query_fname, value_fname)
            row_fname = mycursor.fetchone()
            if row_fname is not None:
                messagebox.showerror("Error", "User with this first name already exists")
                return

            # Check for phone number (cnum) format
            if not re.match(r'^\d{11}$', self.var_cnum.get()):
                messagebox.showerror("Error", "Phone number must be 11 digits")
                return
                             
            # Registration successful
            insert_query = "INSERT INTO regteach (employee_id,fname,mname ,lname, cnum, email,department, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            insert_values = (
                self.var_employee_id.get(),
                self.var_fname.get(),
                self.var_mname.get(),
                self.var_lname.get(),
                self.var_cnum.get(),
                self.var_email.get(),
                self.var_department.get(),
                self.var_password.get(),
            )

            mycursor.execute(insert_query, insert_values)
            conn.commit()

            messagebox.showinfo("Success", "Registration successful.")

            self.root.withdraw()
            self.window1 = tk.Toplevel(self.root)
            self.disable_close_button(self.window1)
            self.app1 = Register(self.window1, self.show_main_app)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
            
    def return_to_main_app(self):
        self.master.withdraw() 
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  

def main():
    root = tk.Tk()
    app = Register(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
