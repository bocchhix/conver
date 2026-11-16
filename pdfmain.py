import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pdf2docx import Converter
from docx2pdf import convert
import subprocess
import os
import filetype
import string
import ctypes
import sys

def fileOpen():
    file = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF files", "*.pdf"), ("DOCX files", "*.docx")])
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

outputfiletypeFormats = ["PDF", "DOCX"]
outputfiletypeEntry = ttk.Combobox(root, values=outputfiletypeFormats, state="readonly")
outputfiletypeEntry.current(0)
outputfiletypeEntry.pack()

def pdfConversion(file, strfile, folder, filename, outputfiletype):
    print(filetype.guess(file).extension)
    print(outputfiletype)
    if filetype.guess(file).extension == "pdf" and outputfiletype == "DOCX":
        cv = Converter(file)
        cv.convert(f"{folder}/{filename}.docx", start=0, end=None)
        cv.close()
    if filetype.guess(file).extension == "docx" and outputfiletype == "PDF":
        print(f"{folder}/{filename}.pdf")
        libreoffice_path = r"C:\\Program Files\\LibreOffice\\program\\soffice.exe"
        subprocess.run([libreoffice_path, "--headless", "--convert-to", "pdf", "--outdir", folder, file], check=True)

def buttonConv():
    file = fileEntry.get()
    strfile = str(file)
    folder = folderEntry.get()
    filename = filenameEntry.get()
    outputfiletype = outputfiletypeEntry.get()
    pdfConversion(file, strfile, folder, filename, outputfiletype)

converButton = tk.Button(root, command=buttonConv)
converButton.pack()

root.mainloop()