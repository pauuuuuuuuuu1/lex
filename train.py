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


class Train:

    def __init__(self,root, show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Train Pannel")

        self.root.attributes('-fullscreen',True)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\imagetrain.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        
        return_button = tk.Button(self.root, text="Return to Dashboard", command=show_main_app_callback, font=("arial",12,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=15,pady=810,sticky=W)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((280,280),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=310,width=280,height=280)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("arial",15,"bold"),bg="#003D60",fg="white")
        std_b1_1.place(x=600,y=600,width=280,height=45)


  


    # ==================Create Function of Traing===================
    
    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

    def train_classifier(self):
        try:
            data_dir = "data_img"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for i, image in enumerate(path):
                img = Image.open(image).convert('L')  # convert in gray scale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)

                if i >= len(path) - 100:  # Show only the last 100 images
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1) == 13

            ids = np.array(ids)

            # =================Train Classifier=============
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("clf.xml")
        
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Dataset Completed!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)



def main():
    root = tk.Tk()
    app = Train(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()