from tkinter import *
from tkmacosx import Button
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os
import cmath

root= Tk()

canvas1 = Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
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
    
browseButton_CSV = Button(root, text="      Import CSV File     ", command=getCSV, fg='green', bg='red', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)


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


saveAsButton_Excel = Button(root, text='Convert CSV to Excel', command=convertToExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)




def exitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()


