import Interface
from tkinter import *
from PIL import Image

class Splash:
    def __init__(self):
        splash = Tk()
        height, width = 500, 500
        x = (splash.winfo_screenwidth() // 2) - (width // 2)
        y = (splash.winfo_screenheight() // 2) - (height // 2)
        splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        backgroundImage = PhotoImage(file="load_screen.png")
        bg_image = Label(splash, image=backgroundImage)
        bg_image.pack()
        splash.overrideredirect(True)

        label = Label(splash, text="Please Wait...", font=("yu gothic ui bold", 15 * -1), bg="#1F41A9", fg="#FFFFFF", )
        label.place(x=200, y=180)

        gifImage = "load.gif"
        openImage = Image.open(gifImage)
        frames = openImage.n_frames
        imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
        count = 0
        showAnimation = None

        def animation(count):
            global showAnimation
            newImage = imageObject[count]
            gif_Label.configure(image=newImage)
            count += 1
            if count == frames:
                count = 0
            showAnimation = splash.after(50, lambda: animation(count))

        gif_Label = Label(splash, image="")
        gif_Label.place(x=200, y=220, width=100, height=100)

        def main_window():
            splash.withdraw()
            Interface.Interface()

        splash.after(2200, main_window)
        animation(count)
        splash.mainloop()

Splash()