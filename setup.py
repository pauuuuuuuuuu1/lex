# from cx_Freeze import setup,Executable
# import sys
# import os
# base = None

# if sys.platform == 'win32':
#     base = "Win32GUI"

# os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python312\tcl\tcl8.6"
# os.environ['TK_LIBRARY'] = r"C:\Program Files\Python312\tcl\tk8.6"

# executables = [Executable("face_recognition.py", base=base, icon="face.ico")]


# setup(
#     name = "Python-FYP-Face-Recognition-Attendence-System",
#     options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'Images_GUI','data_img','Database','attendance']}},
#     version = "1.0",
#     description = "Face Recognition Automatic Attendace System | Developed By Kumon",
#     executables = executables
#     )
