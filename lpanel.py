import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
import os
from adminlogin import Adminlogin
from login import Login



class LoginPanel:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1566x768+0+0")

        self.root.attributes('-fullscreen',True)

       # This part is image labels setting start 
        # first header image  
        # img=Image.open(r"Images_GUI\biga.jpg")
        # img=img.resize((1566,130),Image.LANCZOS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg)
        # f_lb1.place(x=0,y=0,width=1566,height=130)

        # backgorund image    
        bg1=Image.open(r"Images_GUI\panel.jpg")
        bg1=bg1.resize((1575,900),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)


        # Button for Admin
        det_b1 = tk.Button(self.root,command=self.open_windows2, text="ADMIN",cursor="hand2",font=("tahoma",15,"bold"),bg="#244194",fg="white")
        det_b1.place(x=630,y=370,width=281,height=45)
        
        # Button for Teachers
        std_b1 = tk.Button(self.root,command=self.open_windows1, text="TEACHER",cursor="hand2",font=("tahoma",15,"bold"),bg="#244194",fg="white")
        std_b1.place(x=630,y=500,width=281,height=45)

    
    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

    def open_windows1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Login(self.window1, self.show_main_app)

    def open_windows2(self):
        self.root.withdraw()
        self.window2 = tk.Toplevel(self.root)
        self.disable_close_button(self.window2)
        self.app2 = Adminlogin(self.window2, self.show_main_app)
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
        if hasattr(self, 'window2'):
            self.window2.destroy()
        
    

    









def main():
    root = tk.Tk()
    app = LoginPanel(root)
    root.mainloop()

if __name__ == "__main__":
    main()

