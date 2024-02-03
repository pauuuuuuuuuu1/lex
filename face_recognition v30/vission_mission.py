from sys import path
from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk



class vis_mis:

    def __init__(self,root, show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Mission Vission and Philisopy Information")
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
        bg1=Image.open(r"Images_GUI\t_bg1.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1566,height=768)

        
        return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)

        #title section
        title_lb1 = Label(bg_img,text="Vision,Mission and School Philosophy ",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

        title_lb1 = Label(bg_img,text="""
    THE VISION
    To be recognized as an excellent Christian Institution that
    Provides God-centered quality education in building
    And molding young achievers.


    THE MISSION
    Provide quality and Biblically-oriented training
    by expanding the learning experience of students
    through holistic education

    """,font=("verdana",13,"bold"),fg="black",highlightthickness=-1,)
        title_lb1.place(x=20,y=55,width=720,height=625)

        title_lb1 = Label(bg_img,text="""
    SCHOOL PHILOSOPHY 

    BIGA ACHIEVERS’ LEARNING INSTITUTE, INC. 
    believes that God Created each child as a unique 
    individual with talents and abilities for 
    discovering and learning. We thereby aim 
    to discover those talents and bring the students 
    to the level of confidence of who they are made for. 
    Hence, we will strive to promote a quality education 
    that gears toward the development of the students’ 
    head, heart, and hand (knowing, valuing, and applying).

    BALII upholds the idea that teachers are channels
    of learning experiences and motivators of interest in 
    acquiring knowledge. Therefore, the teachers should 
    not stop learning and growing in order to become 
    teachers by example. 

    BALII tries to create an enjoyable atmosphere that 
    will foster love and concern for the growth of the child 
    as a whole. To make this happen, we favor appropriate 
    curriculum and approaches over structured and rigid forms 
    of education. In the end, we want to see our students 
    that learning and growing happily in friendly and godly 
    environment.  

    """,font=("verdana",13,"bold"),fg="black",highlightthickness=-1,)
        title_lb1.place(x=760,y=55,width=780,height=625)

        
    def return_to_main_app(self):
        self.root.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp


def main():
    root = tk.Tk()
    app = vis_mis(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()


