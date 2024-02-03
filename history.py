from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class History:
    def __init__(self, root, show_main_app_callback):
        self.root = root
        self.root.geometry("1566x768+0+0")
        self.root.title("History Information")
        self.root.attributes('-fullscreen',True)
        # Header image
        img = Image.open(r"Images_GUI\biga.jpg")
        img = img.resize((1566, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        header_label = Label(self.root, image=self.photoimg)
        header_label.place(x=0, y=0, width=1566, height=130)

        # Background image
        bg_img = Image.open(r"Images_GUI\t_bg1.jpg")
        bg_img = bg_img.resize((1566, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photobg1)
        bg_label.place(x=0, y=130, width=1566, height=768)

        # Return button
        return_button = Button(self.root, text="Return to MainApp", command=show_main_app_callback,
                               font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        return_button.grid(row=0, column=1, padx=15, pady=820, sticky=W)

        # Title section
        title_label = Label(bg_label, text="History", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_label.place(x=0, y=0, width=1566, height=45)

        # Scrollbar and Canvas
        canvas = Canvas(bg_label, bg="white")
        canvas.place(x=20, y=65, width=1500, height=600)

        scrollbar = Scrollbar(bg_label, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        essay_text = """
            BALII HISTORY
            Once a Vision Now a Reality
            One of PMI’s vision and mission is to reach out to the community. Community services was then organized and one of this was the 
            kindergarten school. It was established in 1975 under the supervision of Mrs. Henrietta Olavidez. Its primary purpose was to provide a 
            training ground for kinder teachers as they do their practicum as a requirement under the Christian Education program.PMI kindergarten 
            school did not only provide a place for enhancing the knowledge of students under the Christian Education degree program. 
            Children in and out of PMI benefited from it. A number of students enrolled and the first batch of graduates were: 
            Dante Calanog,Edgar Peji, Bernard Feliciano, Jonathan Dayrit, 
            Maybel Villar, Fanny Unabia, Carol Fortune, Helen Grace Olivadez, Jonathan Dominguez, David Dominguez and Hannah Gatorian.
            Nursery pupils who graduated were: Carlo Feliciano, Hannah Gay Olavidez, Joluan Dayrit, Eleanor Abuton and some nursery 
            pupils from Biga. In 1982 PMI kinder school was transferred to Biga Elementary school, 
            for the reason that there was no available classroom at PMI.The room that was used as a classroom, was occupied by an MCIF personnel. 
            Mrs. Monica Villar one of PMI staff members handled the class and was assisted by PMI students who majored in CE.
            After three years PMI kindergarten school was transferred back to PMI.In 1988, Miss Devorah Napicol, an alumna at the 
            same time a faculty of PMI started as full-time head teacher with the practicing student-teacher under the supervision of Mrs. Olivadez.  
            In 1992, Mrs. Esther Campilan dela Cruz, an alumna also became her assistant teacher then after one year she became the head teacher 
            up to 2000. The community-based school went on until the time it was decided to be adopted by ACE program in 2001 but unfortunately 
            it didn’t materialize. Thus, concerned group of PMI tried their best to re-open the kinder school. It was in the persistence of the 
            leadership of the former academic Dean Rev. Hector T. Belandres; head of the Christian Education Department,  Miss Elvira E. Hernandez; 
            business manager, Rev. Jim Estorez with Mrs. Anicia Gatorian and Mrs. Esther C. dela Cruz, the former teacher. With all the fervent prayers, 
            vigor desire and personal faithful monetary regular pledges the operation was granted again under the presidency of 
            Engr. Ruben L. de Leon. Mrs. Recelita Tarcena-San Pascual was then the head teacher and Miss Miriam Aboy was the principal.
            It was named as PMI’s Kiddie House of Learning as supervised by the Christian Education Department that serves as a laboratory school 
            for those students who major in Christian Education who are required for practicum in Principles and Methods of Teaching, 
            CE of Children and Kinder Theory and Observations. This was headed by Miss Elvira E. Hernandez. Under her supervision, 
            Mrs. Carmi Avante, a wife of former student was hired  as the administrator-teacher and was assisted by Miss Susan Gabrinao, 
            also an alumna from 2001-2003. When Mrs. Avante resigned Miss Gabrinao became the head teacher and supervised by Ms. Aboy.
    
        """

        essay_widget = Text(content_frame, wrap="word", width=180, height=30,  font=("verdana", 12, "bold"), fg="black")
        essay_widget.insert("135.5", essay_text)
        essay_widget.config(state="disabled")
        essay_widget.pack(pady=0)
        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

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
