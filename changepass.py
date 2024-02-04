from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import re

class Reset:
    def __init__(self, root, show_main_app_callback=None):
        self.root = root
        self.root.title("User Profile")
        self.root.geometry("1566x768+0+0")
        self.root.attributes('-fullscreen',True)
        
        self.show_main_app_callback = show_main_app_callback
        
        # backgorund image 
        bg1=Image.open(r"Images_GUI\changepass.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_employee_id = StringVar()
        self.var_old_pwd = StringVar()
        self.var_password = StringVar()
        self.var_confirm_pwd = StringVar()

        id_label = Label(self.root,text="Employee ID:",font=("arial",15),fg="white",bg="#003D60")
        id_label.place(x=608, y=365)

        self.id_entry = ttk.Entry(self.root, textvariable=self.var_employee_id, font=('times new roman', 15))
        self.id_entry.place(x=750, y=360, width=210,height=35)
        
        old_pwd_label = Label(self.root,text="Old Password:",font=("arial",15),fg="white",bg="#003D60")
        old_pwd_label.place(x=596, y=420)

        self.old_pwd_entry = ttk.Entry(self.root, textvariable=self.var_old_pwd, font=('times new roman', 15))
        self.old_pwd_entry.place(x=750, y=415, width=210,height=35)

        # Label for New Password
        new_pwd_label = Label(self.root,text="New Password:",font=("arial",15),fg="white",bg="#003D60")
        new_pwd_label.place(x=590, y=480)

        self.txtteacherpwd=ttk.Entry(self.root,textvariable=self.var_password,font=('times new roman',15))
        self.txtteacherpwd.place(x=750, y=475, width=210, height=35)
        
        # Label for Confirm Password
        confirm_pwd_label = Label(self.root,text="Confirm Password:",font=("arial",15),fg="white",bg="#003D60")
        confirm_pwd_label.place(x=560, y=540)
        
        self.confirm_pwd_entry = ttk.Entry(self.root, textvariable=self.var_confirm_pwd, font=('times new roman', 15))
        self.confirm_pwd_entry.place(x=750, y=535, width=210, height=35)


        btn_save=Button(root, text="CHANGE PASSWORD", command=self.update_password, font=("arial",15), bg="#6A8CC9", fg="white")
        btn_save.place(x=650, y=620, width=230,height=40)
        
        self.return_button = tk.Button(self.root, text="BACK", command=show_main_app_callback, font=("verdana",15),fg="white", bg="#003D60")
        self.return_button.grid(row=0,column=1,padx=1445,pady=805,sticky=E)
        
    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()
            
    def update_password(self):
        #connect to the db
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        #fetch the current password from the database
        query=("select password from regteach where employee_id=%s")
        value=(self.var_employee_id.get(),)
        mycursor.execute(query,value)
        row = mycursor.fetchone()

        # Check if new password and confirm password match
        if self.var_password.get() != self.var_confirm_pwd.get():
            messagebox.showerror("Error", "New password and confirm password does not match!", parent=self.root)
            return
        
        # Check if the old password matches current password in the database
        if row[0] == self.var_old_pwd.get():
            new_password = self.var_password.get()
            if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', new_password):
                messagebox.showerror("Error", "Password should be at least 8 characters long!", parent=self.root)
                return
            try:
                query=("update regteach set password=%s where employee_id=%s")
                value=(self.var_password.get(), self.var_employee_id.get())
                mycursor.execute(query,value)
                conn.commit()
                messagebox.showinfo("Info", "Successfully changed password!", parent=self.root)
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                conn.rollback()
        else:
            messagebox.showerror("Error", "The old password does not match your credentials.", parent=self.root)

        conn.close()

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

    
def main():
    root = tk.Tk()
    app = Reset(root)
    root.mainloop()

if __name__ == "__main__":
    main()
