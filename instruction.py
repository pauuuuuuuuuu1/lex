from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Instruction:
    def __init__(self, root, show_main_app_callback):
        self.root = root
        self.root.geometry("1566x768+0+0")
        self.root.title("Instruction Information")
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
        title_label = Label(bg_label, text="Instruction", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
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
            PAGAWA NG INSTRUCTION
            PAKIARAL MUNA PARA PAG GUMAWA NG INSTRUCTION MAAYOS THANKYOU :)
    
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
    app = Instruction(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
