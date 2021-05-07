import tkinter as tk
from tkinter import filedialog
from PIL import Image as image
from PIL import ImageTk
from tkinter import *
import rawpy
import imageio
import tkinter.messagebox
import HSV
import HistEql
import CAIP
import matplotlib.pyplot as plt
import matplotlib.colors
import imageio
import cv2
from tkinter.filedialog import askopenfilename
import os

global imageFile
global fileName
def converttohsv():
    global imageFile
    global fileName
    img = imageio.imread(imageFile)
    resimg = HSV.hsv(img)
    imageio.imwrite("result/hsv/"+fileName,resimg)
    plt.imshow(resimg)
    plt.show()

def converttohist():
    global imageFile
    global fileName
    img = imageio.imread(imageFile)
    resimg = HistEql.he(img)
    imageio.imwrite("result/histeql/"+fileName,resimg)
    plt.imshow(resimg)
    plt.show()


def imgcontrast():
    global imageFile
    global fileName
    img = imageio.imread(imageFile)
    resimg = CAIP.caip(img)
    imageio.imwrite("result/caip/"+fileName,resimg)
    plt.imshow(resimg)
    plt.show()


def upload_image(e):
        global imageFile
        global fileName
        imageFile = askopenfilename(initialdir = "testdata")
        fileName = os.path.basename(imageFile)
        print(imageFile)
        img2 = image.open(imageFile)
        print(str(scale_w) + " " + str(scale_h))
        img2 = img2.resize((scale_w , scale_h));
        logo2 = ImageTk.PhotoImage(img2)
        w2.configure(image=logo2)
        button.config(text='Enhance',bg="#ccff99")
        w2.image = logo2

def convert_image():
    global imageFile
    converttohsv()
    converttohist()
    imgcontrast()


    
root = tk.Tk()

root.geometry("1000x550")	

root.title("Low Light Image Enhancement")

frame1 = Frame(master=root,height=200)
frame1.pack(fill=X)

frame2 = Frame(master=root,height=300)
frame2.pack(fill=X)

frame3 = Frame(master=root,height=200)
frame3.pack(fill=X)

frame4 = Frame(master=root,height=200)
frame4.pack(fill=X)

label1 = tk.Label(frame1,text="Original Image",fg="red")
label1.pack(padx=150,pady=50)
label1.config(font=("times new roman", 15))

scale_w = 400
scale_h = 250

w1 = tk.Label(frame2, image='').pack(side="right",padx=10,pady=0)

w2 = tk.Label(frame2, image='')
w2.pack(padx=10,pady=20)

print(w2)

button_select = tk.Button(frame3,text='Upload a Dark Image',fg="red",width=25,height=2)
button_select.bind('<Button>', upload_image)
button_select.pack(padx=115)

button = tk.Button(frame4,text='Enhance the Image`',fg="black",bg="#ffc2b3",width=25,height=2,command=convert_image)
button.pack(side="bottom",pady=30)

root.mainloop()
