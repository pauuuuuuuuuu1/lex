from sys import path
from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from history import History
from greet import Greetings
from vission_mission import vis_mis


class Schoolinfo:

    def __init__(self,root, show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("School Information")

        self.root.attributes('-fullscreen',True)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\about.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        return_button = tk.Button(self.root, text="Return to Dashboard", command=show_main_app_callback, font=("arial",12,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)
        
        # About1
        std_img_btn=Image.open(r"Images_GUI\green.png")
        std_img_btn=std_img_btn.resize((270,270),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.open_window1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=210,y=380,width=280,height=280)

        std_b1 = tk.Button(self.root, text="Greetings", command=self.open_window1,cursor="hand2",font=("arial",15,"bold"),bg="#003D60",fg="white")
        std_b1.place(x=212,y=680,width=280,height=45)

          # About2
        det_img_btn=Image.open(r"Images_GUI\mission_vision.png")
        det_img_btn=det_img_btn.resize((160,160),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.open_window2,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=620,y=380,width=280,height=280)
        
        det_b1 = tk.Button(self.root, text="Mission and Vision", command=self.open_window2,cursor="hand2",font=("arial",15,"bold"),bg="#003D60",fg="white")
        det_b1.place(x=622,y=680,width=280,height=45)


        # About3
        trai_img_btn=Image.open(r"Images_GUI\history.jpg")
        trai_img_btn=trai_img_btn.resize((180,180),Image.LANCZOS)
        self.trai_img1=ImageTk.PhotoImage(trai_img_btn)

        trai_b1 = Button(bg_img,command=self.open_window3,image=self.trai_img1,cursor="hand2",)
        trai_b1.place(x=1050,y=340,width=280,height=280)
        
        trai_b1 = tk.Button(self.root, text="History", command=self.open_window3,cursor="hand2",font=("arial",15,"bold"),bg="#003D60",fg="white")
        trai_b1.place(x=1052,y=680,width=280,height=45)

    def open_window1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Greetings(self.window1, self.show_main_app)

    def open_window2(self):
        self.root.withdraw()
        self.window2 = tk.Toplevel(self.root)
        self.disable_close_button(self.window2)
        self.app2 = vis_mis(self.window2, self.show_main_app)
    
    def open_window3(self):
        self.root.withdraw()
        self.window3 = tk.Toplevel(self.root)
        self.disable_close_button(self.window3)
        self.app3 = History(self.window3, self.show_main_app)

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
    app = Schoolinfo(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()


