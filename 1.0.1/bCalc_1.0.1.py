from tkinter import *
from tkinter import messagebox as mbox


class bCalculator:

    def __init__(self, root):
        #........................design..........................
        root.title("bussiness calculator")

        frame = Frame(root)
        frame.pack(side=TOP, padx=20, pady=20)

        self.pVar = StringVar()
        Label(frame, text="Principal : ").grid(row=0, column=0, sticky=E)
        self.pEntry = Entry(frame, textvariable=self.pVar, bd=2)
        self.pEntry.grid(row=0, column=1, pady=2)

        self.tVar = StringVar()
        Label(frame, text="Time : ").grid(row=1, column=0, sticky=E)
        self.tEntry = Entry(frame, textvariable=self.tVar, bd=2)
        self.tEntry.grid(row=1, column=1, pady=2)

        self.rVar = StringVar()
        Label(frame, text="Rate : ").grid(row=2, column=0, sticky=E)
        self.rEntry = Entry(frame, textvariable=self.rVar, bd=2)
        self.rEntry.grid(row=2, column=1, pady=2)

        self.iVar = StringVar()
        Label(frame, text="Interest : ").grid(row=3, column=0, sticky=E)
        self.iEntry = Entry(frame, textvariable=self.iVar, bd=2)
        self.iEntry.grid(row=3, column=1, pady=2)

        self.bResult = Button(frame, text="click", bd=4, command=lambda: self.mainFunc(
            self.pVar, self.tVar, self.rVar, self.iVar))
        self.bResult.grid(row=0, column=2, rowspan=4,
                          ipadx=10, ipady=10, padx=35)

        lframe = Frame(root)
        lframe.pack(side=TOP)
        Label(lframe, text="Result log : ").grid(row=0, column=0, sticky=W)
        self.lbox = Listbox(lframe, width=80)
        self.lbox.grid(row=1, column=0)

        statusframe = Frame(root)
        statusframe.pack(side=BOTTOM, fill=X)

        statusdata = Label(statusframe, text="version : 1.0.1")
        statusdata.pack(side=LEFT)

#...................main working function....................

    def mainFunc(self, datap, datat, datar, datai):
        #.........................check principal.................
        if datap.get() == "" and datai.get() != "" and datat.get() != "" and datar.get() != "":
            if self.valdata(datai.get(), "i") == True and self.valdata(datat.get(), "t") == True and self.valdata(datar.get(), "r") == True:
                self.pCal()
            else:
                if self.valdata(datai.get(), "i") == "i":
                    mbox.showerror("Error", " interest data is invalid")
                elif self.valdata(datat.get(), "t") == "t":
                    mbox.showerror("Error", "time data is invalid")
                elif self.valdata(datar.get(), "r") == "r":
                    mbox.showerror("Error", "rate data is invalid")
        #.........................calculate interest...............
        elif datap.get() != "" and datai.get() == "" and datat.get() != "" and datar.get() != "":
            if self.valdata(datap.get(), "p") == True and self.valdata(datat.get(), "t") == True and self.valdata(datar.get(), "r") == True:
                self.iCal()
            else:
                if self.valdata(datap.get(), "p") == "p":
                    mbox.showerror("Error", " principal data is invalid")
                elif self.valdata(datat.get(), "t") == "t":
                    mbox.showerror("Error", "time data is invalid")
                elif self.valdata(datar.get(), "r") == "r":
                    mbox.showerror("Error", "rate data is invalid")
        #..........................calculate time..................
        elif datap.get() != "" and datai.get() != "" and datat.get() == "" and datar.get() != "":
            if self.valdata(datai.get(), "i") == True and self.valdata(datap.get(), "p") == True and self.valdata(datar.get(), "r") == True:
                self.tCal()
            else:
                if self.valdata(datai.get(), "i") == "i":
                    mbox.showerror("Error", " interest data is invalid")
                elif self.valdata(datap.get(), "p") == "p":
                    mbox.showerror("Error", "principal data is invalid")
                elif self.valdata(datar.get(), "r") == "r":
                    mbox.showerror("Error", "rate data is invalid")
        #.....................calculate rate......................
        elif datap.get() != "" and datai.get() != "" and datat.get() != "" and datar.get() == "":
            if self.valdata(datai.get(), "i") == True and self.valdata(datat.get(), "t") == True and self.valdata(datap.get(), "p") == True:
                self.rCal()
            else:
                if self.valdata(datai.get(), "i") == "i":
                    mbox.showerror("Error", " interest data is invalid")
                elif self.valdata(datat.get(), "t") == "t":
                    mbox.showerror("Error", "time data is invalid")
                elif self.valdata(datap.get(), "p") == "p":
                    mbox.showerror("Error", "principal data is invalid")
        elif datap.get() != "" and datai.get() != "" and datat.get() != "" and datar.get() != "":
            mbox.showwarning(
                "Warning", "you must have to empty a field which result you want")
        else:
            mbox.showwarning("warning", "only one field must be empty")

    #.................data validation...............
    def valdata(self, data, identifier):
        try:
            getdata = float(data)
            return True
        except:
            return identifier
    #................principal calculation..........

    def pCal(self):
        inter = float(self.iVar.get())
        tim = float(self.tVar.get())
        rat = float(self.rVar.get())
        pri = round((inter * 100) / (tim * rat), 2)
        self.pEntry.insert(END, pri)
        self.lboxentry()
    #...............interest calculation..............

    def iCal(self):
        pri = float(self.pVar.get())
        tim = float(self.tVar.get())
        rat = float(self.rVar.get())
        inter = round(((pri * tim * rat) / 100), 2)
        self.iEntry.insert(END, inter)
        self.lboxentry()
    #.............time calculation..................

    def tCal(self):
        pri = float(self.pVar.get())
        inter = float(self.iVar.get())
        rat = float(self.rVar.get())
        tim = round((inter * 100) / (pri * rat), 2)
        self.tEntry.insert(END, tim)
        self.lboxentry()

    #................rate calculation...............
    def rCal(self):
        pri = float(self.pVar.get())
        inter = float(self.iVar.get())
        tim = float(self.tVar.get())
        rat = round((inter * 100) / (pri * tim), 2)
        self.rEntry.insert(END, rat)
        self.lboxentry()

    def lboxentry(self):
        self.lbox.insert(END, "Principal : " + self.pVar.get() + " Rs., Time : " +
                         self.tVar.get() + " yr/yrs, Rate : " + self.rVar.get() + " %, Interest : " + self.iVar.get() + " Rs.")


root1 = Tk()
root1.geometry("550x370")
b = bCalculator(root1)
root1.mainloop()
