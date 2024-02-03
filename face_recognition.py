# import re
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
import gspread
import tkinter as tk
from oauth2client.service_account import ServiceAccountCredentials


class Face_Recognition:

    def __init__(self, root, show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Face Recognition Pannel")
        # self.root.wm.iconbitmap('face.ico')

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
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1566,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

     


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\det1.jpg")
        std_img_btn=std_img_btn.resize((280,280),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=280,height=280)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=600,y=450,width=280,height=45)


        return_button = tk.Button(self.root, text="Return to MainApp", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="navyblue")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)
    #=====================Attendance===================

        scope = ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive.file',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_service.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open('Attendance_Sheets').sheet1

        # MySQL setup
        self.db_host = "localhost"
        self.db_user = "root"
        self.db_password = ""
        self.db_name = "face_recognition"
        self.connection = mysql.connector.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            database=self.db_name
        )
        self.cursor = self.connection.cursor()


    def mark_attendance(self, student_id, student_name, student_email):
        my_data_list = self.sheet.get_all_values()
        id_list = [entry[0] for entry in my_data_list]

        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # Check if attendance for the current day already exists in Google Sheets
        existing_entries = [index for index, entry in enumerate(my_data_list) if entry[0] == student_id]

        if existing_entries:
            last_entry_index = existing_entries[-1]
            last_entry_date = my_data_list[last_entry_index][4]  # Assuming the date is in the fifth column

            if last_entry_date == current_date:
                print("Attendance already marked for the current day.")
                return

        # Insert new attendance entry if it doesn't exist for the current day
        new_row = [student_id, student_name, student_email, current_time, current_date, "Present"]
        self.sheet.append_row(new_row)

        # Insert into the database
        query_insert = "INSERT INTO stdattendance (std_id, std_name, Email, std_time, std_date, std_attendance) VALUES (%s, %s, %s, %s, %s, %s)"
        data_insert = (student_id, student_name, student_email, current_time, current_date, "Present")

        try:
            self.cursor.execute(query_insert, data_insert)
            self.connection.commit()
            print("Attendance marked and inserted into Google Sheets and the database for the current day.")
        except Exception as e:
            print(f"Error inserting into the database: {e}")

    # Usage example:
    # mark_attendance(self, "123", "John Doe")


    def __del__(self):
        # Close the cursor and connection in the destructor
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection closed.")

    # def mark_attendance(self,i,n):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDatalist=f.readlines()
    #         name_list=[]
    #         for line in myDatalist:
    #             entry=line.split((","))
    #             name_list.append(entry[0])

    #         if((i not in name_list))  and ((n not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i}, {n}, {dtString}, {d1}, Present")

    #================face recognition==================

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp
    
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition')
                cursor = conn.cursor()

                cursor.execute("select Name,lname from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n=" ".join(n)

                cursor.execute("select Email from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Grade-Sec:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")
        videoCap=cv2.VideoCapture(0)

        try:
            while True:
                ret, img = videoCap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Detector",img)

                if cv2.waitKey(1) == 13:
                    break
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            videoCap.release()
            cv2.destroyAllWindows()




def main():
    root = tk.Tk()
    app = Face_Recognition(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()