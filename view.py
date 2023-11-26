import tkinter as tk
from tkinter import messagebox
import subprocess
import cv2
from get_loader import Vocabulary
from model import CNNtoRNN
import os
import datetime
from PIL import Image, ImageTk
from pdf_file import download_pdf_report


from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import core.utils as utils
from absl.flags import FLAGS


import torch
import torchvision.transforms as transforms
import database
from tkinter import font, filedialog
from pymongo import MongoClient


# Global variables
is_playing = False
current_frame = None

video_path = None
processed_video_path = None

videoCanvas = None
cap = None
total_frames = 0
length_label = None
seek_scale = None
is_paused = False
vocab = Vocabulary.load_vocab("vocab.json")
client = MongoClient('mongodb://localhost:27017')
db = client['registration']
collection = db['patients']

# Hyperparameters
embed_size = 256
hidden_size = 256
num_layers = 1

# Calculate the vocabulary size based on the dataset
vocab_size = len(vocab)

# Define the model architecture
model = CNNtoRNN(embed_size, hidden_size, vocab_size, num_layers)

# Load the trained model checkpoint
checkpoint = torch.load("my_checkpoint.pth")


# Update the model's state dictionary to match the checkpoint
model_dict = model.state_dict()
checkpoint_dict = checkpoint["state_dict"]


# Remove the incompatible keys from the checkpoint
checkpoint_dict = {k: v for k, v in checkpoint_dict.items() if k in model_dict}

# Load the updated state dictionary into the model
model_dict.update(checkpoint_dict)
model.load_state_dict(model_dict)

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])



def open_file():
    global video_path, cap
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    cap = cv2.VideoCapture(video_path)
    if video_path:
        update_time_frame()
        process_video(video_path)


def process_video(video_path):

    global processed_video_path, total_frames, file_path

    # Define the output video path
    output_dir = "./process_videos"
    os.makedirs(output_dir, exist_ok=True)
    video_filename = os.path.basename(video_path)
    processed_video_path = os.path.join(output_dir, video_filename)



    # Run the object_tracker.py script as a subprocess, passing the video path and output video path as arguments

    # command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--model', 'yolov4']
    # subprocess.run(command)

    # os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Replace '0' with the GPU device index you want to use
    # Path to the save_model.py script
    save_model_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\save_model.py"

    # Path to the weights file
    weights_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\data\yolov4.weights"

    # Command to run the save_model.py script
    command = [
        'python',
        save_model_path,
        '--weights', weights_path,
        '--output', './checkpoints/yolov4-tiny-416',
        '--model', 'yolov4',
        '--tiny'
    ]

    # Execute the command to run the save_model.py script
    subprocess.run(command)

    command = ['python', 'object_tracker.py', '--video', video_path, '--output', processed_video_path, '--weights',
               './checkpoints/yolov4-tiny-416', '--model', 'yolov4']

    subprocess.run(command)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    if os.path.basename(video_path) == "cabading.mp4":
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\images\cabading"
        play_video()
        display_screenshots(folder_path)
        file_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Cabading.txt"
        try:
            with open(file_path, "r") as file:
                saved_text = file.read()
                commentLog.insert("1.0", saved_text)  # Insert the saved text
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass
        save_button = tk.Button(rightFrame, text="Save", image=save_image, command=lambda: save_text(file_path))
        save_button.grid(row=1, column=1, columnspan=2, padx=80, pady=2)

    elif os.path.basename(video_path) == "cadelina.mp4":
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\images\cadelina"
        play_video()
        display_screenshots(folder_path)
        file_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Cadelina.txt"
        try:
            with open(file_path, "r") as file:
                saved_text = file.read()
                commentLog.insert("1.0", saved_text)  # Insert the saved text
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass
        save_button = tk.Button(rightFrame, text="Save", image=save_image, command=lambda: save_text(file_path))
        save_button.grid(row=1, column=1, columnspan=2, padx=80, pady=2)

    elif os.path.basename(video_path) == "lijauco.mp4":
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\images\lijauco"
        play_video()
        display_screenshots(folder_path)
        file_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Lijuaco.txt"
        try:
            with open(file_path, "r") as file:
                saved_text = file.read()
                commentLog.insert("1.0", saved_text)  # Insert the saved text
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass
        save_button = tk.Button(rightFrame, text="Save", image=save_image, command=lambda: save_text(file_path))
        save_button.grid(row=1, column=1, columnspan=2, padx=80, pady=2)

    elif os.path.basename(video_path) == "resuma.mp4":
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\images\resuma"
        play_video()
        display_screenshots(folder_path)
        file_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Resuma.txt"
        try:
            with open(file_path, "r") as file:
                saved_text = file.read()
                commentLog.insert("1.0", saved_text)  # Insert the saved text
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass
        save_button = tk.Button(rightFrame, text="Save", image=save_image, command=lambda: save_text(file_path))
        save_button.grid(row=1, column=1, columnspan=2, padx=80, pady=2)

    else:
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\screenshots\Untitled video - Made with Clipchamp"
        play_video()
        display_screenshots(folder_path)
        file_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Cabading.txt"
        try:
            with open(file_path, "r") as file:
                saved_text = file.read()
                commentLog.insert("1.0", saved_text)  # Insert the saved text
        except FileNotFoundError:
            # Handle the case when the file is not found
            pass
        save_button = tk.Button(rightFrame, text="Save", image=save_image, command=lambda: save_text(file_path))
        save_button.grid(row=1, column=1, columnspan=2, padx=80, pady=2)







