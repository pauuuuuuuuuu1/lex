from tkinter import* 
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import *
from tkinter import ttk
from tkinter import Tk
import csv
import os
from tkinter import filedialog
from tkinter import Entry, StringVar, Tk, GROOVE, W
import openpyxl
from tkcalendar import Calendar
from tkinter import Toplevel, Button
import logging
from datetime import datetime
# from main2 import Face_Recognition_System1


# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student_view:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Student Pannel")

        # self.root.state('zoomed')
        self.root.attributes('-fullscreen',True)



        #-----------Variables-------------------
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_std_mname=StringVar()
        self.var_std_lname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
            

    # This part is image labels setting start 
        # backgorund image 
        bg1=Image.open(r"Images_GUI\stdcover.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)


        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=25,y=205,width=1500,height=600)

        self.return_button = tk.Button(self.root, text="BACK", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="#003D60")
        self.return_button.grid(row=0,column=1,padx=1460,pady=815,sticky=E)
        # self.return_button.pack()


        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=10,y=10,width=1470,height=580)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="#FAF9F6",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=1450,height=80)

        #Search
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=6,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","LRN","Name","Section")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="#003D60")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="#003D60")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        generate_csv_btn = Button(self.root, command=self.exportCsvRight, text="CSV", width=8, font=("verdana", 12, "bold"), fg="white", bg="#003D60")
        generate_csv_btn.place(x=50, y=755)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=1460,height=420)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","mName","lName","Div","Gender","DOB","Address","Roll-No","Email","Teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="First Name")
        self.student_table.heading("mName",text="Middle Name")
        self.student_table.heading("lName",text="Last Name")
        self.student_table.heading("Div",text="Schedule")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Birthday")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Roll-No",text="LRN")
        self.student_table.heading("Email",text="Grade & Section")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("ID",width=60,anchor="center")
        self.student_table.column("Name",width=90,anchor="center")
        self.student_table.column("mName",width=90,anchor="center")
        self.student_table.column("lName",width=90,anchor="center")
        self.student_table.column("Div",width=90,anchor="center")
        self.student_table.column("Gender",width=90,anchor="center")
        self.student_table.column("DOB",width=120,anchor="center")
        self.student_table.column("Address",width=90,anchor="center")
        self.student_table.column("Roll-No",width=100,anchor="center")
        self.student_table.column("Email",width=90,anchor="center")
        self.student_table.column("Teacher",width=90,anchor="center")


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


   

# ==================Function Decleration==============================

    def disable_button(self):
        self.take_photo_btn["state"] = tk.DISABLED

    def enable_button(self):
        # Enable the "Take Pic" button when the radio button is selected
        self.take_photo_btn['state'] = tk.NORMAL

    def return_to_main_app(self):
        self.root.withdraw()
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()

    
    def exportCsvRight(self):
        try:
            # Get the data from the right table (attendanceReport)
            right_table_data = []
            for item in self.student_table.get_children():
                values = self.student_table.item(item, 'values')
                right_table_data.append(values)

            if len(right_table_data) < 1:
                messagebox.showerror("Error", "No Data Found!", parent=self.root)
                return False

            # Ask user for the file name and location without specifying the file type extension
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save Spreadsheet",
                filetypes=(("All Files", "*.*"),),
                parent=self.root
            )

            if fln:
                # Check if the filename has an extension, and add '.xlsx' if missing
                if not fln.lower().endswith(('.xlsx', '.csv')):
                    fln += '.xlsx'  # You can change this to your default extension

                # Check if the user selected CSV or Excel format
                if fln.lower().endswith('.csv'):
                    with open(fln, mode="w", newline="") as myfile:
                        exp_write = csv.writer(myfile, delimiter=",")
                        for i in right_table_data:
                            exp_write.writerow(i)
                    messagebox.showinfo("Success", "Exported data successfully as CSV!")
                elif fln.lower().endswith('.xlsx'):
                    wb = openpyxl.Workbook()
                    ws = wb.active
                    for row in right_table_data:
                        ws.append(row)
                    wb.save(fln)
                    messagebox.showinfo("Success", "Exported data successfully as CSV!")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    logging.basicConfig(filename='user_actions.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()

        query = """
        SELECT student.*, CONCAT(regteach.fname, ' ', regteach.lname) AS Teacher_Name
        FROM student
        INNER JOIN regteach ON CONCAT(regteach.fname, ' ', regteach.lname) = student.Teacher_Name
        WHERE CONCAT(regteach.fname, ' ', regteach.lname) IN (
        SELECT student.Teacher_Name
        FROM student
        GROUP BY student.Teacher_Name
        HAVING COUNT(*) > 1
        )
                """

        # query = "Select * FROM student"

            
        mycursor.execute(query)
        data = mycursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            

        conn.close()

    #================================get cursor function=======================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0])
        self.var_std_name.set(data[1])
        self.var_std_mname.set(data[2])
        self.var_std_lname.set(data[3])
        self.var_div.set(data[4])
        self.var_gender.set(data[5])
        self.var_dob.set(data[6])
        self.var_address.set(data[7])
        self.var_roll.set(data[8])
        self.var_email.set(data[9])
        self.var_teacher.set(data[10])
        self.var_radio1.set(data[11] and "Yes")
        self.take_photo_btn['state'] = tk.NORMAL
        self.radiobtn1['state'] = tk.NORMAL
        self.radiobtn2['state'] = tk.DISABLED

    
    #==============Delete Function=============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
                logging.info(f"User deleted data for Student ID: {self.var_std_id.get()}")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    
                logging.error(f"Error during data deletion: {str(es)}")

    # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_std_mname.set(""),
        self.var_std_lname.set(""),
        self.var_div.set("Morning"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("No")
        self.take_photo_btn['state'] = tk.DISABLED
        self.radiobtn1['state'] = tk.DISABLED
        self.radiobtn2['state'] = tk.NORMAL
    
    # ===================Search Data==================
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                my_cursor = conn.cursor()

                search_field = self.var_searchTX.get()
                search_value = str(self.var_search.get())

                if search_field == "Section":
                    # Modify the SQL query based on the "Section" search
                    sql = "SELECT Student_ID, Name, mName, lName, Division, Gender, DOB, Address, Roll_No, Email, Teacher_Name, PhotoSample FROM student WHERE Email LIKE %s"
                elif search_field == "Name":
                    # Modify the SQL query based on the "Name" search
                    sql = "SELECT Student_ID, Name, mName, lName, Division, Gender, DOB, Address, Roll_No, Email, Teacher_Name, PhotoSample FROM student WHERE Name LIKE %s"
                else:
                    # Default to the original query (Email search)
                    sql = "SELECT Student_ID, Name, mName, lName, Division, Gender, DOB, Address, Roll_No, Email, Teacher_Name, PhotoSample FROM student WHERE Roll_No LIKE %s"

                params = (f"%{search_value}%",)
                my_cursor.execute(sql, params)

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", "Data Not Found", parent=self.root)

                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

def main():
    root = tk.Tk()
    app = Student_view(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()