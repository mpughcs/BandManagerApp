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
logoRaw=Image.open('bandlogo-02.png')


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
        
        # make winodw non resizable
        self.resizable(0,0)
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


# BAND MANAGER PAGE############################################################################################################
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        # make menu bar appear at top of window



        
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


        # logoRaw=Image.open('bandlogo-02.png')
        resizeLogo=logoRaw.resize((75,75),Image.ANTIALIAS)
        logo=ImageTk.PhotoImage(resizeLogo)
        # show image
        label = Label(self, image=logo)
        label.image = logo
        label.place(x=50, y=50,anchor= CENTER)
        listbox = Listbox(self, height = 5, width = 20,)  
   
        listbox.insert(1,"12/10 @ warehouse OC")  
        listbox.insert(2, "1/13 @ Record Parlor")  
        listbox.insert(3, "2/10 @ The Observatory")
        
        # make listbox an in-line element with other items in row 1
        listbox.grid(row = 1, column = 4, padx = 10, pady = 10)
        


        # putting the button in its place by
        # using grid
        # bandStatsBtn.grid(row = 2, column = 1, padx = 10, pady = 10)
        exitBtn.place(x=50, y=450,anchor= CENTER)
        bandStatsBtn.place(x=55, y=400,anchor= CENTER)


  
          
  
  
#MANAGE DATA PAGE############################################################################################################
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Manage Data",font=headerFont).place(x=250, y=50, anchor=CENTER)

    
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        bandStatsBtn = ttk.Button(self, text ="Band Stats",
                            command = lambda : controller.show_frame(Page2))
                            
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        
        addShowBtn = ttk.Button(self, text ="Add Show",
                            command = lambda : controller.show_frame(Page1))
        addShowBtn.place(x=250, y=125,anchor= CENTER)

        addReleaseBtn = ttk.Button(self, text ="Add Release",command = lambda : controller.show_frame(Page1))
        addReleaseBtn.place(x=250, y=175,anchor= CENTER)

        addMerchBtn= ttk.Button(self, text ="Add Merch",command = lambda : controller.show_frame(Page1))
        addMerchBtn.place(x=250, y=225,anchor= CENTER)

        createSetListBtn= ttk.Button(self, text ="Create Set List",command = lambda : controller.show_frame(Page1))
        createSetListBtn.place(x=250, y=275,anchor= CENTER)

        createVenueBtn= ttk.Button(self, text ="Create Venue",command = lambda : controller.show_frame(Page1))
        createVenueBtn.place(x=250, y=325,anchor= CENTER)


        

        resizeLogo=logoRaw.resize((75,75),Image.ANTIALIAS)
        logo=ImageTk.PhotoImage(resizeLogo)
        # show image
        label = Label(self, image=logo)
        label.image = logo
        label.place(x=50, y=50,anchor= CENTER)

        

        homeBtn.place(x=50,y=125,anchor= CENTER)
        bandStatsBtn.place(x=55, y=400,anchor= CENTER)
        exitBtn.place(x=50, y=450,anchor= CENTER)


  
  
  
# STATS PAGE############################################################################################################
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Stats",font=headerFont).place(x=250, y=50, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.ANTIALIAS)
        logo=ImageTk.PhotoImage(resizeLogo)
        # show image
        label = Label(self, image=logo)
        label.image = logo
        label.place(x=50, y=50,anchor= CENTER)
        # button to show frame 2 with text
        # layout2
        manageDataBtn = ttk.Button(self, text ="Manage Data",
                            command = lambda : controller.show_frame(Page1))
     
        # button to show frame 3 with text
        # layout3
        earningsBtn = ttk.Button(self, text ="Earnings",
                            command = lambda : controller.show_frame(Page2))
                            
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        generateReportBtn = ttk.Button(self, text ="Generate Report",
                            command = lambda : controller.show_frame(Page2))
        
        # putting the button in its place by
        # using grid
        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)
        earningsBtn.place(x=250, y=125,anchor= CENTER)  
        generateReportBtn.place(x=250, y=175,anchor= CENTER)

        
  
  
# Driver Code
app = tkinterApp()
app.mainloop()