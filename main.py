from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from PIL import ImageTk, Image


def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.jpg')]) 
    if file is not None: 
        content = file.read() 
        print(content) 


gui = Tk() 
gui.title('Steganography') 
gui.geometry("500x500")

btn = Button(gui, text ='Open', command = lambda:open_file()) 
btn.pack(side = 'top') 

canv = Canvas(gui, width=300, height=300, bg='white')
canv.pack(side ='top')



basewidth = 300
img = Image.open("./rocket.jpg")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

print(img)


#img = ImageTk.PhotoImage(file=")
#canv.create_image(20, 20, anchor=NW, image=img)

gui.mainloop() 
