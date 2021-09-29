# import required modules
import tkinter as tk
import numpy as np
from tkinter import ttk, Tk, filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import os

import image_manipulation as img_m

# contrast border thumbnail
root = Tk()
root.title("Simple Photo Editor")
root.geometry("940x640")
root.resizable(False, False)


def selected(image_idx=1):
    global canvas2, img, img_array, img_path, M, N, img_array2
    if image_idx == 1:
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((250, 250))
        img_array = np.array(img)
        img1 = ImageTk.PhotoImage(img)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1
        M = img1.height()
        N = img1.width()
    else:
        img_path2 = filedialog.askopenfilename(initialdir=os.getcwd())
        imgg = Image.open(img_path2)
        imgg.thumbnail((250, 250))
        M_imgg = imgg.height
        N_imgg = imgg.width
        img_array2 = np.array(imgg)
        img_array2 = img_mnp.grayscale(img_array2, M_imgg, N_imgg)
        # img_array2 = img_mnp.biner(img_array2, 180, M_imgg, N_imgg)
        imgg = Image.fromarray(np.uint8(img_array2))
        # imgg = imgg.convert('L').point(
        #     lambda x: 0 if x == 0 else 255, "1")
        img2 = ImageTk.PhotoImage(imgg.resize((210, 210)))
        canvas3.create_image(155, 115, image=img2)
        canvas3.image = img2
    print('Image selected')


def reset():
    global img_path, img_array, canvas2
    img = Image.open(img_path)
    img.thumbnail((250, 250))
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


def save_temp():
    global img_array, img_result
    img_array = np.array(img_result)
    print('Image saved...')


def update_image(img_result_arr, binary=False):
    global img_result, canvas2
    img_result = Image.fromarray(np.uint8(img_result_arr))
    if binary:
        img_result = img_result.point(
            lambda x: 0 if x == 0 else 255)
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


def img_add():
    global img_mnp, img_array, M, N
    img_result_arr = img_mnp.addition(img_array, img_array2, M, N)
    update_image(img_result_arr, True)


def img_sub():
    global img_mnp, img_array, M, N
    img_result_arr = img_mnp.substraction(img_array, img_array2, M, N)
    update_image(img_result_arr, True)


def img_mult():
    global img_mnp, img_array, M, N
    img_result_arr = img_mnp.multiplication(img_array, img_array2, M, N)
    update_image(img_result_arr, True)


def img_not():
    global img_mnp, img_array, M, N
    img_result_arr = img_mnp.not_boolean(img_array, M, N)
    update_image(img_result_arr, True)


def img_trans():
    global img_mnp, img_array, M, N, input_x_trs, input_y_trs
    img_result_arr = img_mnp.translation(
        img_array, M, N, int(input_y_trs.get()), int(input_x_trs.get()))
    update_image(img_result_arr)


def img_rotate(event):
    global img_mnp, img_array, M, N, rotate_combo
    if str(rotate_combo.get()) == "90CCW":
        img_result_arr = img_mnp.rotation90CCW(img_array, M, N)
    else:
        img_result_arr = img_mnp.rotation90CW(img_array, M, N)
    update_image(img_result_arr)


def img_zoom(event):
    global img_mnp, img_array, M, N, zoom_combo
    if str(zoom_combo.get()) == "Zoom in":
        img_result_arr = img_mnp.zoom_in(img_array, M, N)
    else:
        img_result_arr = img_mnp.zoom_out(img_array, M, N)
    update_image(img_result_arr)


def img_flip(event):
    global img_mnp, img_array, M, N, flip_combo
    if str(flip_combo.get()) == "Flip horizontal":
        img_result_arr = img_mnp.horizontal_flip(img_array, M, N)
    else:
        img_result_arr = img_mnp.vertical_flip(img_array, M, N)
    update_image(img_result_arr)


# Global variable
img_path = ''
img = None
img_array = None
img_array2 = None
img_result = None
M = 0
N = 0

img_mnp = img_m.image_manipulation()

# ==================Display GUI==================
# Disclaimer text
text_content = """
============== README ==============\n
*Orange button need RGB image\n
*White button need 1 grayscale image\n
*'NOT' button need binary image (boolean operation)\n
*Violet button need 2 grayscale images (arithmetic operator)\n
*Top right green button used to update your image"""

text_disc = tk.Text(root, height=18, width=40, highlightthickness=3, padx=4,
                    highlightbackground='#B33A3A')
text_disc.place(x=630, y=420)
text_disc.insert(
    tk.END, text_content)

# ==================Function button==================

# Brightness
bright = tk.Label(root, text='Brightness: ', font=('ariel 10 bold'))
bright.place(x=8, y=8)
bright_val = tk.IntVar()
bright_scale = ttk.Scale(root, from_=0, to=255, variable=bright_val,
                         orient=tk.HORIZONTAL, command=brightening)
bright_scale.place(x=90, y=8)

# Biner
biner_label = tk.Label(root, text='Biner(0-255): ', font=('ariel 10 bold'))
biner_label.place(x=350, y=8)
biner_thresh = tk.IntVar()
biner_scale = ttk.Scale(root, from_=0, to=255, variable=biner_thresh,
                        orient=tk.HORIZONTAL, command=biner)
