import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
import os
from panel import AdminPanel
from student import Student
from train import Train
from python_monitor import LogViewerApp


class adminfeat:
    
    def __init__(self, root,show_main_app_callback):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1566x768+0+0")

        self.root.attributes('-fullscreen',True)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\adminpanel.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # student
        std_img_btn=Image.open(r"Images_GUI\user.png")
        std_img_btn=std_img_btn.resize((240,240),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.open_windows1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=260,y=360,width=280,height=280)

        std_b1 = tk.Button(self.root,command=self.open_windows1, text="STUDENTS",cursor="hand2",font=("arial",15,"bold"), fg="white", bg="#003D60")
        std_b1.place(x=262,y=645,width=281,height=45)

        # teacher
        det_img_btn=Image.open(r"Images_GUI\teacher.png")
        det_img_btn=det_img_btn.resize((240,240),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.open_windows3,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=638,y=360,width=280,height=280)
        
        det_b1 = tk.Button(self.root, text="TEACHERS",command=self.open_windows3,cursor="hand2",font=("arial",15,"bold"), fg="white", bg="#003D60")
        det_b1.place(x=640,y=645,width=281,height=45)
        
        # activity logs
        logs_img_btn=Image.open(r"Images_GUI\logs.png")
        logs_img_btn=logs_img_btn.resize((240,240),Image.LANCZOS)
        self.logs_img1=ImageTk.PhotoImage(logs_img_btn)

        logs_b1 = Button(bg_img,command=self.open_windows4,image=self.logs_img1,cursor="hand2",)
        logs_b1.place(x=998,y=360,width=280,height=280)
        
        return_button = Button(self.root, text="ACTIVITY LOGS", command=self.open_windows4,font=("arial", 15, "bold"), fg="white", bg="#003D60")
        return_button.place(x=1000,y=645,width=281,height=45)
        
        self.return_button = tk.Button(self.root, text="LOGOUT", command=show_main_app_callback, font=("arial",15,"bold"),bg="#003D60",fg="white")
        self.return_button.grid(row=0,column=1,padx=1420,pady=810,sticky=E)
        
        
    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()

    def open_windows1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Student(self.window1, self.show_main_app)

    
    def open_windows3(self):
        self.root.withdraw()
        self.window3 = tk.Toplevel(self.root)
        self.disable_close_button(self.window3)
        self.app3 = AdminPanel(self.window3, self.show_main_app)
        
        
    def open_windows4(self):
        self.root.withdraw()
        self.window4 = tk.Toplevel(self.root)
        self.disable_close_button(self.window4)
        self.app4 = LogViewerApp(self.window4, self.show_main_app)
        
        
        
        
        
    
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
        if hasattr(self, 'window3'):
            self.window3.destroy()
        
    

    









def main():
    root = tk.Tk()
    app = adminfeat(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()

