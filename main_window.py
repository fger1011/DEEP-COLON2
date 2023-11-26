import tkinter as tk
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import core.utils as utils
from absl.flags import FLAGS
import database
from tkinter import font


def display_latest_record():

    canvas_patient_details = tk.Canvas(rightFrame, width=50, height=200)
    canvas_patient_details.grid(row=0, column=1, padx=1, pady=1, sticky=tk.NSEW)

    # Fetch the latest record from the database
    document = database.get_latest_record()

    # Extract the fields from the document
    firstname = document['firstname']
    lastname = document['lastname']
    birthday = document['birthday']
    age = document['age']
    sex = document['sex']
    address = document['address']
    contact_number = document['contact_number']
    emergency_contact_name = document['emergency_contact_name']
    emergency_contact_number = document['emergency_contact_number']
    marital_status = document['marital_status']

    custom_font = font.Font(family="Arial", size=12)

    # Create labels and display the data
    firstname_label = tk.Label(canvas_patient_details, text="\n\n\n\n\nFirst Name: {}".format(firstname), font=custom_font)
    firstname_label.grid(row=0, column=0, padx=10, pady=2)

    lastname_label = tk.Label(canvas_patient_details, text="Last Name: {}".format(lastname), font=custom_font)
    lastname_label.grid(row=1, column=0, padx=20, pady=2)

    birthday_label = tk.Label(canvas_patient_details, text="Birthday: {}".format(birthday), font=custom_font)
    birthday_label.grid(row=2, column=0, padx=20, pady=2)

    age_label = tk.Label(canvas_patient_details, text="Age: {}".format(age), font=custom_font)
    age_label.grid(row=3, column=0, padx=20, pady=2)

    sex_label = tk.Label(canvas_patient_details, text="Sex: {}".format(sex), font=custom_font)
    sex_label.grid(row=4, column=0, padx=20, pady=2)

    address_label = tk.Label(canvas_patient_details, text="Address: {}".format(address), font=custom_font)
    address_label.grid(row=5, column=0, padx=20, pady=2)

    contact_number_label = tk.Label(canvas_patient_details, text="Contact Number: {}".format(contact_number), font=custom_font)
    contact_number_label.grid(row=6, column=0, padx=20, pady=2)

    emergency_contact_name_label = tk.Label(canvas_patient_details,text="Emergency Contact Name: {}".format(emergency_contact_name), font=custom_font)
    emergency_contact_name_label.grid(row=7, column=0, padx=20, pady=2)

    emergency_contact_number_label = tk.Label(canvas_patient_details,text="Emergency Contact Number: {}".format(emergency_contact_number), font=custom_font)
    emergency_contact_number_label.grid(row=8, column=0, padx=20, pady=2)

    marital_status_label = tk.Label(canvas_patient_details, text="Marital Status: {}".format(marital_status), font=custom_font)
    marital_status_label.grid(row=9, column=0, padx=10, pady=2)


root = tk.Tk() # Makes the window
root.wm_title("Main Window") # Makes the title that will appear in the top left
root.state('zoomed')
root.geometry("1000x600")
root.config(bg="#2c3e50")


# Configure grid to center widgets
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Put widgets here

# Right Frame and its contents
rightFrame = tk.Frame(root, width=200, height=600)
rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky=tk.NSEW)
rightFrame.config(bg="#2c3e50")


btnFrame = tk.Frame(rightFrame, width=700, height=200)
btnFrame.grid(row=1, column=0, padx=8, pady=2, sticky=tk.NSEW)
btnFrame.config(bg="#2c3e50")

#Create the playback buttons

length_label = tk.Label(btnFrame, text="Video Length: 0/0")
length_label.grid(row=1, column=0, columnspan=2, padx=10, pady=2)



# Expand left and right frames vertically and horizontally
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


display_latest_record()

