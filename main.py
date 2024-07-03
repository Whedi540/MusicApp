import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("600x400")

        # Initialize pygame mixer
        pygame.mixer.init()

        # Playlist and current song index
        self.playlist = []
        self.current_song_index = 0

        # Background image setup
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = Image.open("bg.jpg")
        self.bg_image = self.bg_image.resize((600, 400))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Logo in the center
        self.logo_image = Image.open("lg.PNG")
        self.logo_image = self.logo_image.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)

        self.canvas.create_image(300, 100, image=self.logo_photo, anchor="center")

        # Load, Play, Pause, Stop buttons
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music, bg="blue", fg="white")
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music, bg="green", fg="white")
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music, bg="yellow", fg="black")
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music, bg="red", fg="white")

        self.canvas.create_window(150, 300, window=self.load_button)
        self.canvas.create_window(250, 300, window=self.play_button)
        self.canvas.create_window(350, 300, window=self.pause_button)
        self.canvas.create_window(450, 300, window=self.stop_button)

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("Music Files", "*.mp3 *.wav")])
        if files:
            self.playlist = files
            self.current_song_index = 0

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song_index])
            pygame.mixer.music.play()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
