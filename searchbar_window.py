import os
import cv2
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.video_path = None
        self.is_playing = False
        self.cap = None

        # Create a canvas to display the video frames
        self.canvas = tk.Canvas(root, width=960, height=540)
        self.canvas.pack()

    def play_video(self):
        if self.video_path is None:
            return

        self.is_playing = True
        self.cap = cv2.VideoCapture(self.video_path)

        while self.is_playing:
            ret, frame = self.cap.read()

            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame_rgb)
                # Resize the image to fit the canvas
                image = image.resize((960, 540), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.image = photo

                self.root.update()
            else:
                self.is_playing = False

        self.cap.release()

    def search_video(self):
        query = search_entry.get()
        folder_path = r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\process_videos"
        files = os.listdir(folder_path)
        found_video = False

        for file in files:
            if query.lower() in file.lower():
                self.video_path = os.path.join(folder_path, file)
                found_video = True
                break

        if not found_video:
            print("No video found.")
        else:
            # Update text based on query
            if query.lower() == "cabading":
                try:
                    with open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Cabading.txt", "r") as file:
                        saved_text = file.read()
                        text_label.config(text=saved_text)
                except FileNotFoundError:
                    # Handle the case when the file is not found
                    pass
            elif query.lower() == "cadelina":
                try:
                    with open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Cadelina.txt", "r") as file:
                        saved_text = file.read()
                        text_label.config(text=saved_text)
                except FileNotFoundError:
                    # Handle the case when the file is not found
                    pass
            elif query.lower() == "lijauco":
                try:
                    with open(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\Lijuaco.txt", "r") as file:
                        saved_text = file.read()
                        text_label.config(text=saved_text)
                except FileNotFoundError:
                    # Handle the case when the file is not found
                    pass
            elif query.lower() == "resuma":
                try:
                    with open("Resuma.txt", "r") as file:
                        saved_text = file.read()
                        text_label.config(text=saved_text)
                except FileNotFoundError:
                    # Handle the case when the file is not found
                    pass
            else:
                text_label.config(text="No video")

    def play_button_click(self):
        self.search_video()
        self.play_video()

    def back_home(self):
        window.withdraw()
        window.destroy()
        import home_window

def back_home():
    window.withdraw()
    window.destroy()
    import home_window

# Create the Tkinter window
window = tk.Tk()
window.title("Video Player")
window.geometry("1000x600")
window.configure(bg="#CCCCCC")
window.state("zoomed")

bold_font = font.Font(weight="bold")

# Create a VideoPlayer instance
player = VideoPlayer(window)

# Create a search label and entry
search_label = tk.Label(window, text="Enter last name to search:", font=("Arial", 14), fg="#000000", bg="#CCCCCC")
search_label.pack(pady=20)

search_entry = tk.Entry(window, font=("Arial", 12))
search_entry.pack()

# Create a search button
search_button = tk.Button(window, text="Search", font=bold_font, command=player.search_video)
search_button.place(x=920, y=650)

# Create a play button
play_button = tk.Button(window, text="Play", font=bold_font, command=player.play_button_click)
play_button.place(x=850, y=650)


# Create a label to display the text
text_label = tk.Label(window, text="", font=("Arial", 12), fg="black", bg="#CCCCCC")
text_label.pack(pady=100)

back_button = tk.Button(window, text="Back", command=back_home, font=bold_font)
back_button.place(x=1010, y=650)

window.mainloop()