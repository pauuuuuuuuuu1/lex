from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk

class History:
    def __init__(self, root, show_main_app_callback):
        self.root = root
        self.root.geometry("1566x768+0+0")
        self.root.title("History Information")
        self.root.attributes('-fullscreen',True)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\history.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        return_button = tk.Button(self.root, text="BACK", command=show_main_app_callback, font=("arial",15,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=1450,pady=810,sticky=E)
        
    def return_to_main_app(self):
        self.root.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

def main():
    root = Tk()
    app = History(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
