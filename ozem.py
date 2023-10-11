import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmb
from PIL import Image, ImageTk
import random
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ozem App!")

        lb_welc = ttk.Label(self, text="Welcome to the Ozem App!")

        pil_logo = Image.open("logo.png").resize((325, 125))
        self.img_logo = ImageTk.PhotoImage(pil_logo)
        lb_logo = ttk.Label(self, image=self.img_logo)

        btn_ozem = ttk.Button(self, text="ozem", command=self.ozem)

        lb_welc.pack(pady=(30, 0))
        lb_logo.pack(padx=20, pady=10)
        btn_ozem.pack(pady=(0, 30))

    def ozem(self):
        photo = random.choice(os.listdir("ozem"))
        new_ozem = Ozem(os.path.join("ozem", photo))
        new_ozem.mainloop()

class Ozem(tk.Toplevel):
    def __init__(self, photo_path):
        super().__init__()

        self.title("Ozem Image!")

        pil_ozem = Image.open(photo_path).resize((500, 500))
        self.img_ozem = ImageTk.PhotoImage(pil_ozem)
        lb_img = ttk.Label(self, image=self.img_ozem)

        btn_close = ttk.Button(self, text="clozem", command=self.destroy)

        lb_img.pack(padx=30, pady=(30, 10))
        btn_close.pack(pady=(0, 30))

if __name__ == "__main__":
    if not os.path.isdir("ozem") and not os.listdir("ozem"):
        tkmb.showerror("Error", "You must make a directory called ozem and put the images in there!")
    else:
        app = App()
        app.mainloop()