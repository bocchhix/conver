import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()

filetypeOptions = ["image", "pdf"]
fileType = ttk.Combobox(root, values=filetypeOptions)
fileType.pack()

def opent():
    filetypeR = fileType.get()
    if filetypeR == "image":
        os.startfile("imagemain.py")
    if filetypeR == "pdf":
        os.startfile("pdfmain.py")

button = tk.Button(root, command=opent)
button.pack()

root.mainloop()