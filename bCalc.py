from tkinter import *
from tkinter import messagebox as mbox


class bCalculator:

    def __init__(self, root):
        #........................design..........................
        root.title("bussiness calculator")

        frame = Frame(root)
        frame.pack(side=LEFT, padx=20, pady=20)

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

        bframe = Frame(root)
        bframe.pack(side=LEFT)

        self.bResult = Button(bframe, text="click", width=5, bd=5, height=3, command=lambda: self.mainFunc(
            self.pVar, self.tVar, self.rVar, self.iVar))
        self.bResult.grid(row=0, column=0)

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
        pri = (inter * 100) / (tim * rat)
        self.pEntry.insert(END, pri)
    #...............interest calculation..............

    def iCal(self):
        pri = float(self.pVar.get())
        tim = float(self.tVar.get())
        rat = float(self.rVar.get())
        inter = (pri * tim * rat) / 100
        self.iEntry.insert(END, inter)
    #.............time calculation..................

    def tCal(self):
        pri = float(self.pVar.get())
        inter = float(self.iVar.get())
        rat = float(self.rVar.get())
        tim = (inter * 100) / (pri * rat)
        self.tEntry.insert(END, tim)

    #................rate calculation...............
    def rCal(self):
        pri = float(self.pVar.get())
        inter = float(self.iVar.get())
        tim = float(self.tVar.get())
        rat = (inter * 100) / (pri * tim)
        self.rEntry.insert(END, rat)


root1 = Tk()
root1.geometry("300x150")
b = bCalculator(root1)
root1.mainloop()
