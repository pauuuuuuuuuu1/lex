from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import re

class Profile:
    def __init__(self, root, show_main_app_callback=None):
        self.root = root
        self.root.title("User Profile")
        self.root.geometry("1566x768+0+0")
        self.root.attributes('-fullscreen',True)
        
        self.show_main_app_callback = show_main_app_callback
        
        # backgorund image 
        bg1=Image.open(r"Images_GUI\cover.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_employee_id = StringVar()
        self.var_password = StringVar()

        self.txtteacher=ttk.Entry(root,textvariable=self.var_employee_id, font=('times new roman', 15))
        self.txtteacher.place(x=20, y=165, width=210, height=35)

        self.txtteacherpwd=ttk.Entry(root,textvariable=self.var_password,font=('times new roman',15))
        self.txtteacherpwd.place(x=20, y=225, width=210,height=35)

        btn_save=Button(root, text="Save Password", command=self.update_password, font=("times new roman",15,"bold"), bg="gray", fg="white")
        btn_save.place(x=50, y=275, width=150,height=35)
    
    def update_password(self):
        conn = mysql.connector.connect(
                user="root", password="", host="localhost", database="face_recognition"
        )
        try:
            new_password = self.var_password.get()
            if len(new_password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long")
                return
            conn = mysql.connector.connect(user="root", password="", host="localhost", database="face_recognition")
            mycursor = conn.cursor()
            mycursor.execute("UPDATE regteach SET password = %s WHERE employee_id = %s", (new_password, self.var_employee_id.get()))
            conn.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
        except Exception as es:
            messagebox.showerror("Error", f"Due Error: {str(es)}", parent=self.master)

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

def main():
    root = tk.Tk()
    app = Profile(root)
    root.mainloop()

if __name__ == "__main__":
    main()
