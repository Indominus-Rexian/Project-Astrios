import tkinter as tk
from tkVideoPlayer import TkinterVideo

class Tker():
    def __init__(self):
        pass

    def Player(self, loc):
        root = tk.Tk()
        player = TkinterVideo(master=root, scaled=True, pre_load=False)
        player.load(loc)
        player.pack(expand=True, fill='both')
        player.play()
        root.mainloop()