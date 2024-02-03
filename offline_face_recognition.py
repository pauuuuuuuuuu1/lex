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
import csv
import tkinter as tk    

class OFFline_face_recognition:
    def __init__(self,root,show_main_app_callback):
        self.root=root
        self.root.geometry("1566x768+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.attributes('-fullscreen',True)
        # This part is image labels setting start 
        
        # backgorund image 
        bg1=Image.open(r"Images_GUI\offline.jpg")
        bg1=bg1.resize((1566,850),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\det1.jpg")
        std_img_btn=std_img_btn.resize((280,280),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=310,width=280,height=280)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("arial",15,"bold"),bg="#003D60",fg="white")
        std_b1_1.place(x=600,y=600,width=280,height=45)

        return_button = tk.Button(self.root, text="Return to Dashboard", command=show_main_app_callback, font=("verdana",12,"bold"),fg="white", bg="#003D60")
        return_button.grid(row=0,column=1,padx=15,pady=820,sticky=W)
        # create function for button 

    def return_to_main_app(self):
        self.master.withdraw()  # Hide the child window
        if hasattr(self, 'show_main_app_callback') and callable(self.show_main_app_callback):
            self.show_main_app_callback()  # Call the callback to show MainApp

    #=====================Attendance===================

    # def mark_attendance(self,i,n):
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDatalist=f.readlines()
    #         name_list=[]
    #         for line in myDatalist:
    #             entry=line.split((","))
    #             name_list.append(entry[0])

    #         if((i not in name_list)) and ((n not in name_list)):
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i}, {n}, {dtString}, {d1}, Present")



    

    def mark_attendance(self, i, n, r, attendance_date=None):
        # Use the provided date or default to the current date
        if attendance_date is None:
            attendance_date = datetime.now().strftime("%Y-%m-%d")

        # Check if attendance has already been marked for today in CSV file
        with open("attendance.csv", "r") as file:
            lines = file.readlines()
            for line in reversed(lines):
                if f"{i}, {n}, {r}" in line and "Present" in line and attendance_date in line:
                    print(f"Attendance already marked for student {i} on {attendance_date}.")
                    return

        # Check if attendance has already been marked for today in MySQL database
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='face_recognition'
        )
        cursor = db_connection.cursor()

        check_query = "SELECT * FROM stdattendance WHERE std_id = %s AND std_date = %s AND std_attendance = 'Present'"
        check_values = (i, attendance_date)
        cursor.execute(check_query, check_values)

        if cursor.fetchone():
            print(f"Attendance already marked for student {i} on {attendance_date} in the database.")
            cursor.close()
            db_connection.close()
            return

        # Update the CSV file
        with open("attendance.csv", "a", newline="\n") as f:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.write(f"\n{i}, {n}, {r}, {dtString}, {attendance_date}, Present")

        # Insert data into MySQL database
        query = "INSERT INTO stdattendance (std_id, std_name, Email, std_time, std_date, std_attendance) VALUES (%s,%s, %s, %s, %s, %s)"
        values = (i, n, r, dtString, attendance_date, "Present")

        cursor.execute(query, values)

        db_connection.commit()
        cursor.close()
        db_connection.close()




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

                confidence=int((100*(1-predict/600)))

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
                    # cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Student",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

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
    app = OFFline_face_recognition(root, None)
    root.mainloop()

if __name__ == "__main__":
    main()