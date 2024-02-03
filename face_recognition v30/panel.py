from tkinter import* 
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import *
from tkinter import ttk
from tkinter import Tk

# Connect to MySQL database
conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
cursor = conn.cursor()

class AdminPanel:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Student Pannel")
        self.root.attributes('-fullscreen',True)
        # self.var_std_id=StringVar()
        # self.var_thr_id=StringVar()
        

 # This part is image labels setting start 
        # first header image  
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
        title_lb1 = Label(bg_img,text="ADMIN DASHBOARD",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

       

        # Creating Frame 
        
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=25,y=55,width=1500,height=610)

        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=750,y=10,width=730,height=580)
        
        return_button = Button(self.root, text="LOGOUT", command=show_main_app_callback,
                               font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        return_button.grid(row=0, column=1, padx=15, pady=820, sticky=W)

        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=730,height=580)

        left_table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        left_table_frame.place(x=10,y=10,width=710,height=460)

        self.del_teacher_btn = Button(left_frame,command=self.teacher_delete_data, text="Delete", width=7, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        self.del_teacher_btn.place(x=20, y=490, width=155, height=40)

        self.teacher_search_entry = Entry(left_frame, font=("verdana", 11), bd=2, relief=GROOVE)
        self.teacher_search_entry.place(x=360, y=490, width=200, height=40)

        self.teacher_search_btn = Button(left_frame, text="Search", command=self.search_teacher_data, font=("verdana", 10, "bold"), fg="white", bg="navyblue")
        self.teacher_search_btn.place(x=190, y=490, width=155, height=40)

        self.teacher_search_entry.insert(0, "Enter First or Last Name")
        self.teacher_search_entry.bind("<FocusIn>", self.ons_entry_click)
        self.teacher_search_entry.bind("<FocusOut>", self.ons_focus_out)

        showAll_btn=Button(left_frame,command=self.teacher_fetch_data,text="Show All",width=12, font=("verdana", 12, "bold"),
                            fg="white", bg="navyblue")
        showAll_btn.place(x=565, y=490, width=155, height=40)

        # Search bar and button for Student
        self.student_search_entry = Entry(right_frame, font=("verdana", 11), bd=2, relief=GROOVE)
        self.student_search_entry.place(x=360, y=25, width=200, height=40)

        self.student_search_entry.insert(0, "Enter Last Name or LRN")

        self.student_search_entry.bind("<FocusIn>", self.on_entry_click)
        self.student_search_entry.bind("<FocusOut>", self.on_focus_out)

        self.student_search_btn = Button(right_frame, text="Search", command=self.search_student_data, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        self.student_search_btn.place(x=190, y=25, width=155, height=40)

        showAll_btn=Button(right_frame,command=self.fetch_data,text="Show All",width=12, font=("verdana", 12, "bold"),
                            fg="white", bg="navyblue")
        showAll_btn.place(x=565, y=25, width=155, height=40)


        scroll_x = ttk.Scrollbar(left_table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(left_table_frame,orient=VERTICAL)
        
        #create table 
        self.teacher_table = ttk.Treeview(left_table_frame,column=("id","fname","lname","cnum","email","ssq","sa","pwd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("id",text="Teacher ID")
        self.teacher_table.heading("fname",text="First Name")
        self.teacher_table.heading("lname",text="Last Name")
        self.teacher_table.heading("cnum",text="Number")
        self.teacher_table.heading("email",text="Email")
        self.teacher_table.heading("ssq",text="Security Answer")
        self.teacher_table.heading("sa",text="Answer")
        self.teacher_table.heading("pwd",text="Password")
        self.teacher_table["show"]="headings"


        # Set Width of Colums 
        self.teacher_table.column("id",width=90, anchor="center")
        self.teacher_table.column("fname",width=90, anchor="center")
        self.teacher_table.column("lname",width=90, anchor="center")
        self.teacher_table.column("cnum",width=120, anchor="center")
        self.teacher_table.column("email",width=130, anchor="center")
        self.teacher_table.column("ssq",width=130, anchor="center")
        self.teacher_table.column("sa",width=100, anchor="center")
        self.teacher_table.column("pwd",width=70, anchor="center")

    


        self.teacher_table.pack(fill=BOTH,expand=1)
        # self.teacher_table.bind("<ButtonRelease>",self.get_cursor)
        self.teacher_fetch_data()

        
      #Table Frame 
      
 

        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=710,height=460)

        self.del_student_btn = Button(right_frame, command=self.student_delete_data, text="Delete", width=7, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        self.del_student_btn.place(x=20, y=25, width=155, height=40)
        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","mName","lName","Div","Gender","DOB","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="First Name")
        self.student_table.heading("mName",text="Middle Name")
        self.student_table.heading("lName",text="Last Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Birthday")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="LRN")
        self.student_table.heading("Email",text="Grade & Section")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("ID",width=60, anchor="center")
        self.student_table.column("Name",width=90, anchor="center")
        self.student_table.column("mName",width=90, anchor="center")
        self.student_table.column("lName",width=90, anchor="center")
        self.student_table.column("Div",width=90, anchor="center")
        self.student_table.column("Gender",width=90, anchor="center")
        self.student_table.column("DOB",width=120, anchor="center")
        self.student_table.column("Address",width=90, anchor="center")
        self.student_table.column("Roll-No",width=100, anchor="center")
        self.student_table.column("Email",width=90, anchor="center")
        self.student_table.column("Teacher",width=90, anchor="center")
        self.student_table.column("Photo",width=90, anchor="center")


        self.student_table.pack(fill=BOTH,expand=1)
        # self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # def get_cursor(self,event=""):
    #     cursor_focus = self.teacher_table.focus()
    #     content = self.teacher_table.item(cursor_focus)
    #     data = content["values"]

    #     self.var_thr_id.set(data[0])
   
    def teacher_fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from regteach")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for j in data:
                self.teacher_table.insert("",END,values=j)
            conn.commit()
        conn.close()


    def on_entry_click(self, event):
        if self.student_search_entry.get() == "Enter Last Name or LRN":
            self.student_search_entry.delete(0, "end")
            self.student_search_entry.config(fg='black')  # Change text color to black

    def on_focus_out(self, event):
        if not self.student_search_entry.get():
            self.student_search_entry.insert(0, "Enter Last Name or LRN")
            self.student_search_entry.config(fg='grey')  # Change text color to grey

    def ons_entry_click(self, event):
        if self.teacher_search_entry.get() == "Enter First or Last Name":
            self.teacher_search_entry.delete(0, "end")
            self.teacher_search_entry.config(fg='black')  # Change text color to black

    def ons_focus_out(self, event):
        if not self.teacher_search_entry.get():
            self.teacher_search_entry.insert(0, "Enter First or Last Name")
            self.teacher_search_entry.config(fg='grey')

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp
    
    def search_teacher_data(self):
        search_query = self.teacher_search_entry.get()

        # Check if search query is empty
        if not search_query:
            messagebox.showinfo("Search Error", "Please enter a search query.")
            return

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM regteach WHERE fname LIKE %s OR lname LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()

        if len(data) != 0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for j in data:
                self.teacher_table.insert("", END, values=j)
            conn.commit()
        else:
            # Show a message if no results found
            messagebox.showinfo("No Results", "No matching records found.")

        conn.close()

    def search_student_data(self):
        search_query = self.student_search_entry.get()

        # Check if search query is empty
        if not search_query:
            messagebox.showinfo("Search Error", "Please enter a search query.")
            return

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM student WHERE lname LIKE %s OR Roll_No LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        else:
            # Show a message if no results found
            messagebox.showinfo("No Results", "No matching records found.")

        conn.close()


   


       

    def teacher_delete_data(self):
        selected_item = self.teacher_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a teacher record to delete.", parent=self.root)
            return

        teacher_id = self.teacher_table.item(selected_item, 'values')[0]

        try:
            delete = messagebox.askyesno("Delete", "Do you want to delete this teacher?", parent=self.root)
            if delete:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                mycursor = conn.cursor()
                sql = "DELETE FROM regteach WHERE id=%s"
                val = (teacher_id,)
                mycursor.execute(sql, val)
                conn.commit()
                self.teacher_fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Teacher record deleted successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error deleting teacher record: {str(es)}", parent=self.root)
   


    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def student_delete_data(self):
        selected_item = self.student_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student record to delete.", parent=self.root)
            return

        student_id = self.student_table.item(selected_item, 'values')[0]

        try:
            delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
            if delete:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                mycursor = conn.cursor()
                sql = "DELETE FROM student WHERE Student_ID=%s"
                val = (student_id,)
                mycursor.execute(sql, val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student record deleted successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error deleting student record: {str(es)}", parent=self.root)

def main():
    root = tk.Tk()
    app = AdminPanel(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
