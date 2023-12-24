import tkinter as tk
import math


class CalculatorUtil:
    def __init__(self, geometry):
        self.font = ('TimesNewRoman', 20,'bold')
        self.operator = None

        # Create root
        self.root = tk.Tk()
        self.root.configure(background = 'white')
        self.root.resizable(width=False, height=False)
        self.root.geometry(geometry)
        
        # Frame to hold buttons
        self.calc = tk.Frame(self.root)
        self.calc.grid()


    def display(self, value):
        # Change textdisplay
        self.txtDisplay.delete(0, tk.END)
        self.txtDisplay.insert(0, str(value))


    def createEntryField(self, width=20, columnspan=4):
        self.txtDisplay = tk.Entry(
            self.calc,
            font=(self.font[0], 28, self.font[2]),
            bg='black',
            fg='white',
            bd=21,
            width=width, 
            justify=tk.RIGHT
        )
        self.txtDisplay.grid(row=0, column=0, columnspan=columnspan, padx=0, pady=0)
        self.txtDisplay.insert(0, "0")
    

    def createButton(self, text, command, bg, fg, row, column):
        tk.Button(
            self.calc,
            text = text,
            command = command,
            bg = bg,
            fg = fg,
            width = 6,
			height = 2,
			font = self.font,
            bd = 4
		).grid(row = row, column = column, padx=0, pady = 0)
    

    def numberEnter(self, num):
        # Check if current is empty
        if self.txtDisplay.get() == "0":
            self.display(str(num))
        else:
            self.display(self.txtDisplay.get() + str(num))


    def createNumberPad(self, row, column, numberorder):
        i=0
        for j in range(row, row+3):
            for k in range(column, column+3):
                tk.Button(
                    self.calc,
                    text=numberorder[i],
                    width=6,
                    height=2,
                    bg='black',
                    fg='white',
                    font=self.font,
                    bd=4,
                    command = lambda x=numberorder[i]:self.numberEnter(x)
                ).grid(row=j, column=k, padx=0, pady=0)
                i+=1


    def clearEntry(self):
        self.operator = None
        self.display(0)
    

    def onEnter(self):
        if self.operator is not None:
            self.display(self.operator(float(self.txtDisplay.get())))
            self.operator = None