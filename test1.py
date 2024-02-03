import tkinter as tk
from tkinter import ttk

class YourApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Your Application")

        self.var_radio1 = tk.StringVar()
        self.take_photo_btn = tk.Button(self.root, command=self.generate_dataset, text="Take Pic", width=9,
                                       font=("verdana", 12, "bold"), fg="white", bg="navyblue", state=tk.DISABLED)

        class_Student_frame = ttk.Frame(self.root)
        class_Student_frame.grid(row=0, column=0, padx=10, pady=10)

        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes",
                                    command=self.enable_button)
        radiobtn1.grid(row=7, column=0, padx=15, pady=20, sticky=tk.W)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, text="No Photo Sample", variable=self.var_radio1, value="No",
                                    command=self.disable_button)
        radiobtn2.grid(row=7, column=1, padx=15, pady=80, sticky=tk.W)

        submit_button = ttk.Button(class_Student_frame, text="Submit", command=self.perform_action)
        submit_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.take_photo_btn.grid(row=0, column=4, padx=10, pady=10, sticky=tk.W)

    def enable_button(self):
        self.take_photo_btn["state"] = tk.NORMAL

    def disable_button(self):
        self.take_photo_btn["state"] = tk.DISABLED

    def perform_action(self):
        selected_option = self.var_radio1.get()

        if selected_option == "Yes":
            # Call a function or perform actions for "Take Photo Sample" option
            print("Take Photo Sample selected")
        elif selected_option == "No":
            # Call a function or perform actions for "No Photo Sample" option
            print("No Photo Sample selected")
        else:
            # Handle other cases if needed
            print("Unknown option selected")

    def generate_dataset(self):
        # Add your logic for the 'Take Pic' button functionality here
        print("Take Pic button clicked")

    def run(self):
        self.root.mainloop()

# Instantiate your application
app = YourApp()

# Run the application
app.run()
