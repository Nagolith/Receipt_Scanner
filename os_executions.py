import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os


root= tk.Tk()


canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global read_file
    
    path_to_file = filedialog.askopenfilename()
    # Displays the path to the file
    print(read_file)
    # Displays the type of the variable used
    print(type(read_file))
    # use the 'os.system' to execute the path
    os.system(read_file)
    
browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, fg='green', bg='red', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)


def convertToExcel ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None, header=True)

saveAsButton_Excel = tk.Button(text='Convert CSV to Excel', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
