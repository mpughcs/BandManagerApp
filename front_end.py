from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import db_operations as db


import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)
headerFont=("Ariel", 35)
smallFont=("Ariel", 12)
PAGE_1_NAME = "Start Menu"
PAGE_2_NAME = "Manage Data"
PAGE_3_NAME = "S 3"
logoRaw=Image.open('bandlogo-02.png')

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "Band Manager")
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

        for F in (StartPage, Page1, Page2, addShow, addRelease, addMerch,songStatView,addToSetlist):
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
        # universal style for all buttons, make them have no background color
        style = ttk.Style()
        # style.configure('TButton', bd=25, background='white', foreground='black', font=smallFont)
        style.configure('TButton', bd=25, background='white', foreground='black', font=smallFont)

  
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
        
        manageDataBtn.grid(row = 1, column = 1, padx = 10, pady = 10)
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
  
        ## button to show frame 2 with text layout2
        bandStatsBtn = ttk.Button(self, text ="Band Stats",
        command = lambda : controller.show_frame(Page2))
        # show image 


        # logoRaw=Image.open('bandlogo-02.png')
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
                            command = lambda : controller.show_frame(addShow))
        addShowBtn.place(x=250, y=125,anchor= CENTER)

        addReleaseBtn = ttk.Button(self, text ="Add Release",command = lambda : controller.show_frame(addRelease))
        addReleaseBtn.place(x=250, y=175,anchor= CENTER)

        addMerchBtn= ttk.Button(self, text ="Add Merch",command = lambda : controller.show_frame(addMerch))
        addMerchBtn.place(x=250, y=225,anchor= CENTER)

        addToSetlistBtn= ttk.Button(self, text ="Add To Setlist",command = lambda : controller.show_frame(addToSetlist))
        addToSetlistBtn.place(x=250, y=275,anchor= CENTER)

        

        

        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        songStatViewBtn = ttk.Button(self, text ="Song Stats",
                            command = lambda : controller.show_frame(songStatView))
                            
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        generateReportBtn = ttk.Button(self, text ="Generate Report",
                            command = lambda : generateReport())
        
        # putting the button in its place by
        # using grid
        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)
        songStatViewBtn.place(x=250, y=125,anchor= CENTER)  
        generateReportBtn.place(x=250, y=175,anchor= CENTER)

class addShow(tk.Frame):
    def __init__(self, parent, controller):
        yOffset=-15

        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Add Show",font=headerFont).place(x=250, y=15, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        # create form for adding show
        venueIdLabel=Label(self, bg="white",fg="black",text="VenueId",font=smallFont).place(x=250, y=65+yOffset, anchor=CENTER)
        venueIdEntry=Entry(self, bg="white",fg="black",font=smallFont)
        venueIdEntry.place(x=250, y=90+yOffset, anchor=CENTER)

        dateLabel=Label(self, bg="white",fg="black",text="Date",font=smallFont).place(x=250, y=125+yOffset, anchor=CENTER)
        dateEntry=Entry(self, bg="white",fg="black",font=smallFont)
        dateEntry.place(x=250, y=150+yOffset, anchor=CENTER)

        merchRevenueLabel=Label(self, bg="white",fg="black",text="Merch Revenue",font=smallFont).place(x=250, y=185+yOffset, anchor=CENTER)
        merchRevenueEntry=Entry(self, bg="white",fg="black",font=smallFont)
        merchRevenueEntry.place(x=250, y=210+yOffset, anchor=CENTER)

        topMerchLabel=Label(self, bg="white",fg="black",text="Top Merch ID",font=smallFont).place(x=250, y=245+yOffset, anchor=CENTER)
        topMerchEntry=Entry(self, bg="white",fg="black",font=smallFont)
        topMerchEntry.place(x=250, y=270+yOffset, anchor=CENTER)

        bookerLabel=Label(self, bg="white",fg="black",text="Booker",font=smallFont).place(x=250, y=305+yOffset, anchor=CENTER)
        bookerEntry=Entry(self, bg="white",fg="black",font=smallFont)
        bookerEntry.place(x=250, y=330+yOffset, anchor=CENTER)

        ticketsSoldLabel=Label(self, bg="white",fg="black",text="Tickets Sold",font=smallFont).place(x=250, y=365+yOffset, anchor=CENTER)
        ticketsSoldEntry=Entry(self, bg="white",fg="black",font=smallFont)
        ticketsSoldEntry.place(x=250, y=390+yOffset, anchor=CENTER)

        ticketPriceLabel=Label(self, bg="white",fg="black",text="Ticket Price",font=smallFont).place(x=250, y=425+yOffset, anchor=CENTER)
        ticketPriceEntry=Entry(self, bg="white",fg="black",font=smallFont)
        ticketPriceEntry.place(x=250, y=450+yOffset, anchor=CENTER)

        submitBtn = ttk.Button(self, text ="Submit",
                        command = lambda : insertShow(venueIdEntry,merchRevenueEntry,topMerchEntry,bookerEntry,ticketsSoldEntry,ticketPriceEntry,dateEntry))
        submitBtn.place(x=250, y=470,anchor= CENTER)



        
        
        # putting the button in its place by
        # using grid
        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)
        # earningsBtn.place(x=250, y=125,anchor= CENTER)  

