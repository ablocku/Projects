import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

aplicatii = []

if os.path.isfile('apps.txt') :
    with open('apps.txt', 'r') as f :
        apltemp = f.read()
        apltemp = apltemp.split(',')
        aplicatii = [x for x in apltemp if x.strip()]


def add():

    for wid in frame2.winfo_children():
        wid.destroy()

    name = filedialog.askopenfilename(initialdir="/", title="Select Title",
                                      filetypes=(("Executables", "*.exe"),("All Files","*.*")))
    aplicatii.append(name)
    print(name)
    for i in aplicatii :
        l = tk.Label(frame2, text=i, fg='white', bg="#3500D3")
        l.pack()

def run():
    for i in aplicatii :
        os.startfile(i)

def dele():
    aplicatii.pop(0)

canvas = tk.Canvas(root, height = 700, width = 700, bg="#0C0032")
canvas.pack()

frame = tk.Frame(root, bg="#190061")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

frame1 = tk.Frame(frame, bg="#3500D3")
frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

frame2 = tk.Frame(frame1, bg="#3500D3")
frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

opFile = tk.Button (frame, text="Open File ", padx=20, pady=2.4, fg="white", bg="#282828", command=add)
opFile.pack()

run = tk.Button  (frame, text="Run Apps ", padx=20, pady=2.4, fg="white", bg="#282828", command=run)
run.pack()

delete = tk.Button (frame, text="Delete", padx=10 , pady=2, fg="white", bg="#282828", command=dele)
delete.pack()

for i in aplicatii :
    l = tk.Label(frame2, text=i)
    l.pack()

root.mainloop()


with open('apps.txt', 'w') as f:
    for i in aplicatii :
        f.write(i + ',')
