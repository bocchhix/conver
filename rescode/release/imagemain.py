import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import string
import ctypes
import sys

def fileOpen():
    file = filedialog.askopenfilename(title="Select a file", filetypes=[("JPG files", "*.jpg"), ("PNG files", "*.png"), ("WEBP files", "*.webp")])
    fileEntry.delete(0, tk.END)
    fileEntry.insert(0, file)

def folderOpen():
    folder = filedialog.askdirectory(title="Select a folder")
    folderEntry.delete(0, tk.END)
    folderEntry.insert(0, folder)

root = tk.Tk()

fileEntry = tk.Entry(root)
fileEntry.pack()

fileEntryButton = tk.Button(root, command=fileOpen)
fileEntryButton.pack()

folderEntry = tk.Entry(root)
folderEntry.pack()

folderEntryButton = tk.Button(root, command=folderOpen)
folderEntryButton.pack()

filenameEntry = tk.Entry(root)
filenameEntry.pack()

outputfiletypeFormats = ["PNG", "JPEG", "WEBP", "BMP"]
outputfiletypeEntry = ttk.Combobox(root, values=outputfiletypeFormats, state="readonly")
outputfiletypeEntry.current(0)
outputfiletypeEntry.pack()

def imageConversion(file, folder, filename, outputfiletype):
    openImage = Image.open(file)
    filTyp = Image.open(file).format
    openImage.save(f"{folder}/{filename}.{outputfiletype}", f"{filTyp}")

def buttonConv():
    file = fileEntry.get()
    file = str(file)
    folder = folderEntry.get()
    filename = filenameEntry.get()
    outputfiletype = outputfiletypeEntry.get()
    imageConversion(file, folder, filename, outputfiletype)

converButton = tk.Button(root, command=buttonConv)
converButton.pack()

root.mainloop()