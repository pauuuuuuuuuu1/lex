from tkinter import* 
import tkinter as tk
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image,ImageTk
from tkinter import messagebox

class LogViewerApp:
    def __init__(self, root, show_main_app_callback):
        self.root = root
        self.root.geometry("1566x768+0+0")
        self.root.title("Log Viewer")

        self.root.attributes('-fullscreen', True)

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
        title_lb1 = Label(bg_img,text="Monitoring and Logging System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=25,y=55,width=1500,height=610)


        
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=10,y=10,width=1470,height=580)
        # Create a frame to hold the components

        # self.return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        # self.return_button.grid(row=0,column=1,padx=15,pady=810,sticky=W)

        # Create GUI components

        self.log_display = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=120, height=30)
        self.log_display.place(x=25,y=85,width=1450,height=470)

        # Log levels filter
        self.log_levels = ['INFO']
        self.selected_log_level = tk.StringVar(value='INFO')
        level_filter_label = ttk.Label(main_frame, text="Filter by Log Level:")
        level_filter_label.place(x=25, y=45)

        level_filter_combobox = ttk.Combobox(main_frame, values=self.log_levels, textvariable=self.selected_log_level, state="readonly")
        level_filter_combobox.place(x=135, y=45)
        level_filter_combobox.bind("<<ComboboxSelected>>", self.filter_logs)
        

        self.load_logs()
        
        return_button = Button(self.root, text="LOGOUT", command=show_main_app_callback,
                               font=("verdana", 12, "bold"), fg="white", bg="#003D60")
        return_button.grid(row=0, column=1, padx=15, pady=820, sticky=W)

    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()
    

    def load_logs(self):
        # Read logs from a file (replace 'app_log.log' with the actual log file)
        with open('user_actions.log', 'r') as log_file:
            logs = log_file.read()

        # Display all logs initially
        self.log_display.insert(tk.END, logs)

    def filter_logs(self, event):
        selected_level = self.selected_log_level.get()

        # Read logs from a file (replace 'app_log.log' with the actual log file)
        with open('user_actions.log', 'r') as log_file:
            logs = log_file.readlines()

        # Filter logs based on selected log level
        filtered_logs = [log.strip() for log in logs if self.is_valid_log(log, selected_level)]

        # Display filtered logs
        self.log_display.config(state=tk.NORMAL)
        self.log_display.delete(1.0, tk.END)  # Clear existing logs
        self.log_display.insert(tk.END, '\n'.join(filtered_logs))
        self.log_display.config(state=tk.DISABLED)  # Disable text editing

    def is_valid_log(self, log, selected_level):
        log_parts = log.split(' - ')
        if len(log_parts) == 3:
            log_level = log_parts[1].strip()
            return log_level == selected_level
        return False



def main():
    root = tk.Tk()
    app = LogViewerApp(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
