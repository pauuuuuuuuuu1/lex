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

        # def grab_date():
        #     student_dob_entry = cal.get_date()
        #     print("Selected Date:", student_dob_entry)
        #     # Add your logic to handle the selected date as needed
        #     date_window.destroy()

     

        # Assuming you have a delete_window somewhere else in your code
        # and you want to destroy it, you can add a function like this:
            

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
        search_frame = LabelFrame(right_frame,bd=2,bg="#FAF9F6",relief=RIDGE,text="Information",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=1450,height=80)

        #search
        self.search_entry = Entry(search_frame,width=30,font=("arial",14))
        self.search_entry.grid(row=0,column=2,padx=15,pady=10,sticky=W)
        
        
        self.search_entry.bind("<KeyRelease>", lambda event: self.search_data())
        self.search_entry.insert(0, "Search ...")
        self.search_entry.bind("<FocusIn>", self.ons_entry_click)
        self.search_entry.bind("<FocusOut>", self.ons_focus_out)


        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="#003D60")
        showAll_btn.grid(row=0,column=4,padx=10,pady=10,sticky=W)

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
        self.student_table.bind("<ButtonRelease>",self.get_student_cursor)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


   

# ==================Function Decleration==============================
    def search_student_data(self):
        search_query = self.search_entry.get()
        self.autocomplete_student(search_query)

    def autocomplete_student(self, search_query):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT Name, Roll_No FROM regteach WHERE Name LIKE %s OR Roll_No LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()
        conn.close()


    def ons_entry_click(self, event):
        if self.search_entry.get() == "Search ...":
            self.search_entry.delete(0, "end")
            self.search_entry.config(fg='black')  # Change text color to black

    def ons_focus_out(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search ...")
            self.search_entry.config(fg='grey')


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

    def add_data(self):
       
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_mname.get()=="" or self.var_std_lname.get()=="" or self.var_div.get()=="" or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_std_mname.get(),
                self.var_std_lname.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))
                
                
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
                logging.info(f"User added data for Student ID: {self.var_std_id.get()}")
            except Exception as es:
                logging.error(f"Error during data addition: {str(es)}")
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:

            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================
    def get_cursor(self, event=""):
            cursor_focus = self.student_table()
            content = self.student_table.item(cursor_focus)
            data = content["values"]

            self.var_std_id.set(data[0])


    def get_student_cursor(self, event=""):
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

        # Check if var_radio1 is "Yes" and enable the button accordingly




    # ========================================Update Function==========================
    def update_data(self):
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_std_mname.get()=="" or self.var_std_lname.get()=="" or   self.var_div.get()=="" or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,mName=%s,lName=%s,Division=%s,Gender=%s,DOB=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_std_mname.get(),
                    self.var_std_lname.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                logging.info(f"User updated data for Student ID: {self.var_std_id.get()}")
            except Exception as es:
                logging.error(f"Error during data update: {str(es)}")
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
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
        self.var_teacher.set("")
    
    # ===========================Search Data===================


    def search_data(self):
        search_query = self.search_entry.get()

        # Check if search query is empty
     

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM student WHERE Name LIKE %s OR mname LIKE %s OR lname LIKE %s OR Division LIKE %s OR Gender LIKE %s OR DOB LIKE %s OR Address LIKE %s OR Roll_No LIKE %s OR Email LIKE %s OR Teacher_Name LIKE %s", 
        ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%','%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=tuple(row)) # insert the updated row back as a tuple
            conn.commit()
       

        conn.close()




#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_roll.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Name=%s,mName=%s,lName=%s,Division=%s,Gender=%s,DOB=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_std_mname.get(),
                    self.var_std_lname.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
                logging.info(f"User generated dataset for Student ID: {self.var_std_id.get()}")
            except Exception as es:
                logging.error(f"Error during dataset generation: {str(es)}")
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 




def main():
    root = tk.Tk()
    app = Student_view(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()