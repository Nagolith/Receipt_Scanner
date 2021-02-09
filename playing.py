from tkinter import *
from tkmacosx import Button
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os
import tkinter as tk
import cmath

root= Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = '#474749', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = '#474749', fg="white",)
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global image_path
    global image_name
    global path

    image_path = filedialog.askopenfilename()
    image_name = os.path.basename(image_path)
    
    test = image_path.split(image_name)
    path = test[0]
    
# Creating a photoimage object to use image
photo = PhotoImage(file="upload.png")

# Resizing image to fit on button
photoimage = photo.subsample(9, 9)

browseButton_CSV = tk.Button(image = photoimage, text="     Import CSV File      ",  command=getCSV, fg='white', bg='#1db954', font=('helvetica', 12, 'bold'),compound=LEFT)
browseButton_CSV.pack()
canvas1.create_window(150, 120, window=browseButton_CSV)


def convertToExcel ():
    new_file_name = 'poppy'
    clear_dir = 'cd\ '
    run_tesseract = 'tesseract ' + image_name + ' ' + new_file_name

    os.system(clear_dir)
    os.system('cd ' + path)
    os.chdir(path)
    os.system(run_tesseract)

    # converts txt file to cvs
    read_file = pd.read_csv (path + new_file_name + '.txt', sep='delimiter', header=None)
    read_file.to_csv (path + new_file_name + '.csv', index=None)

    # converts cvs file to excel file
    # read_file = pd.read_csv (path + new_file_name, new_file_name + '.csv')
    # read_file.to_excel (path + new_file_name, new_file_name + '.xlsx', index = None, header=True)


photo2 = PhotoImage(file="convert.png")

# Resizing image to fit on button
photoimage2 = photo2.subsample(7, 7)

saveAsButton_Excel = tk.Button(image = photoimage2,text='Convert CSV to Excel', command=convertToExcel, bg='#1db954', fg='white', font=('helvetica', 12, 'bold'),compound=LEFT)
saveAsButton_Excel.pack()
canvas1.create_window(150, 180, window=saveAsButton_Excel)

def open_file():
    os.system(path + new_file_name + '.csv')
    
# Button open file
openFile_Excel = Button(root
    ,width = 160
    ,text='Open File'
    ,command=open_file
    ,bg='green'
    ,fg='white'
    ,font=('helvetica', 12, 'bold')
    ,borderless=1)

canvas1.create_window(150, 300, window=openFile_Excel


def exitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='#ec002d', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 240, window=exitButton)

root.mainloop()


