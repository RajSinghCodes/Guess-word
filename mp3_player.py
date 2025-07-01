import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame mixer
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Raj's MP3 Player")
window.geometry("400x200")

# Load Music File
def load_file():
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

# Pause Music
def pause():
    pygame.mixer.music.pause()

# Resume Music
def resume():
    pygame.mixer.music.unpause()

# Stop Music
def stop():
    pygame.mixer.music.stop()

# Buttons
btn_load = tk.Button(window, text="Load & Play", command=load_file)
btn_pause = tk.Button(window, text="Pause", command=pause)
btn_resume = tk.Button(window, text="Resume", command=resume)
btn_stop = tk.Button(window, text="Stop", command=stop)

# Layout
btn_load.pack(pady=10)
btn_pause.pack(pady=10)
btn_resume.pack(pady=10)
btn_stop.pack(pady=10)

window.mainloop()
