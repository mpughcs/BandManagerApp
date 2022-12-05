from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font


import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)
headerFont=("Ariel", 35)
PAGE_1_NAME = "Start Menu"
PAGE_2_NAME = "Manage Data"
PAGE_3_NAME = "S 3"

  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # logoRaw=Image.open('bandlogo-02.png')
        # resizeLogo=logoRaw.resize((100,100),Image.ANTIALIAS)
        # logo=ImageTk.PhotoImage(resizeLogo)
        # show image 
       
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # make window larger
        self.geometry("500x500")
  
        # initializing frames to an empty array
        self.frames = {} 
        
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        testLabel=Label(self, bg="white",fg="black",text="Band Manager",font=headerFont).grid(row = 0, column = 4, padx = 10, pady = 10)

         
        # putting the grid in its place by using
        # grid
  
        manageDataBtn = ttk.Button(self, text ="Manage Data",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        manageDataBtn.grid(row = 1, column = 1, padx = 10, pady = 10)
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
  
        ## button to show frame 2 with text layout2
        bandStatsBtn = ttk.Button(self, text ="Band Stats",
        command = lambda : controller.show_frame(Page2))
        # show image 
        logoRaw=Image.open('bandlogo-02.png')
        resizeLogo=logoRaw.resize((100,100),Image.ANTIALIAS)
        logo=ImageTk.PhotoImage(resizeLogo)
        # show image
        label = Label(self, image=logo)
        label.image = logo
        label.grid(row = 1, column = 4, padx = 10, pady = 10)
        


        # putting the button in its place by
        # using grid
        bandStatsBtn.grid(row = 2, column = 1, padx = 10, pady = 10)
        exitBtn.grid(row = 12, column = 1, padx = 10, pady = 200)

  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        # label = ttk.Label(self, text ="MANAGE DATA", font = LARGEFONT)
  
        # button to show frame 2 with text
        # layout2
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
  
        bandStatsBtn = ttk.Button(self, text ="Band Stats",
                            command = lambda : controller.show_frame(Page2))
                            
     
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())


        testLabel=Label(self, bg="white",fg="black",text="Manage Data",font=headerFont).grid(row = 0, column = 4, padx = 10, pady = 10)

        homeBtn.grid(row = 2, column = 1, padx = 10, pady = 10)
        bandStatsBtn.grid(row = 1, column = 1, padx = 10, pady = 10)
        exitBtn.grid(row = 12, column = 1, padx = 10, pady = 200)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Stats",font=headerFont).grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        manageDataBtn = ttk.Button(self, text ="Manage Data",
                            command = lambda : controller.show_frame(Page1))
     
        # button to show frame 3 with text
        # layout3
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        # putting the button in its place by
        # using grid
        manageDataBtn.grid(row = 1, column = 1, padx = 10, pady = 10)
        homeBtn.grid(row = 2, column = 1, padx = 10, pady = 10)
        exitBtn.grid(row = 12, column = 1, padx = 10, pady = 200)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()