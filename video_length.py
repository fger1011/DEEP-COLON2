import tkinter as tk
import cv2


class VideoPlayer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0

        self.window = tk.Tk()
        self.window.title("Video Player")

        # Create a canvas to display the video frames
        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.pack()

        # Create a seek slider
        self.seek_slider = tk.Scale(self.window, from_=0, to=self.total_frames,
                                    orient=tk.HORIZONTAL, length=600, command=self.update_frame)
        self.seek_slider.pack()

        # Create buttons for play and pause
        self.play_button = tk.Button(self.window, text="Play", command=self.play)
        self.pause_button = tk.Button(self.window, text="Pause", command=self.pause)
        self.play_button.pack(side=tk.LEFT)
        self.pause_button.pack(side=tk.LEFT)

        self.is_playing = False

        self.update_frame()
        self.window.mainloop()

    def update_frame(self, event=None):
        self.current_frame = int(self.seek_slider.get())
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
            self.canvas.create_image(0, 0, image=image, anchor=tk.NW)
            self.window.update()

    def play(self):
        self.is_playing = True
        while self.is_playing:
            if self.current_frame >= self.total_frames:
                self.current_frame = 0
                self.seek_slider.set(self.current_frame)
            self.update_frame()
            self.current_frame += 1
            self.seek_slider.set(self.current_frame)

    def pause(self):
        self.is_playing = False


# Provide the path to your video file here
video_player = VideoPlayer(r"C:\Users\Franco Gian Ramos\PycharmProjects\pythonProject8\data\colon_video\Cabading.mp4")
