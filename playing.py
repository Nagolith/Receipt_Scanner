import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd


root= tk.Tk()


canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getCSV ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path)
    
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





    def1:
    global image_path
    global image_name
    global path

    image_path = filedialog.askopenfilename()
    image_name = os.path.basename(image_path)
    
    test = image_path.split(image_name)
    path = test[0]
  
    def2:
    new_file_name = 'poppy'
    clear_dir = 'cd\ '
    run_tesseract = 'tesseract ' + image_name + ' ' + new_file_name

    os.system(clear_dir)
    os.system('cd ' + path)
    os.chdir(path)
    os.system(run_tesseract)