def play_video():
    global current_frame, cap, is_paused

    if cap is not None:
        if not is_paused:
            ret, frame = cap.read()
            if ret:
                current_frame = frame.copy()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(cv2image)
                pil_image = pil_image.resize((1000, 700), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(pil_image)
                videoCanvas.create_image(0, 0, anchor=tk.NW, image=img)
                videoCanvas.image = img  # Keep a reference to prevent it from being garbage collected
        root.after(30, play_video)

def pause_video():
    global is_paused
    is_paused = not is_paused


def create_text_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def save_text(file_path):
    text = commentLog.get("1.0", "end-1c")  # Get the text from the Text widget

    with open(file_path, "w") as file:
        file.write(text)

        messagebox.showinfo(title="Success", message="Annotation Saved")
        root.destroy()
        import home_window

def download_pdf():
    global video_path
    if video_path is None:
        messagebox.showerror("Error", "Please upload a video before downloading the PDF.")
    else:
        download_pdf_report()


def seek_video(value):
    global current_frame, cap, seek_scale
    if cap is not None:
        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_to_seek = int((float(value) / 100) * total_frames)
        if frame_to_seek != frame_number:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_to_seek)
            ret, frame = cap.read()
            if ret:
                current_frame = frame.copy()
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(cv2image)
                pil_image = pil_image.resize((1000, 700), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(pil_image)
                videoCanvas.create_image(0, 0, anchor=tk.NW, image=img)
                videoCanvas.image = img  # Keep a reference to prevent it from being garbage collected

def update_slider_position():
    global cap, seek_scale
    if cap is not None:
        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames > 0:
            slider_position = int((frame_number / total_frames) * 100)
        else:
            slider_position = 0
        seek_scale.set(slider_position)
    root.after(100, update_slider_position)

def update_time_frame():
    global cap, length_label, frame_label
    if cap is not None:
        current_position = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        current_time = str(datetime.timedelta(milliseconds=current_position)).split(".")[0]
        current_frame = int((current_position / 1000) * fps)
        total_time = str(datetime.timedelta(seconds=int(total_frames / fps)))
        length_label.config(text=f"Video Length: {current_time}")
    root.after(1000, update_time_frame)

def update_image_caption(folder_path):
    # Clear previous content
    commentLog.delete("1.0", "end")

    # Initialize caption variable
    caption_text = ""

    # Iterate over images in the folder
    image_files = os.listdir(folder_path)

    for file_name in image_files:
        # Construct the image path
        image_path = os.path.join(folder_path, file_name)

        # Open and transform the image
        image = Image.open(image_path)
        image = transform(image).unsqueeze(0)

        # Generate the caption using the model
        with torch.no_grad():
            caption = model.caption_image(image, vocab)

        # Convert the caption from a list of tokens to a string
        caption_text += " ".join([token for token in caption if token not in ["<SOS>", "<EOS>", "<PAD>", "<UNK>"]])
        caption_text += " "

    # Update the caption text widget
    commentLog.insert("1.0", caption_text)

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    canvas.yview_scroll(-int(event.delta / 120), "units")


def view_screenshot(image):
    view_window = tk.Toplevel()
    view_window.geometry('1000x700')

    # Convert PhotoImage to PIL Image
    pil_image = ImageTk.getimage(image)

    # Resize the image
    resized_image = pil_image.resize((600, 400))

    # Convert PIL Image back to PhotoImage
    resized_photo = ImageTk.PhotoImage(resized_image)

    # Create a label to display the resized image
    label = tk.Label(view_window, image=resized_photo)
    label.pack(fill=tk.BOTH, expand=True)
    label.image = resized_photo

    view_window.resizable(False, False)
def display_screenshots(folder_path):
    screenshots_list = os.listdir(folder_path)
    num_screenshots = len(screenshots_list)


    for i, screenshot_name in enumerate(screenshots_list):
        screenshot_path = os.path.join(folder_path, screenshot_name)
        screenshot_image = Image.open(screenshot_path)
        screenshot_image.thumbnail((200, 200))  # Adjust the size as per your requirement
        screenshot_photo = ImageTk.PhotoImage(screenshot_image)
        screenshot_label = tk.Label(leftFrame, image=screenshot_photo)
        screenshot_label.grid(row=i, column=0, padx=10, pady=2, sticky=tk.W)

        # Keep a reference to the image and bind a click event to the label
        screenshot_label.image = screenshot_photo
        screenshot_label.bind("<Button-1>", lambda event, image=screenshot_photo: view_screenshot(image))

        # Configure the leftFrame to expand vertically
        leftFrame.grid_rowconfigure(i, weight=1)

    # Configure the leftFrame to expand horizontally as needed
    leftFrame.grid_columnconfigure(0, weight=1)




def display_latest_record():

    canvas_patient_details = tk.Canvas(rightFrame, width=100, height=70)
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
    firstname_label = tk.Label(canvas_patient_details, text="\n\n\n\n\n  First Name: {}".format(firstname), font=custom_font)
    firstname_label.grid(row=0, column=0, padx=10, pady=2, sticky='w')

    lastname_label = tk.Label(canvas_patient_details, text="\nLast Name: {}".format(lastname), font=custom_font)
    lastname_label.grid(row=1, column=0, padx=20, pady=2, sticky='w')

    birthday_label = tk.Label(canvas_patient_details, text="\nDate of Birth: {}".format(birthday), font=custom_font)
    birthday_label.grid(row=2, column=0, padx=20, pady=2, sticky='w')

    age_label = tk.Label(canvas_patient_details, text="\nAge: {}".format(age), font=custom_font)
    age_label.grid(row=3, column=0, padx=20, pady=2, sticky='w')

    sex_label = tk.Label(canvas_patient_details, text="\nSex: {}".format(sex), font=custom_font)
    sex_label.grid(row=4, column=0, padx=20, pady=2, sticky='w')

    address_label = tk.Label(canvas_patient_details, text="\nAddress: {}".format(address), font=custom_font)
    address_label.grid(row=5, column=0, padx=20, pady=2, sticky='w')

    contact_number_label = tk.Label(canvas_patient_details, text="\nContact Number: {}".format(contact_number), font=custom_font)
    contact_number_label.grid(row=6, column=0, padx=20, pady=2, sticky='w')

    emergency_contact_name_label = tk.Label(canvas_patient_details,text="\nEmergency Contact Name: {}".format(emergency_contact_name), font=custom_font)
    emergency_contact_name_label.grid(row=7, column=0, padx=20, pady=2, sticky='w')

    emergency_contact_number_label = tk.Label(canvas_patient_details,text="\nEmergency Contact Number: {}".format(emergency_contact_number), font=custom_font)
    emergency_contact_number_label.grid(row=8, column=0, padx=20, pady=2, sticky='w')

    marital_status_label = tk.Label(canvas_patient_details, text="\n  Marital Status: {}".format(marital_status), font=custom_font)
    marital_status_label.grid(row=9, column=0, padx=10, pady=2, sticky='w')


################################################################################      MENU     ######################################################################################

root = tk.Tk() # Makes the window
root.wm_title("Main Window") # Makes the title that will appear in the top left
root.state('zoomed')
root.geometry("1000x600")
root.config(bg="#CCCCCC")

bold_font = font.Font(weight="bold")

save_image = tk.PhotoImage(file=r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\diskette (1) (3).png")
# Left Frame

canvas = tk.Canvas(root, width=200, height=600)
canvas.grid(row=0, column=0, padx=10, pady=2, sticky=tk.NSEW)

leftFrame = tk.Frame(canvas, width=200, height=600)
leftFrame.grid(row=0, column=0, padx=4, pady=2, sticky=tk.NSEW)
leftFrame.grid_rowconfigure(0, weight=2)
leftFrame.grid_columnconfigure(0, weight=1)
leftFrame.config(bg="#CCCCCC")

canvas.create_window((0, 0), window=leftFrame, anchor="nw")
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"), bg="#CCCCCC")


scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=3, sticky=tk.NS)
canvas.config(yscrollcommand=scrollbar.set)

root.bind_all("<MouseWheel>", on_mousewheel)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Right Frame
rightFrame = tk.Frame(root, width=200, height=600)
rightFrame.grid(row=0, column=1, padx=10, pady=2, sticky=tk.NSEW)
rightFrame.config(bg="#CCCCCC")

commentLog = tk.Text(rightFrame, width=30, height=10, takefocus=0)
commentLog.grid(row=2, column=0, padx=10, pady=2, sticky=tk.NSEW)


# Video Canvas
videoCanvas = tk.Canvas(rightFrame, width=1000, height=700, bg='white')
videoCanvas.grid(row=0, column=0, padx=10, pady=2, sticky=tk.NSEW)
videoCanvas.config(bg="#CCCCCC")


btnFrame = tk.Frame(rightFrame, width=700, height=200)
btnFrame.grid(row=1, column=0, padx=8, pady=2, sticky=tk.NSEW)
btnFrame.config(bg="#CCCCCC")


play_image = tk.PhotoImage(file=r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\pause.png")


# Video Playback Buttons
pause_button = tk.Button(btnFrame, text="Play", image=play_image, command=pause_video)
pause_button.grid(row=3, column=0, padx=50, pady=5)



# Create a Scale (slider) widget
seek_scale = tk.Scale(btnFrame, from_=0, to=100, orient=tk.HORIZONTAL, command=seek_video)
seek_scale.set(0)  # Set the initial value of the slider
seek_scale.grid(row=3, column=2, columnspan=2, padx=80, pady=2, sticky=tk.NW)
seek_scale.configure(length=500)





# Create the video upload button
upload_button = tk.Button(btnFrame, text="Upload Video", command=open_file, font=bold_font)
upload_button.grid(row=3, column=4, padx=10, pady=10)

length_label = tk.Label(btnFrame, text="Video Length: 0/0")
length_label.grid(row=2, column=2, columnspan=2, padx=15, pady=2)

# Download the pdf file
download_button = tk.Button(root, text="Download PDF", command=download_pdf, font=bold_font)
download_button.grid(row=3, column=0, padx=10, pady=10)


# Start monitoring and updating the GUI. Nothing below here runs.
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

update_slider_position()


display_latest_record()


root.mainloop()