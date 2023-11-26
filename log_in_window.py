import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient
from ttkthemes import ThemedStyle
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime



# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')
db = client['login']
collection = db['login_history']

# Check if the user "Gastro-001" already exists in the database
user = db.users.find_one({'username': 'Gastro-001'})

# If the user "Gastro-001" doesn't exist, add them to the database
if not user:
    db.users.insert_one({'username': 'Gastro-001', 'password': 'gastroenterologist'})


def log_login(username, success):
    # Get the current timestamp
    timestamp = datetime.datetime.now()

    # Create a log entry for the login attempt
    log_entry = {
        'username': username,
        'timestamp': timestamp,
        'success': success
    }

    # Insert the log entry into the database
    db.login_history.insert_one(log_entry)



def check_credentials():
    # Get the users from the input fields
    username = username_input.get()
    password = password_input.get()

    # Check if the username and password match any records
    user = db.users.find_one({'username': username, 'password': password})

    # If the username and password are correct
    if user:
        message_label.config(text="Login successful!", foreground="green")
        password_input.delete(0, tk.END)  # Clear the password entry field

        # Call log_login() function to log the successful login
        log_login(username, True)

        # Go to window module
        home_window()
    else:
        messagebox.showerror(title="Wrong", message="Wrong Username or Password")



def home_window():
    window.destroy()
    import home_window  # Import and run the searchbar module

def resize_image():
    # Get the size of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Resize the image to fit the screen
    resized_image = original_image.resize((screen_width, screen_height))

    # Decrease the opacity of the image
    resized_image = resized_image.convert("RGBA")
    data = resized_image.getdata()

    new_data = []
    for item in data:
        # Set the alpha value to 50% (128 out of 255)
        new_data.append((item[0], item[1], item[2], 128))

    resized_image.putdata(new_data)

    # Convert the resized image to Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(resized_image)

    # Update the image displayed in the label
    label.config(image=image_tk)
    label.image = image_tk  # Keep a reference to the resized image


######################################################################################  Create the main window  #########################################################################
window = tk.Tk()
window.title("Log in Window")
window.geometry('700x600')


# Create a themed style for the window
style = ThemedStyle(window)

original_image = Image.open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\mdi.jpg")

# Create a label widget
label = tk.Label(window)
label.pack(fill=tk.BOTH, expand=True)

# Configure the window to be full screen
window.state('zoomed')


# Call the resize_image function to resize the image to fit the full screen
resize_image()


# Create the login frame
login_frame = ttk.Frame(window)
login_frame.pack(pady=100)

# Create the username input
username_label = ttk.Label(login_frame, text="Username:", font=("TkDefaultFont", 14))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_input = ttk.Entry(login_frame)
username_input.grid(row=0, column=1, padx=10, pady=10)



# Create the password input
password_label = ttk.Label(login_frame, text="Password:", font=("TkDefaultFont", 14))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_input = ttk.Entry(login_frame, show="*")
password_input.grid(row=1, column=1, padx=10, pady=10)

style.configure("Custom.TButton", font=("TkDefaultFont", 14))

# Create the button with the custom style
login_button = ttk.Button(login_frame, text="Login", command=check_credentials, style="Custom.TButton")
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='WE')


# Create the message
message_label = ttk.Label(window, text="", font=('Helvetica', 12))
message_label.pack()

# Center the login frame
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Run the application
window.mainloop()
