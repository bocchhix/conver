import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
import string
import ctypes
import sys
import pdf2docx

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

def check(fil_tip, fil_tip1):
    if fil_tip == "JPG" or "PNG" or "WEBP":
        if fil_tip1 == "PDF" or "DOCX":
            return False
        elif fil_tip1 == "JPG" or "PNG" or "WEBP":
            return True
    if fil_tip == "PDF" or "DOCX":
        if fil_tip1 == "JPG" or "PNG" or "WEBP":
            return False
        elif fil_tip1 == "PDF" or "DOCX":
            return True

def img_conver(path, folder):
    im = Image.open(img)
    im.save(f"{img_pat}/phot.{fgil_t}", f"{fil_tip}")

fil_tip = "JPG"

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

input1 = tk.Entry(frame)
input1.pack(side="left")

def img_po():
    fil_tip = combo.get()
    if fil_tip == "JPG":
        img_o = filedialog.askopenfilename(title="Select a file", filetypes=[("JPG files", "*.jpg")])
    elif fil_tip == "PNG":
        img_o = filedialog.askopenfilename(title="Select a file", filetypes=[("PNG files", "*.png")])
    elif fil_tip == "WEBP":
        img_o = filedialog.askopenfilename(title="Select a file", filetypes=[("WEBP files", "*.webp")])
    print(img_o)
    img_sto = str(img_o)
    input1.delete(0, tk.END)
    input1.insert(0, img_sto)

button_po = tk.Button(frame, command=img_po)
button_po.pack(side="left")

frame1 = tk.Frame(root)
frame1.pack()

input2 = tk.Entry(frame1)
input2.pack(side="left")

def img_pf():
    img_p = filedialog.askdirectory(title="Select a folde")
    img_stp = str(img_p)
    input2.delete(0, tk.END)
    input2.insert(0, img_stp)

button_pf = tk.Button(frame1, command=img_pf)
button_pf.pack(side="left")

options = ["JPG", "WEBP", "PNG", "DOCX"]

combo = ttk.Combobox(root, values=options, state="readonly")
combo.set("JPG")
combo.pack(pady=20)

options1 = ["JPG", "PNG", "DOCX"]

combo1 = ttk.Combobox(root, values=options, state="readonly")
combo1.set("JPG")
combo1.pack(pady=20)

def img_con():
    fil_tip = combo.get()
    fil_tip0 = combo1.get()
    check(fil_tip, fil_tip0)
    if fil_tip == "JPG":
        fil_tip = "JPEG"
        fgil_t = "jpg"
    elif fil_tip == "PNG":
        fgil_t = "png"
    elif fil_tip == "WEBP":
        fgil_t = "webp"
    img = input1.get()
    img_pat = input2.get()
    im = Image.open(img)
    im.save(f"{img_pat}/phot.{fgil_t}", f"{fil_tip}")

def pdf_con():
    pdf_path = img_o
    docx_path = f"[img_p]//doc.docx"

    cv = Converter(pdf_path)

    cv.convert(docx_path)

    cv.close()

def cho_con():
    fil_tip0 = combo1.get()
    if check(fil_tip, fil_tip0):
        if fil_tip == "DOCX":
            pdf_con()
        if fil_tip == "DOCX":
            pdf_con()
    

button = tk.Button(command=cho_con)
button.pack()

root.mainloop()