biner_scale.place(x=445, y=8)

# Negatif
btn_reset = tk.Button(root, text="Negative", width=10, bg='white', fg='black', border=2,
                      font=('ariel 10 bold'), relief=tk.GROOVE, command=negative)
btn_reset.place(x=730, y=8)

# grayscale
btn_grayscale = tk.Button(root, text="Grayscale", width=10, bg='#ff9e42', fg='black', border=2,
                          font=('ariel 10 bold'), relief=tk.GROOVE, command=grayscale)
btn_grayscale.place(x=730, y=40)

# addition
btn_add = tk.Button(root, text="Addition", width=10, bg='#B4A1EE', fg='black', border=2,
                    font=('ariel 10 bold'), relief=tk.GROOVE, command=img_add)
btn_add.place(x=630, y=70)

# substraction
btn_sub = tk.Button(root, text="Substraction", width=10, bg='#B4A1EE', fg='black', border=2,
                    font=('ariel 10 bold'), relief=tk.GROOVE, command=img_sub)
btn_sub.place(x=630, y=100)

# multiplication
btn_mult = tk.Button(root, text="Multiply", width=10, bg='#B4A1EE', fg='black', border=2,
                     font=('ariel 10 bold'), relief=tk.GROOVE, command=img_mult)
btn_mult.place(x=730, y=70)

# not operation
btn_not = tk.Button(root, text="NOT", width=10, bg='#ADD8E6', fg='black', border=2,
                    font=('ariel 10 bold'), relief=tk.GROOVE, command=img_not)
btn_not.place(x=730, y=100)

# translation
input_x_label = tk.Label(root, text='Translation: ', font=('ariel 10 bold'))
input_x_label.place(x=8, y=40)
btn_trs = tk.Button(root, text="Translation", width=10, bg='white', fg='black', border=2,
                    font=('ariel 10 bold'), relief=tk.GROOVE, command=img_trans)
btn_trs.place(x=100, y=35)
input_x_label = tk.Label(root, text='input x: ', font=('ariel 10 bold'))
input_x_label.place(x=8, y=65)
input_y_label = tk.Label(root, text='input y: ', font=('ariel 10 bold'))
input_y_label.place(x=8, y=85)
input_x_trs = tk.Entry(root, border=2)
input_x_trs.place(x=85, y=65)
input_x_trs.insert(tk.END, "0")
input_y_trs = tk.Entry(root, border=2)
input_y_trs.place(x=85, y=85)
input_y_trs.insert(tk.END, "0")

# combobox rotate
rotate = tk.Label(root, text="Rotate:", font=("ariel 10 bold"))
rotate.place(x=8, y=120)
values = ["90CW", "90CCW"]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=85, y=120)
rotate_combo.bind("<<ComboboxSelected>>", img_rotate)

# zoom
zoom = tk.Label(root, text="Zoom:", font=("ariel 10 bold"))
zoom.place(x=350, y=80)
values = ["Zoom in", "Zoom out"]
zoom_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
zoom_combo.place(x=410, y=80)
zoom_combo.bind("<<ComboboxSelected>>", img_zoom)

# combobox flip
flip = tk.Label(root, text="Flip:", font=("ariel 10 bold"))
flip.place(x=350, y=120)
values = ["Flip horizontal", "Flip vertical"]
flip_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
flip_combo.place(x=410, y=120)
flip_combo.bind("<<ComboboxSelected>>", img_flip)

# ==================Display GUI==================
# ==================Display Image==================

# create canvas to display image
canvas2 = tk.Canvas(root, width="600", height="420", relief=tk.RIDGE, bd=2)
canvas2.place(x=15, y=150)
canvas3 = tk.Canvas(root, width="300", height="220", relief=tk.RIDGE, bd=2)
canvas3.place(x=630, y=150)

# create buttons
# Save temp
btn_save_tmp = tk.Button(root, text="*sv", width=4, bg='#90EE90', fg='black', border=2,
                         font=('ariel 10 bold'), relief=tk.GROOVE, command=save_temp)
btn_save_tmp.place(x=860, y=5)

btn_reset = tk.Button(root, text="Reset", width=8, bg='black', fg='red',
                      font=('ariel 15 bold'), relief=tk.GROOVE, command=reset)
btn_reset.place(x=8, y=595)

btn_select_image = tk.Button(root, text="Select Image", bg='black', fg='gold',
                             font=('ariel 15 bold'), relief=tk.GROOVE, command=selected)
btn_select_image.place(x=180, y=595)

btn_select_image2 = tk.Button(root, text="Select Image 2", bg='#ADD8E6', fg='black',
                              font=('ariel 12 bold'), relief=tk.GROOVE, command=lambda: selected(2))
btn_select_image2.place(x=630, y=380)

btn_save = tk.Button(root, text="Save", width=8, bg='black', fg='gold',
                     font=('ariel 15 bold'), relief=tk.GROOVE, command=save)
btn_save.place(x=370, y=595)

btn_exit = tk.Button(root, text="Exit", width=8, bg='black', fg='gold',
                     font=('ariel 15 bold'), relief=tk.GROOVE, command=root.destroy)
btn_exit.place(x=500, y=595)

root.mainloop()
