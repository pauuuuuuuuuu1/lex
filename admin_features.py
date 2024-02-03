import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
import os
from panel import AdminPanel
from adminlogin import *


class adminfeat:
    
    def __init__(self, root,show_main_app_callback):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1566x768+0+0")

        self.root.attributes('-fullscreen',True)

       # This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\biga.jpg")
        img=img.resize((1566,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1566,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1566,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Login Panel System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)


       # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student
        std_img_btn=Image.open(r"Images_GUI\panels.png")
        std_img_btn=std_img_btn.resize((240,240),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.open_windows1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=400,y=200,width=280,height=280)

        std_b1 = tk.Button(self.root,command=self.open_windows1, text="Panel Info",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1.place(x=402,y=612,width=281,height=45)



        # Face Recog
        det_img_btn=Image.open(r"Images_GUI\logging.png")
        det_img_btn=det_img_btn.resize((240,240),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.open_windows2,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=800,y=200,width=280,height=280)
        det_b1 = tk.Button(self.root,command=self.open_windows2, text="Monitoring Logging",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1.place(x=802,y=612,width=281,height=45)

        self.return_button = tk.Button(self.root, text="Logout", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        self.return_button.grid(row=0,column=1,padx=15,pady=810,sticky=W)

    
    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()

    def open_windows1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = AdminPanel(self.window1, self.show_main_app)

    
    def open_windows3(self):
        self.root.withdraw()
        self.window3 = tk.Toplevel(self.root)
        self.disable_close_button(self.window3)
        self.app3 = Adminlogin(self.window3, self.show_main_app)
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
        if hasattr(self, 'window2'):
            self.window2.destroy()
        if hasattr(self, 'window3'):
            self.window3.destroy()
        
    

    









def main():
    root = tk.Tk()
    app = adminfeat(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()

