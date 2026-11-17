import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pdf2docx import Converter
from docx2pdf import convert
from pydub import AudioSegment
import subprocess
import os
import filetype
import string
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

def fileOpen():
    file = filedialog.askopenfilename(title="Select a file", filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
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

outputfiletypeFormats = ["MP3", "WAV"]
outputfiletypeEntry = ttk.Combobox(root, values=outputfiletypeFormats, state="readonly")
outputfiletypeEntry.current(0)
outputfiletypeEntry.pack()

def audioConversion(file, strfile, folder, filename, outputfiletype):
    print(file)
    if outputfiletype == "MP3" and filetype.guess(file).extension == "wav":
        audio = AudioSegment.from_wav(file)
        audio.export(f"{filename}.mp3", format="mp3")
    if outputfiletype == "WAV" and filetype.guess(file).extension == "mp3":
        audio = AudioSegment.from_mp3(file)
        audio.export(f"{folder}/{filename}.wav", format="wav")

def buttonConv():
    file = fileEntry.get()
    strfile = str(file)
    folder = folderEntry.get()
    filename = filenameEntry.get()
    outputfiletype = outputfiletypeEntry.get()
    audioConversion(file, strfile, folder, filename, outputfiletype)

converButton = tk.Button(root, command=buttonConv)
converButton.pack()

root.mainloop()