class addRelease(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Add Release",font=headerFont).place(x=250, y=50, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        # create form for adding show
        yOffset=-35
        releaseNameLabel=Label(self, bg="white",fg="black",text="Release Name",font=smallFont).place(x=250, y=125+yOffset, anchor=CENTER)
        releaseNameEntry=Entry(self, bg="white",fg="black",font=smallFont)
        releaseNameEntry.place(x=250, y=150+yOffset, anchor=CENTER)

        releaseDateLabel=Label(self, bg="white",fg="black",text="Release Date",font=smallFont).place(x=250, y=185+yOffset, anchor=CENTER)
        releaseDateEntry=Entry(self, bg="white",fg="black",font=smallFont)
        releaseDateEntry.place(x=250, y=210+yOffset, anchor=CENTER)

        submitBtn = ttk.Button(self, text ="Submit",
                        command = lambda : insertRelease(releaseNameEntry,releaseDateEntry))
        submitBtn.place(x=250, y=500+yOffset,anchor= CENTER)



        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)

class addMerch(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Add Merch",font=headerFont).place(x=250, y=50, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        # create form for adding show
        yOffset=-35
        merchNameLabel=Label(self, bg="white",fg="black",text="Merch name",font=smallFont).place(x=250, y=125+yOffset, anchor=CENTER)
        merchNameEntry=Entry(self, bg="white",fg="black",font=smallFont)
        merchNameEntry.place(x=250, y=150+yOffset, anchor=CENTER)

        merchPriceLabel=Label(self, bg="white",fg="black",text="Cost to make",font=smallFont).place(x=250, y=185+yOffset, anchor=CENTER)
        merchPriceEntry=Entry(self, bg="white",fg="black",font=smallFont)
        merchPriceEntry.place(x=250, y=210+yOffset, anchor=CENTER)

        merchSaleCost=Label(self, bg="white",fg="black",text="Price to consumer",font=smallFont).place(x=250, y=245+yOffset, anchor=CENTER)
        merchSaleCost=Entry(self, bg="white",fg="black",font=smallFont)
        merchSaleCost.place(x=250, y=270+yOffset, anchor=CENTER)

        submitBtn = ttk.Button(self, text ="Submit",
                        command = lambda : insertMerch(merchNameEntry,merchPriceEntry,merchSaleCost))

        submitBtn.place(x=250, y=300,anchor= CENTER)
        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)


class addToSetlist(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Add to Set List",font=headerFont).place(x=250, y=50, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())
        # create form for adding show
        yOffset=-35
        gigIdLabel=Label(self, bg="white",fg="black",text="Gig ID",font=smallFont).place(x=250, y=125+yOffset, anchor=CENTER)
        gigIdEntry=Entry(self, bg="white",fg="black",font=smallFont)
        gigIdEntry.place(x=250, y=150+yOffset, anchor=CENTER)

        songIDLabel=Label(self, bg="white",fg="black",text="Song ID",font=smallFont).place(x=250, y=185+yOffset, anchor=CENTER)
        songIDEntry=Entry(self, bg="white",fg="black",font=smallFont)
        songIDEntry.place(x=250, y=210+yOffset, anchor=CENTER)



        submitBtn = ttk.Button(self, text ="Submit",
                        command = lambda : insertSetList(gigIdEntry,songIDEntry))
        submitBtn.place(x=250, y=300+yOffset,anchor= CENTER)
        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)




