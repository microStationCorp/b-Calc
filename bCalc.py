from tkinter import *
from tkinter import messagebox as mbox


class bCalculator:

    def __init__(self, root):
        root.title("bussiness calculator")

        frame = Frame(root)
        frame.pack(side=LEFT, padx=20, pady=20)

        self.pVar = StringVar()
        Label(frame, text="principal : ").grid(row=0, column=0, sticky=E)
        self.pEntry = Entry(frame, textvariable=self.pVar)
        self.pEntry.grid(row=0, column=1, pady=2)

        self.tVar = StringVar()
        Label(frame, text="time : ").grid(row=1, column=0, sticky=E)
        self.tEntry = Entry(frame, textvariable=self.tVar)
        self.tEntry.grid(row=1, column=1, pady=2)

        self.rVar = StringVar()
        Label(frame, text="rate : ").grid(row=2, column=0, sticky=E)
        self.rEntry = Entry(frame, textvariable=self.rVar)
        self.rEntry.grid(row=2, column=1, pady=2)

        self.iVar = StringVar()
        Label(frame, text="interest : ").grid(row=3, column=0, sticky=E)
        self.iEntry = Entry(frame, textvariable=self.iVar)
        self.iEntry.grid(row=3, column=1, pady=2)

        Label(frame, text="total Amount : ").grid(row=4, column=0, sticky=E)
        self.piEntry = Entry(frame)
        self.piEntry.grid(row=4, column=1, pady=2)

        bframe = Frame(root)
        bframe.pack(side=LEFT)

        self.bResult = Button(bframe, text="click", width=5, height=3, command=self.get_data)
        self.bResult.grid(row=0, column=0)

    def get_data(self):
        if self.pVar.get() != "":
            try:
                self.pdata = int(self.pVar.get())
                mbox.showinfo("Info", "all good")
            except ValueError:
                mbox.showerror("error", "enter a valid number")
                self.pEntry.delete(0, END)
        else:
            mbox.showwarning("warning", "enter a data")


root1 = Tk()
root1.geometry("400x200")
b = bCalculator(root1)
root1.mainloop()
