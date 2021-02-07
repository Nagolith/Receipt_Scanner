from tkinter import *
from tkmacosx import Button
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os

import_file_path = ""

root= Tk(className=" Receipt Scrapper")


canvas1 = Canvas(root, width = 300, height = 400, bg = 'lightgrey', relief = 'raised')
canvas1.pack()

label1 = Label(root, text='File Conversion Tool', bg = 'lightgrey')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global read_file
    global import_file_path
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path)
# Button
browseButton_CSV = Button(text="      Import CSV File     "
                        , command=getCSV, fg='green'
                        , bg='red'
                        , font=('helvetica', 12, 'bold')
                        , borderless=1)
canvas1.create_window(150, 150, window=browseButton_CSV)

# Display filename
#label2 = Label(root, text=os.path.basename(import_file_path), bg = 'lightgrey')
#label2.config(font=('helvetica', 20))
#canvas1.create_window(150, 200, window=label2)

def convertToExcel ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None, header=True)

# Button
saveAsButton_Excel = Button(text='Convert CSV to Excel', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'), borderless=1)
canvas1.create_window(150, 250, window=saveAsButton_Excel)

def exitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

# Button open file
openFile_Excel = Button(text='Open File', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'), borderless=1)
canvas1.create_window(150, 300, window=openFile_Excel)
       
# Button 
exitButton = Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'), borderless=1)
canvas1.create_window(150, 350, window=exitButton)

root.mainloop()