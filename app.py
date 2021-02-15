from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

class GUI:

    def __init__(self, master):
        
        master.geometry("300x300")

        frame = Frame(master)
        frame.pack()

        
        #self.button = Button(frame, text="KONEC", command=master.destroy)
        #self.button.pack(side=LEFT)

        #self.hi_there = Button(frame, text="Pozdrav!", command=self.rekni_ahoj)
        #self.hi_there.pack(side=LEFT)
        

        self.button = Button(frame, text="Open", command=self.open_file) 
        self.button.pack(side=LEFT)

    def open_file(): 
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.docx')]) 
        if file is not None: 
            content = file.read() 
            print(content) 
    




root = Tk(className='Steganography')
app = GUI(root)
root.mainloop()