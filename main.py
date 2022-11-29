from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
 
# root window title and dimension
root.title("Sunday Mourners")
# Set geometry (widthxheight)
c = Canvas(root, width=500, height=500)
c.pack()

logoRaw=Image.open('bandlogo-02.png')
resizeLogo=logoRaw.resize((100,100),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(resizeLogo)

# change the image size

c.create_image(5, 5, image=logo, anchor=NW)

# all widgets will be here
# Execute Tkinter
root.mainloop()