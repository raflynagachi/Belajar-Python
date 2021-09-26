# import required modules
import tkinter as tk
import numpy as np
from tkinter import StringVar, Variable, ttk, Tk, filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

from numpy.lib.type_check import imag
import image_manipulation as img_m

# contrast border thumbnail
root = Tk()
root.title("Simple Photo Editor")
root.geometry("640x640")


def selected():
    global canvas2, img, img_array, img_path, M, N
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img_array = np.array(img)

    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1
    M = img1.height()
    N = img1.width()
    print(img_array)
    print('Image selected')


def reset():
    global img_path, img_array, canvas2
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img_array = np.array(img)

    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1


def save():
    global img_path, img_result
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}", filetypes=[(
        "All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        img_result.save(file)
        print('Image saved')


def update_image(img_result_arr, binary=False):
    global img_result, canvas2
    img_result = Image.fromarray(np.uint8(img_result_arr))
    if binary:
        img_result = img_result.convert('L').point(
            lambda x: 0 if x == 0 else 255, "1")
    img_result_tk = ImageTk.PhotoImage(
        image=img_result)
    canvas2.create_image(300, 210, image=img_result_tk)
    canvas2.image = img_result_tk
    print('Image updated')


def brightening(event):
    global img_result, img_mnp, img_array, M, N, bright_val
    # lambda img_result: img_mnp.image_brightening(img_array, bright_val.get(), M, N)
    img_result_arr = img_mnp.image_brightening(
        img_array, bright_val.get(), M, N)
    update_image(img_result_arr)


def biner(event):
    global img_mnp, img_array, M, N, biner_thresh
    img_result_arr = img_mnp.biner(img_array, int(biner_thresh.get()), M, N)
    update_image(img_result_arr, True)


def grayscale():
    global img_mnp, img_array, M, N
    img_array = img_mnp.grayscale(img_array, M, N)
    update_image(img_array)


def negative():
    global img_mnp, img_array, M, N
    img_result_arr = img_mnp.negatif(img_array, M, N)
    update_image(img_result_arr)


# Global variable
img_path = ''
img = None
img_array = None
img_result = None
M = 0
N = 0

img_mnp = img_m.image_manipulation()

# Brightness
bright = tk.Label(root, text='Brightness', font=('ariel 12 bold'))
bright.place(x=8, y=8)
bright_val = tk.IntVar()
bright_scale = ttk.Scale(root, from_=0, to=255, variable=bright_val,
                         orient=tk.HORIZONTAL, command=brightening)
bright_scale.place(x=110, y=10)

# Biner
biner_label = tk.Label(root, text='Biner(0-255)', font=('ariel 12 bold'))
biner_label.place(x=250, y=8)
biner_thresh = tk.IntVar()
biner_scale = ttk.Scale(root, from_=0, to=255, variable=biner_thresh,
                        orient=tk.HORIZONTAL, command=biner)
biner_scale.place(x=375, y=10)

# grayscale
btn_grayscale = tk.Button(root, text="Grayscale", width=8, bg='white', fg='black', border=2,
                          font=('ariel 12 bold'), relief=tk.GROOVE, command=grayscale)
btn_grayscale.place(x=520, y=40)

# Negatif
btn_reset = tk.Button(root, text="Negative", width=8, bg='white', fg='black', border=2,
                      font=('ariel 12 bold'), relief=tk.GROOVE, command=negative)
btn_reset.place(x=520, y=8)

# create canvas to display image
canvas2 = tk.Canvas(root, width="600", height="420", relief=tk.RIDGE, bd=2)
canvas2.place(x=15, y=150)

# create buttons
btn_reset = tk.Button(root, text="Reset", width=8, bg='black', fg='red',
                      font=('ariel 15 bold'), relief=tk.GROOVE, command=reset)
btn_reset.place(x=8, y=595)

btn_select_image = tk.Button(root, text="Select Image", bg='black', fg='gold',
                             font=('ariel 15 bold'), relief=tk.GROOVE, command=selected)
btn_select_image.place(x=180, y=595)

btn_save = tk.Button(root, text="Save", width=8, bg='black', fg='gold',
                     font=('ariel 15 bold'), relief=tk.GROOVE, command=save)
btn_save.place(x=370, y=595)

btn_exit = tk.Button(root, text="Exit", width=8, bg='black', fg='gold',
                     font=('ariel 15 bold'), relief=tk.GROOVE, command=root.destroy)
btn_exit.place(x=500, y=595)

root.mainloop()
