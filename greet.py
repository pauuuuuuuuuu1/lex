from sys import path
from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class Greetings:

    def __init__(self,root, show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Greetings Information")
        self.root.attributes('-fullscreen',True)
        # This part is image labels setting start
         
        # backgorund image 
        bg1=Image.open(r"Images_GUI\greetings.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        
        return_button = tk.Button(self.root, text="BACK", command=show_main_app_callback, font=("arial",15,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=1450,pady=810,sticky=E)


        title_lb1 = Label(bg_img,text="""
        Dear Achiever,

        Education is wealth. It makes a person grow intellectually, socially, and emotionally. 
        But BALII offers more. We believe that education without the fear of God is incomplete. 
        With live & prayer, wer help our students grow in the saving knowledge and grace of the 
        Lord Jesus.

        To study at BALII (Biga Achievers Learning Institute, Inc.) is a wise decision you made. 
        BALII is a conductive place to study. It has a safe a fresh environment in the community 
        of believers. We also have loving, qualified & dedicated faculty who can make each learner 
        a real achiever.

        This Handbook & Diary is written for your guidance. Familiarize yourself with its 
        contents for the smooth teacher-learning relationship.

        Thank you for becoming a part of BALII.

        “Commit your way unto the Lord, trust in Him and He shall bring it to pass”
        Psalms 37:5

        Ptr. Generus  Ignacio  
        Principal
        """,font=("arial",14),fg="black")
        title_lb1.place(x=275,y=250,width=1000,height=570)


        
    def return_to_main_app(self):
        self.root.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp


def main():
    root = tk.Tk()
    app = Greetings(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()


