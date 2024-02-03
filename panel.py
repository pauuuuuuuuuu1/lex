from tkinter import* 
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkcalendar import *
from tkinter import ttk
from tkinter import Tk
from register import Register
from tkinter import PhotoImage



# Connect to MySQL database
conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
cursor = conn.cursor()

class AdminPanel:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Student Pannel")
        self.root.attributes('-fullscreen',True)
        self.var_std_id=StringVar()
        self.var_employee_id=StringVar()
        self.var_teacher_id=StringVar()
        self.var_fname=StringVar()
        self.var_mname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_dep=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        # self.var_thr_id=StringVar()
        
        

 # This part is image labels setting start 
         # backgorund image 
        bg1=Image.open(r"Images_GUI\tccover.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

       

        # Creating Frame  
        main_frame = Frame(bg_img,bd=2,bg="lightgray") #bd mean border 
        main_frame.place(x=15,y=165,width=1500,height=640)
        
           
        return_button = Button(self.root, text="LOGOUT", command=show_main_app_callback,
                               font=("verdana", 12, "bold"), fg="white", bg="#003D60")
        return_button.grid(row=0, column=1, padx=15, pady=820, sticky=W)
        


        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Teacher Information",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=1470,height=610)

        # data table
        left_table_frame = Frame(left_frame,bd=2,bg="black",relief=RIDGE)
        left_table_frame.place(x=10,y=100,width=1445,height=430)

        self.del_teacher_btn = Button(left_frame,command=self.teacher_delete_data, text="Delete", width=7, font=("verdana", 12, "bold"), fg="white", bg="#003D60", state=DISABLED)
        self.del_teacher_btn.place(x=1300, y=540, width=155, height=40)
        
        # update table
        teacher_table_frame = Frame(main_frame,bd=2,bg="white",relief=RIDGE)
        teacher_table_frame.place(x=25,y=40,width=1440,height=70)
        
        self.teacher_id_entry = Entry(teacher_table_frame, textvariable=self.var_teacher_id, font=("verdana", 11), bd=2, relief=GROOVE)
        self.teacher_id_entry.grid_remove()
        
        # employee ID
        self.teacher_employee_id_label = Label(teacher_table_frame,text="Employee ID:",font=("arial",12,"bold"),fg="navyblue",bg="#FAF9F6")
        self.teacher_employee_id_label.place(x=15,y=25)
        
        self.employee_id_entry = Entry(teacher_table_frame, textvariable=self.var_employee_id, font=("arial", 11), bd=2, relief=GROOVE, state="readonly")     
        self.employee_id_entry.place(x=130,y=25, width=200, height=30)
        
        # department
        self.dep_combobox_label = Label(teacher_table_frame,text="Department:",font=("arial",12,"bold"),fg="navyblue",bg="#FAF9F6")
        self.dep_combobox_label.place(x=340,y=25)
        
        self.dep_combobox = ttk.Combobox(teacher_table_frame, textvariable=self.var_dep, font=("verdana", 11), state="readonly")
        self.dep_combobox.place(x=450,y=25, width=200, height=30)

        # Set values for the Combobox (replace these with your actual department values)
        department_values = ["Elementary", "High - School"]
        self.dep_combobox['values'] = department_values

        self.dep_combobox.set("Select Department")
        
        # update button
        self.teacher_update_btn = Button(teacher_table_frame, text="UPDATE", command=self.update_teacher_data, font=("verdana", 12, "bold"), fg="white", bg="#003D60")
        self.teacher_update_btn.place(x=670, y=25, width=155, height=30)
        
        # search
        self.teacher_search_entry = Entry(teacher_table_frame, font=("verdana", 11), bd=2, relief=GROOVE)
        self.teacher_search_entry.place(x=930, y=17, width=500, height=40)
        
        self.teacher_search_entry.bind("<KeyRelease>", lambda event: self.search_teacher_data())
        self.teacher_search_entry.insert(0, "Search ...")
        self.teacher_search_entry.bind("<FocusIn>", self.ons_entry_click)
        self.teacher_search_entry.bind("<FocusOut>", self.ons_focus_out)
        
        # # first name
        # self.teacher_fname_entry_label = Label(teacher_table_frame,text="First Name:",font=("arial",11,"bold"),fg="navyblue",bg="#FAF9F6")
        # self.teacher_fname_entry_label.place(x=15,y=50,)
        
        # self.fname_entry = Entry(teacher_table_frame, textvariable=self.var_fname, font=("arial", 10), bd=2, relief=GROOVE)
        # self.fname_entry.place(x=140,y=50, width=200)
        
        # # middle name
        # self.teacher_mname_entry_label = Label(teacher_table_frame,text="Middle Name:",font=("arial",11,"bold"),fg="navyblue",bg="#FAF9F6")
        # self.teacher_mname_entry_label.place(x=15,y=90)
        
        # self.mname_entry = Entry(teacher_table_frame, textvariable=self.var_mname, font=("arial", 10), bd=2, relief=GROOVE)
        # self.mname_entry.place(x=140,y=90, width=200)
        
        # # last name
        # self.teacher_lname_entry_label = Label(teacher_table_frame,text="Last Name:",font=("arial",11,"bold"),fg="navyblue",bg="#FAF9F6")
        # self.teacher_lname_entry_label.place(x=15,y=115)
        
        # self.lname_entry = Entry(teacher_table_frame, textvariable=self.var_lname, font=("arial", 10), bd=2, relief=GROOVE)
        # self.lname_entry.place(x=140,y=115, width=200)
        
        # # email
        # self.email_entry_label = Label(teacher_table_frame,text="Email:",font=("arial",11,"bold"),fg="navyblue",bg="#FAF9F6")
        # self.email_entry_label.place(x=500,y=90)
        
        # self.email_entry = Entry(teacher_table_frame, textvariable=self.var_email, font=("verdana", 11), bd=2, relief=GROOVE)
        # self.email_entry.place(x=600,y=90, width=200)
        
        # contact number
        # self.cnum_entry = Entry(teacher_table_frame, textvariable=self.var_cnum, font=("verdana", 11), bd=2, relief=GROOVE)
        # self.cnum_entry.grid(row=2,column=2,padx=15,pady=15,sticky=W)
        
        # end of update table
        

        self.teacher_search_btn = Button(left_frame, text="Register", command=self.open_windows2, font=("verdana", 12, "bold"), fg="white", bg="#003D60")
        self.teacher_search_btn.place(x=55, y=540, width=155, height=40)

        showAll_btn=Button(left_frame,command=self.teacher_fetch_data,text="Show All",width=12, font=("verdana", 12, "bold"),
                            fg="white", bg="#003D60")
        showAll_btn.place(x=215, y=540, width=155, height=40)
        
       # refresh button
        refresh_img_btn = Image.open(r"Images_GUI/refresh.png")
        refresh_img_btn = refresh_img_btn.resize((40, 25), Image.LANCZOS)
        self.refresh_img1 = ImageTk.PhotoImage(refresh_img_btn)

        refresh_btn = Button(
            left_frame, 
            image=self.refresh_img1,
            command=self.teacher_refresh_data, 
            compound="center",
            font=("verdana", 12, "bold"),
            fg="black", 
            bg="#003D60"
        )

        refresh_btn.place(x=10, y=540, width=40, height=40)

# Store reference to the image to prevent garbage

        
        scroll_x = ttk.Scrollbar(left_table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(left_table_frame,orient=VERTICAL)
        
        #create table 
        style = ttk.Style()
        style.configure('Treeview', font=('Arial', 10), rowheight=25)
        style.configure('Treeview.Heading', font=('Arial', 12, "bold"), rowheight=25)

        self.teacher_table = ttk.Treeview(left_table_frame, style='Treeview', column=("id","employee_id","fname","mname","lname","cnum","email","department","ssq","sa","pwd"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.teacher_table.xview)
        scroll_y.config(command=self.teacher_table.yview)

        self.teacher_table.heading("id",text="Teacher ID")
        self.teacher_table.heading("employee_id",text="Employee ID")
        self.teacher_table.heading("fname",text="First Name")
        self.teacher_table.heading("mname",text="Middle Name")
        self.teacher_table.heading("lname",text="Last Name")
        self.teacher_table.heading("cnum",text="Number")
        self.teacher_table.heading("email",text="Email")
        self.teacher_table.heading("department",text="Department")
        self.teacher_table.heading("ssq",text="Security Question")
        self.teacher_table.heading("sa",text="Answer")
        self.teacher_table.heading("pwd",text="Password")
        self.teacher_table["show"]="headings"


        # Set Width of Colums 
        self.teacher_table.column("id",width=90, anchor="center")
        self.teacher_table.column("employee_id",width=90, anchor="center")
        self.teacher_table.column("fname",width=90, anchor="center")
        self.teacher_table.column("mname",width=90, anchor="center")
        self.teacher_table.column("lname",width=90, anchor="center")
        self.teacher_table.column("cnum",width=120, anchor="center")
        self.teacher_table.column("email",width=130, anchor="center")
        self.teacher_table.column("department",width=130, anchor="center")
        self.teacher_table.column("ssq",width=130, anchor="center")
        self.teacher_table.column("sa",width=100, anchor="center")
        self.teacher_table.column("pwd",width=70, anchor="center")

    


        self.teacher_table.pack(fill=BOTH,expand=1)
        self.teacher_table.bind("<ButtonRelease>",self.get_cursor)
        self.teacher_table.bind("<ButtonRelease>",self.get_teacher_cursor)
        self.teacher_fetch_data()

        
    def teacher_refresh_data(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = AdminPanel(self.window1, self.show_main_app)
      
      
    def search_teacher_data(self):
        search_query = self.teacher_search_entry.get()
        self.autocomplete_teacher(search_query)


    def autocomplete_teacher(self, search_query):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT fname, lname FROM regteach WHERE fname LIKE %s OR lname LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()
        conn.close()

        suggestions = [f"{row[0]} {row[1]}" for row in data]
        self.teacher_search_entry.config(completevalues=suggestions)


        suggestions = [f"{row[0]} {row[1]}" for row in data]
        self.student_search_entry.config(completevalues=suggestions)
        

   
    def get_cursor(self, event=""):
        cursor_focus = self.teacher_table.focus()
        content = self.teacher_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0])
        self.del_teacher_btn['state'] = tk.NORMAL
        
    def get_cursor1(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0])
        self.teacher_delete_data['state'] = tk.NORMAL
    
    
    def teacher_fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
        mycursor = conn.cursor()

        mycursor.execute("select * from regteach")
        data=mycursor.fetchall()

        if len(data)!= 0:

            self.teacher_table.delete(*self.teacher_table.get_children())

            for row in data:
                row = list(row)  # Convert the row to a list to make it mutable
                row[-1] = "********"   # Replace the password with '*' assuming 'pwd' is the last column
                row[-2] = "***"

                self.teacher_table.insert("", END, values=row)
            conn.commit()
            self.del_teacher_btn['state'] = tk.DISABLED
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
        if self.teacher_search_entry.get() == "Search ...":
            self.teacher_search_entry.delete(0, "end")
            self.teacher_search_entry.config(fg='black')  # Change text color to black

    def ons_focus_out(self, event):
        if not self.teacher_search_entry.get():
            self.teacher_search_entry.insert(0, "Search ...")
            self.teacher_search_entry.config(fg='grey')

    def clear_inputs(self):
        self.admintxtuser.delete(0, 'end')  
        self.admintxtpwd.delete(0, 'end')

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        self.clear_inputs()  # Call the function to clear inputs
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

    # All your other code...
            
            
        
    def open_windows2(self):
        self.root.withdraw()
        self.window1 = tk.Toplevel(self.root)
        self.disable_close_button(self.window1)
        self.app1 = Register(self.window1, self.show_main_app)
    
    

    def disable_close_button(self, window): 
        window.protocol("WM_DELETE_WINDOW", lambda: None)  # Do nothing when close button is clicked

    def show_main_app(self):
        self.root.deiconify()  # Show the main window
        # Destroy child windows when returning to MainApp
        if hasattr(self, 'window2'):
            self.window1.destroy()
        
            
    
    def search_teacher_data(self):
        search_query = self.teacher_search_entry.get()

        # Check if search query is empty
     

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM regteach WHERE fname LIKE %s OR mname LIKE %s OR lname LIKE %s OR employee_id LIKE %s OR department LIKE %s", 
        ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
        data = mycursor.fetchall()

        if len(data) != 0:
            self.teacher_table.delete(*self.teacher_table.get_children())
            for row in data:
                row = list(row)  # Convert the row to a list to make it mutable
                row[-1] = "********"   # Replace the password with '*'
                row[-2] = "***" # Replace the second last column with '*' as needed
                self.teacher_table.insert("", END, values=tuple(row)) # insert the updated row back as a tuple
            self.del_student_btn['state'] = tk.DISABLED
            conn.commit()
       

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
                self.del_teacher_btn['state'] = tk.DISABLED
                messagebox.showinfo("Delete", "Teacher record deleted successfully!", parent=self.root)
                
        except Exception as es:
            messagebox.showerror("Error", f"Error deleting teacher record: {str(es)}", parent=self.root)
   
    def get_teacher_cursor(self, event=""):
        cursor_focus = self.teacher_table.focus()
        content = self.teacher_table.item(cursor_focus)
        data = content["values"]

        self.var_teacher_id.set(data[0])
        self.var_employee_id.set(data[1])
        self.var_fname.set(data[2])
        self.var_mname.set(data[3])
        self.var_lname.set(data[4])
        self.var_cnum.set(data[5])
        self.var_email.set(data[6])
        self.var_dep.set(data[7])

        self.del_teacher_btn['state'] = tk.NORMAL
        
    def update_teacher_data(self):
        teacher_id = self.var_teacher_id.get()
        employee_id = self.var_employee_id.get()
        fname = self.var_fname.get()
        mname = self.var_mname.get()
        lname = self.var_lname.get()
        cnum = self.var_cnum.get()
        email = self.var_email.get()
        dep = self.var_dep.get()

        if not teacher_id or not employee_id or not fname or not lname or not cnum or not email or not dep or not mname:
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition')
            mycursor = conn.cursor()
            sql = "UPDATE regteach SET fname=%s, mname=%s,  lname=%s, cnum=%s, email=%s, department=%s, employee_id=%s WHERE id=%s"
            val = (fname, mname, lname, cnum, email, dep, employee_id, teacher_id)
            mycursor.execute(sql, val)
            conn.commit()
            conn.close()
            self.teacher_fetch_data()
            self.del_teacher_btn['state'] = tk.DISABLED
            messagebox.showinfo("Success", "Teacher record updated successfully!", parent=self.root)

            # Clear the Entry widgets after update
            self.var_teacher_id.set("")
            self.var_employee_id.set("")
            self.var_fname.set("")
            self.var_mname.set("")
            self.var_lname.set("")
            self.var_cnum.set("")
            self.var_email.set("")
            self.var_dep.set("")

        except Exception as es:
            messagebox.showerror("Error", f"Error updating teacher record: {str(es)}", parent=self.root)
            
            
    


def main():
    root = tk.Tk()
    app = AdminPanel(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()
