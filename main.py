import tkinter as tk
from PIL import Image

img = Image.open("data/assets/TransparentCookie.png").resize((120, 70))
img.save("data/assets/PerfectCookie.png")

window = tk.Tk()

photo = tk.PhotoImage(file=r'data\assets\PerfectCookie.png')
button = tk.Button(window, image=photo)
button.pack()

window.mainloop()


# TODO: add three inputs = a, b, c; then make the button to compute quadratic and output it to the GUI
