from datetime import datetime
import time
import Tkinter

def DateTimeInMagic(MEDITECH):
    MEDITECH = float(long(MEDITECH))
    MTTime = MEDITECH
    if time.daylight == 1:
        #Add the difference between UTC Daylight Savings and MEDITECH time (320734800 seconds)
        MTTime += 320731200
    else:
        #Add the difference between UTC and MEDITECH time (320734800 seconds)
        MTTime += 320734800
    #1068915786 = 1/13/14 17:03:06 EST
    #UTC time
    d = datetime.utcfromtimestamp(MTTime)       
    #Calculate offset based off OS time UTC to EST offset 
    offset = datetime.now() - datetime.utcnow()   
    #Add offset to UTC
    return d + offset   
     
class TimeGUI(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter time here.")

        button = Tkinter.Button(self,text=u"Convert",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="lightblue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Time:")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        self.labelVariable.set(DateTimeInMagic(self.entryVariable.get()))

    def OnPressEnter(self,event):
        self.labelVariable.set(DateTimeInMagic(self.entryVariable.get()))
        
if __name__ == "__main__":
    app = TimeGUI(None)
    app.title('MEDITECH Time')
    app.mainloop()