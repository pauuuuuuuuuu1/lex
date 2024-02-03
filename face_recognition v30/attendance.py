# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import filedialog
from tkcalendar import *
import tkinter as tk
import openpyxl

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Attendance Panel")

        self.root.attributes('-fullscreen',True)

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        def pick_date(event):
            global cal, date_window

            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Choose Date of Birth')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, selectmode="day", date_pattern="y-mm-dd")
            cal.place(x=0, y=0)

            submit_btn = Button(date_window, text="Submit", command=grab_date)
            submit_btn.place(x=80, y=190)

        def grab_date():
            date_entry.delete(0, END)
            date_entry.insert(0, cal.get_date())
            date_window.destroy()  # Corrected line: destroy the date_window
            

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\biga.jpg")
        img=img.resize((1566,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1566,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1566,height=768)


        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE DASHBOARD",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=25,y=55,width=1500,height=610)


        
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=10,y=10,width=1470,height=580)
        # Left Label Frame 
        # left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        # left_frame.place(x=15,y=10,width=680,height=480)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(right_frame,text="ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(right_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(right_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(right_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # Department
        dep_label = Label(right_frame,text="Grade - Sec:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dep_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(right_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        dep_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(right_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(right_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(right_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        date_entry = Entry(right_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"),bd=2, relief=GROOVE)
        date_entry.insert(0,"yyyy-mm-dd")
        date_entry.bind("<1>", pick_date)
        date_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #Attendance
        student_attend_label = Label(right_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(right_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        # table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        # table_frame.place(x=10,y=120,width=635,height=310)

        # #scroll bar 
        # scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        # #create table 
        # self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Name","Email","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # scroll_x.pack(side=BOTTOM,fill=X)
        # scroll_y.pack(side=RIGHT,fill=Y)
        # scroll_x.config(command=self.attendanceReport_left.xview)
        # scroll_y.config(command=self.attendanceReport_left.yview)

        # self.attendanceReport_left.heading("ID",text="Std-ID")
        # self.attendanceReport_left.heading("Name",text="Std-Name")
        # self.attendanceReport_left.heading("Email",text="Grade -Sec")
        # self.attendanceReport_left.heading("Time",text="Time")
        # self.attendanceReport_left.heading("Date",text="Date")
        # self.attendanceReport_left.heading("Attend",text="Attend-status")
        # self.attendanceReport_left["show"]="headings"


        # # Set Width of Colums 
        # self.attendanceReport_left.column("ID",width=100)
        # self.attendanceReport_left.column("Name",width=100)
        # self.attendanceReport_left.column("Email",width=100)
        # self.attendanceReport_left.column("Time",width=100)
        # self.attendanceReport_left.column("Date",width=100)
        # self.attendanceReport_left.column("Attend",width=100)
        
        # self.attendanceReport_left.pack(fill=BOTH,expand=1)
        # self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================button section========================

        #Button Frame
        # btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        # btn_frame.place(x=10,y=390,width=635,height=60)

        #Improt button
        # save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        # save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        # update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        # update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        # del_btn=Button(btn_frame,command=self.action,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        # del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        


        return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)
        # Right section=======================================================



        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=150,width=1450,height=350)

        search_label  = Label(right_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.search_by_var = StringVar()
        self.search_by_var.set("Name")  # Set default value
        self.search_by_combo = ttk.Combobox(right_frame, textvariable=self.search_by_var, values=["Name", "Grade-Section"],width=14,font=("verdana",12,"bold"),state="readonly")
        self.search_by_combo.grid(row=3, column=1, padx=5)

        # Create a search bar
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(right_frame, textvariable=self.search_var, width=12, font=("verdana", 12, "bold"), bd=2, relief=GROOVE)
        self.search_entry.grid(row=3, column=2, padx=5)

        # Create a search button
       

        time_range_options = ["Daily", "Weekly", "Monthly"]
        self.time_range_var = ttk.Combobox(right_frame, values=time_range_options, state="readonly",width=13,font=("verdana",12,"bold"))
        self.time_range_var.set("Daily")  # Set a default value
        self.time_range_var.grid(row=3, column=3, padx=5)

        search_button = Button(right_frame, text="Search", command=self.search_data,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_button.grid(row=3, column=4, padx=5)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Name","Email","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="ID")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Email",text="Grade - Sec")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=100,anchor="center")
        self.attendanceReport.column("Name",width=100,anchor="center")
        self.attendanceReport.column("Email",width=100,anchor="center")
        self.attendanceReport.column("Time",width=100,anchor="center")
        self.attendanceReport.column("Date",width=100,anchor="center")
        self.attendanceReport.column("Attend",width=100,anchor="center")
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================
    #Update button
        btn_frame = Frame(main_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=22,y=535,width=1450,height=50)

        del_btn=Button(btn_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=2,column=1,padx=6,pady=10,sticky=W)
    #Update button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=2,column=2,padx=6,pady=10,sticky=W)
        
        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=2,column=3,padx=6,pady=10,sticky=W)

        pdf_btn = Button(btn_frame, command=self.generate_pdf, text="Generate PDF", width=12, font=("verdana", 12, "bold"),fg="white", bg="navyblue")
        pdf_btn.grid(row=2, column=4, padx=6, pady=10, sticky=W)

        showAll_btn=Button(btn_frame,command=self.fetch_data,text="Show All",width=12, font=("verdana", 12, "bold"),
                            fg="white", bg="navyblue")
        showAll_btn.grid(row=2,column=7,padx=5,pady=10,sticky=W)
        export_btn_right = Button(btn_frame, command=self.exportCsvRight, text="Export CSV", width=12, font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        export_btn_right.grid(row=2, column=8, padx=6, pady=10, sticky=W)
    # ===============================update function for mysql database=================
    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp
    
    def exportCsvRight(self):
        try:
            # Get the data from the right table (attendanceReport)
            right_table_data = []
            for item in self.attendanceReport.get_children():
                values = self.attendanceReport.item(item, 'values')
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


    def search_data(self):
        if self.search_var.get() == "":
            messagebox.showerror("Error", "Enter Name in the entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
                my_cursor = conn.cursor()

                # Update the SQL query to search by selected field (Name or Email) and time range
                field = self.search_by_var.get()
                time_range = self.time_range_var.get()
                if field == "Name":
                    sql = "SELECT std_id, std_name, Email, std_time, std_date, std_attendance FROM stdattendance WHERE std_name LIKE %s"
                else:
                    sql = "SELECT std_id, std_name, Email, std_time, std_date, std_attendance FROM stdattendance WHERE Email LIKE %s"

                # Modify the query based on the selected time range
                if time_range == "Daily":
                    sql += " AND DATE(std_date) = CURDATE()"
                elif time_range == "Weekly":
                    sql += " AND WEEK(std_date) = WEEK(CURDATE())"
                elif time_range == "Monthly":
                    sql += " AND MONTH(std_date) = MONTH(CURDATE())"

                params = (f"%{self.search_var.get()}%",)  # Use LIKE for partial matching
                my_cursor.execute(sql, params)

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.attendanceReport.delete(*self.attendanceReport.get_children())
                    for i in rows:
                        self.attendanceReport.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", "Data Not Found", parent=self.root)

                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    
    def update_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_name=%s,Email=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_id=%s"
                    val=(self.var_id.get(),)    
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
    # Get the current date
        # current_date = datetime.now().date()

        # Connect to the database
        conn = mysql.connector.connect(username='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()

        # Check if data for the current date already exists
        mycursor.execute("SELECT * FROM stdattendance")
        data = mycursor.fetchall()

        if len(data) != 0:
            # Clear the existing data in the treeview
            self.attendanceReport.delete(*self.attendanceReport.get_children())

            # Insert new data into the treeview
            for i in data:
                self.attendanceReport.insert("", END, values=i)

            # Commit the changes to the database
            conn.commit()

        # Close the database connection
        conn.close()


    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_email.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_email.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_id.get()=="" or self.var_name.get()==""or self.var_email.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_name.get(),
                self.var_email.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def generate_pdf(self):
        try:
            # Get the current data from the Treeview
            data = []
            for item in self.attendanceReport.get_children():
                values = self.attendanceReport.item(item, 'values')
                data.append(values)

            # Create a PDF file
            pdf_filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf")],
                title="Save PDF Report"
            )

            if pdf_filename:
                pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

                # Add a title to the PDF
                pdf_canvas.setFont("Helvetica-Bold", 16)
                pdf_canvas.drawCentredString(300, 750, "Attendance Report")  # Centered title

                # Add a table to the PDF with column headers
                col_widths = [80, 80, 80, 80, 80, 80]
                row_height = 20
                x = 100
                y = 720
                headers = ["ID", "Name", "Grade-Section", "Time", "Date", "Attend"]

                # Define a table style
                style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ])

                # Create a table with data and apply the style
                table_data = [headers] + data
                table = Table(table_data, colWidths=col_widths)
                table.setStyle(style)

                # Draw the table on the canvas
                table.wrapOn(pdf_canvas, 0, 0)
                table.drawOn(pdf_canvas, x, y - len(table_data) * row_height)

                # Save the PDF
                pdf_canvas.save()
                messagebox.showinfo("Success", "PDF generated successfully!", parent=self.root)

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found or permission denied.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error generating PDF: {str(es)}", parent=self.root)


def main():
    root = tk.Tk()
    app = Attendance(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()