class songStatView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        testLabel=Label(self, bg="white",fg="black",text="Song Stats",font=headerFont).place(x=250, y=50, anchor=CENTER)
        resizeLogo=logoRaw.resize((75,75),Image.Resampling.LANCZOS)
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
        
        homeBtn = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
        exitBtn = ttk.Button(self, text ="Exit",
            command = lambda : exit())

        yOffset=-10
        # represent data using a tree view
        tree = ttk.Treeview(self, columns=("Song Title","Times Performed","Release Date"), show="headings", height="6")
        tree.column("Song Title", width=200, anchor=CENTER)
        tree.column("Times Performed", width=100, anchor=CENTER)
        tree.column("Release Date", width=100, anchor=CENTER)
        tree.heading("Song Title", text="Song Title")
        tree.heading("Times Performed", text="Times Performed")
        tree.heading("Release Date", text="Release Date")
        tree.place(x=250, y=240+yOffset, anchor=CENTER)
        addSongViewDataToTree(tree)
        
        



        


        manageDataBtn.place(x=60, y=400,anchor= CENTER)

        homeBtn.place(x=50,y=125,anchor= CENTER)

        exitBtn.place(x=50, y=450,anchor= CENTER)



       
# make button for number of times each song has been played since released 


# generate report will create a csv file with all the data in it
def generateReport():
    try:
        db.writeDateToCsv()
    except:
        print("error")




def getShowData(e1: Entry ,e2:Entry,e3:Entry,e4:Entry,e5:Entry,e6:Entry,e7:Entry):
    returnStr= e1.get()+","+e2.get()+","+e3.get()+","+e4.get()+","+e5.get()+","+e6.get()+","+e7.get()
    returnArr=returnStr.split(",")
    print(returnArr)
    return returnArr

def insertShow(e1: Entry ,e2:Entry,e3:Entry,e4:Entry,e5:Entry,e6:Entry,e7:Entry):
    # get data from form
    showData=getShowData(e1,e2,e3,e4,e5,e6,e7)
    # insert into database
    print(showData)
    db.insertGig(db.mycursor,showData[0],showData[1],showData[2],showData[3],showData[4],showData[5],showData[6])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

def getSetListData(e1: Entry, e2: Entry):
    returnStr= e1.get()+","+e2.get()
    returnArr=returnStr.split(",")
    # print(returnArr)
    return returnArr
def insertSetList(e1: Entry, e2: Entry):
    # get data from form
    setListData=getSetListData(e1,e2)
    # insert into database
    print(setListData)
    db.insertSetList(db.mycursor,setListData[1],setListData[0])
    e1.delete(0,END)
    e2.delete(0,END)

def getReleaseData(e1: Entry ,e2:Entry):
    returnStr= e1.get()+","+e2.get()
    returnArr=returnStr.split(",")
    # print(returnArr)
    return returnArr

def insertRelease(e1: Entry ,e2:Entry):
    # get data from form
    releaseData=getReleaseData(e1,e2)
    # insert into database
    print(releaseData)
    db.insertRelease(db.mycursor,releaseData[0],releaseData[1])
    e1.delete(0,END)
    e2.delete(0,END)

def getMerchData(e1:Entry, e2:Entry, e3:Entry):
    returnStr= e1.get()+","+e2.get()+","+e3.get()
    returnArr=returnStr.split(",")
    return returnArr

def insertMerch(e1:Entry, e2:Entry, e3:Entry):
    merchData=getMerchData(e1,e2,e3)
    print(merchData)
    db.insertMerch(db.mycursor,merchData[0],merchData[1],merchData[2])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
   


def exit():
    print("exiting")
    db.mydb.close()
    sys.exit()


    
       

        
def addSongViewDataToTree(tree):
    # get data from database
    songData=db.getSongViewData()
    # add data to tree
    for row in songData:
        tree.insert("", "end", values=row)

  
# Driver Code
app = tkinterApp()
app.mainloop()