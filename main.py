import tkinter as tk
from tkinter import*
from PIL import Image,ImageTk
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from helpsupport import Helpsupport
from school_info import Schoolinfo
from offline_face_recognition import OFFline_face_recognition
from instruction import Instruction
from students_only import Student_view
from changepass import Reset

class MainApp:
    
    def __init__(self, root, show_main_app_callback):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1566x768+0+0")

        self.root.attributes('-fullscreen',True)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\cover.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # student panel
        std_img_btn=Image.open(r"Images_GUI\student.png")
        std_img_btn=std_img_btn.resize((200,200),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.open_window1,image=self.std_img1,cursor="hand2")
        std_b1.place(x=270,y=390,width=220,height=220)

        std_b1 = tk.Button(self.root, text="Student Panel", command=self.open_window1,cursor="hand2",font=("tahoma",15,"bold"),bg="#003D60",fg="white")
        std_b1.place(x=270,y=620,width=221,height=45)


        # online face recog
        det_img_btn=Image.open(r"Images_GUI\stdfacerecog.png")
        det_img_btn=det_img_btn.resize((200,200),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.open_window2,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=530,y=390,width=220,height=220)
        
        det_b1 = tk.Button(self.root, text="Online Attendance", command=self.open_window2,cursor="hand2",font=("tahoma",15,"bold"),bg="#003D60",fg="white")
        det_b1.place(x=530,y=620,width=221,height=45)


         # offline face recog
        ofdet_img_btn=Image.open(r"Images_GUI\no-wifi.png")
        ofdet_img_btn=ofdet_img_btn.resize((200,200),Image.LANCZOS)
        self.ofdet_img1=ImageTk.PhotoImage(ofdet_img_btn)

        ofdet_b1 = Button(bg_img,command=self.open_window3,image=self.ofdet_img1,cursor="hand2",)
        ofdet_b1.place(x=790,y=390,width=220,height=220)
        
        ofdet_b1 = tk.Button(self.root, text="Offline Attendance", command=self.open_window3,cursor="hand2",font=("tahoma",15,"bold"),bg="#003D60",fg="white")
        ofdet_b1.place(x=790,y=620,width=221,height=45)

        
        # attendance
        att_img_btn=Image.open(r"Images_GUI\calendar.png")
        att_img_btn=att_img_btn.resize((200,200),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.open_window4,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=1050,y=390,width=220,height=220)

        att_b1 = tk.Button(self.root, text="Attendance", command=self.open_window4, cursor="hand2",font=("tahoma",15,"bold"),bg="#003D60",fg="white")
        att_b1.place(x=1050,y=620,width=221,height=45)
        
        pho_b1_1 = tk.Button(self.root, text="School Info", command=self.open_window6,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#003D60")
        pho_b1_1.place(x=270,y=680,width=221,height=45)

        ins_b1 = tk.Button(self.root, text="Instruction", command=self.open_window9,font=("tahoma",15,"bold"),bg="white",fg="#003D60")
        ins_b1.place(x=530,y=680,width=221,height=45)

        hlp_b1_1 = tk.Button(self.root, text="Help Support", command=self.open_window5,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#003D60")
        hlp_b1_1.place(x=790,y=680,width=221,height=45)
        
        trai_b1 = tk.Button(self.root, text="Change Password", command=self.open_window7,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="#003D60")
        trai_b1.place(x=1050,y=680,width=221,height=45)

        # exit
        exi_b1_1 = tk.Button(self.root, text="LOGOUT", command=self.open_window10,cursor="hand2",font=("tahoma",15,"bold"),bg="#003D60",fg="white")
        exi_b1_1.grid(row=0,column=1,padx=1420,pady=810,sticky=E)
    
    def open_window1(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Student_view(self.window1, self.show_main_app)

    def open_window2(self):
        self.root.withdraw()
        self.window2 = tk.Toplevel(self.root)
        self.disable_close_button(self.window2)
        self.app2 = Face_Recognition(self.window2, self.show_main_app)
    
    def open_window3(self):
        self.root.withdraw()
        self.window3 = tk.Toplevel(self.root)
        self.disable_close_button(self.window3)
        self.app3 = OFFline_face_recognition(self.window3, self.show_main_app)

    def open_window4(self):
        self.root.withdraw()
        self.window4 = tk.Toplevel(self.root)
        self.disable_close_button(self.window4)
        self.app4 = Attendance(self.window4, self.show_main_app)
    
    def open_window5(self):
        self.root.withdraw()
        self.window5 = tk.Toplevel(self.root)
        self.disable_close_button(self.window5)
        self.app5 = Helpsupport(self.window5, self.show_main_app)
    
    def open_window6(self):
        self.root.withdraw()
        self.window6 = tk.Toplevel(self.root)
        self.disable_close_button(self.window6)
        self.app6 = Schoolinfo(self.window6, self.show_main_app)
    
    def open_window7(self):
        self.root.withdraw()
        self.window7 = tk.Toplevel(self.root)
        self.disable_close_button(self.window7)
        self.app7 = Reset(self.window7, self.show_main_app)
    
    def open_window9(self):
        self.root.withdraw()
        self.window9 = tk.Toplevel(self.root)
        self.disable_close_button(self.window9)
        self.app9 = Instruction(self.window9, self.show_main_app)

    def open_window10(self):
        self.root.withdraw()
        self.window10 = tk.Toplevel(self.root)
        self.disable_close_button(self.window10)
        self.app10 = (self.window10, self.show_main_app)
        self.root.destroy()

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def return_to_main_app(self):
        self.root.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp
    

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window1'):
            self.window1.destroy()
        if hasattr(self, 'window2'):
            self.window2.destroy()
        if hasattr(self, 'window3'):
            self.window3.destroy()
        if hasattr(self, 'window4'):
            self.window4.destroy()
        if hasattr(self, 'window5'):
            self.window5.destroy()
        if hasattr(self, 'window6'):
            self.window6.destroy()
        if hasattr(self, 'window7'):
            self.window7.destroy()
        if hasattr(self, 'window8'):
            self.window8.destroy()
        if hasattr(self, 'window9'):
            self.window9.destroy()
        if hasattr(self, 'window10'):
            self.window10.destroy() 

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

