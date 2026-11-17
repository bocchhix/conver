import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import PyInstaller.__main__
from pathlib import Path
import string
import ctypes
import sys

def fileOpen():
    file = filedialog.askopenfilename(title="Select a file", filetypes=[("PY files", "*.py")])
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

outputfiletypeFormats = ["EXE"]
outputfiletypeEntry = ttk.Combobox(root, values=outputfiletypeFormats, state="readonly")
outputfiletypeEntry.current(0)
outputfiletypeEntry.pack()

def pyConversion(file, folder, filename, outputfiletype):
    if outputfiletype == "EXE":
        PyInstaller.__main__.run([file, "--onefile", f"--distpath={folder}", f"--paths={Path(file).parent}", f"--name={filename}"])

def buttonConv():
    file = fileEntry.get()
    strfile = str(file)
    folder = folderEntry.get()
    filename = filenameEntry.get()
    outputfiletype = outputfiletypeEntry.get()
    pyConversion(file, folder, filename, outputfiletype)

converButton = tk.Button(root, command=buttonConv)
converButton.pack()

root.mainloop()