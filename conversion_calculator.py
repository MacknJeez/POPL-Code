import tkinter as tk
import calculator_util


class ConversionCalculator(calculator_util.CalculatorUtil):
    def __init__(self):
        super().__init__("696x460")
        self.root.title("Conversion Calculator")
        self.createEntryField(14, 3)
        self.converting = False


        # Create the display showing current type
        self.txtUnitDisplay = tk.Entry(
            self.calc,
            font=(self.font[0], 28, self.font[2]),
            bg='black',
            fg='black',
            bd=21,
            width=3, 
            justify=tk.RIGHT
        )
        self.txtUnitDisplay.grid(row=0, column=5, columnspan=1, padx=0, pady=0)
        self.txtUnitDisplay.insert(0, "cm")
        self.txtUnitDisplay.config(state="disabled")


        # Create the special buttons for conversion
        self.unitButton = tk.Button(
            self.calc,
            text = "unit",
            font = self.font,
            command = self.setChangeUnit,
            bg = 'green',
            fg = 'black',
            activebackground="green",
            width = 6,
			height = 2,
            bd = 4,
            relief = "sunken",
            state = "disabled"
		)
        self.unitButton.grid(row = 0, column = 6, padx=0, pady = 0)

        self.convertButton = tk.Button(
            self.calc,
            text = "conv",
            font = self.font,
            command = self.setConvert,
            bg = 'green',
            fg = 'black',
            activebackground="green",
            width = 6,
			height = 2,
            bd = 4
		)
        self.convertButton.grid(row = 0, column = 7, padx=0, pady = 0)


        # Creating Basic Buttons
        self.createNumberPad(1, 0, "789456123")
        self.createButton("0", lambda x=0:self.numberEnter(x), "black", "white", 4, 0)
        self.createButton("C", self.clearEntry, "orange", "black", 4, 1)
        self.createButton(".", self.dot, "orange", "black", 4, 2)


        # Creating Length Buttons
        self.createButton("cm", self.cm, "aquamarine", "black", 1, 5)
        self.createButton("m", self.m, "aquamarine", "black", 2, 5)
        self.createButton("ft", self.ft, "aquamarine", "black", 3, 5)
        self.createButton("mi", self.mi, "aquamarine", "black", 4, 5)


        # Creating Weight Buttons
        self.createButton("g", self.g, "dark slate blue", "black", 1, 6)
        self.createButton("kg", self.kg, "dark slate blue", "black", 2, 6)
        self.createButton("oz", self.oz, "dark slate blue", "black", 3, 6)
        self.createButton("lbs", self.lbs, "dark slate blue", "black", 4, 6)


        # Creating Temprature Buttons
        self.createButton("°C", self.C, "steel blue", "black", 1, 7)
        self.createButton("°F", self.F, "steel blue", "black", 2, 7)
        self.createButton("°K", self.K, "steel blue", "black", 3, 7)
        self.createButton("°R", self.R, "steel blue", "black", 4, 7)
    

    def dot(self):
        if "." not in self.txtDisplay.get():
            self.display(self.txtDisplay.get() + ".")


    def setChangeUnit(self):
        self.converting = False
        self.unitButton.config(relief="sunken", state="disabled")
        self.convertButton.config(relief="raised", state="active")
        pass


    def setConvert(self):
        self.converting = True
        self.convertButton.config(relief="sunken", state="disabled")
        self.unitButton.config(relief="raised", state="active")
        pass
    
    
    def changeUnit(self, newUnit):
        self.txtUnitDisplay.config(state="normal")
        self.txtUnitDisplay.delete(0, tk.END)
        self.txtUnitDisplay.insert(0, newUnit)
        self.txtUnitDisplay.config(state="disabled")


    def cm(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "cm":
                    pass
                case "m":
                    self.display(float(self.txtDisplay.get()) * 100)
                    self.changeUnit("cm")
                case "ft":
                    self.display(float(self.txtDisplay.get()) * 30.48)
                    self.changeUnit("cm")
                case "mi":
                    self.display(float(self.txtDisplay.get()) * 160900)
                    self.changeUnit("cm")
        else:
            self.changeUnit("cm")


    def m(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "cm":
                    self.display(float(self.txtDisplay.get()) / 100)
                    self.changeUnit("m")
                case "m":
                    pass
                case "ft":
                    self.display(float(self.txtDisplay.get()) / 3.281)
                    self.changeUnit("m")
                case "mi":
                    self.display(float(self.txtDisplay.get()) * 1609)
                    self.changeUnit("m")
        else:
            self.changeUnit("m")


    def ft(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "cm":
                    self.display(float(self.txtDisplay.get()) / 30.48)
                    self.changeUnit("ft")
                case "m":
                    self.display(float(self.txtDisplay.get()) * 3.281)
                    self.changeUnit("ft")
                case "ft":
                    pass
                case "mi":
                    self.display(float(self.txtDisplay.get()) * 5280)
                    self.changeUnit("ft")
        else:
            self.changeUnit("ft")


    def mi(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "cm":
                    self.display(float(self.txtDisplay.get()) / 160900)
                    self.changeUnit("mi")
                case "m":
                    self.display(float(self.txtDisplay.get()) / 1609)
                    self.changeUnit("mi")
                case "ft":
                    self.display(float(self.txtDisplay.get()) / 5280)
                    self.changeUnit("mi")
                case "mi":
                    pass
        else:
            self.changeUnit("mi")
    

    def g(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "g":
                    pass
                case "kg":
                    self.display(float(self.txtDisplay.get()) * 1000)
                    self.changeUnit("g")
                case "oz":
                    self.display(float(self.txtDisplay.get()) * 28.35)
                    self.changeUnit("g")
                case "lbs":
                    self.display(float(self.txtDisplay.get()) * 453.6)
                    self.changeUnit("g")
        else:
            self.changeUnit("g")
    

    def kg(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "g":
                    self.display(float(self.txtDisplay.get()) / 1000)
                    self.changeUnit("kg")
                case "kg":
                    pass
                case "oz":
                    self.display(float(self.txtDisplay.get()) / 35.274)
                    self.changeUnit("kg")
                case "lbs":
                    self.display(float(self.txtDisplay.get()) / 2.205)
                    self.changeUnit("kg")
        else:
            self.changeUnit("kg")
    

    def oz(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "g":
                    self.display(float(self.txtDisplay.get()) / 28.35)
                    self.changeUnit("oz")
                case "kg":
                    self.display(float(self.txtDisplay.get()) * 35.274)
                    self.changeUnit("oz")
                case "oz":
                    pass
                case "lbs":
                    self.display(float(self.txtDisplay.get()) * 16)
                    self.changeUnit("oz")
        else:
            self.changeUnit("oz")

    
    def lbs(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "g":
                    self.display(float(self.txtDisplay.get()) / 453.6)
                    self.changeUnit("lbs")
                case "kg":
                    self.display(float(self.txtDisplay.get()) * 2.205)
                    self.changeUnit("lbs")
                case "oz":
                    self.display(float(self.txtDisplay.get()) / 16)
                    self.changeUnit("lbs")
                case "lbs":
                    pass
        else:
            self.changeUnit("lbs")
    

    def C(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "°C":
                    pass
                case "°F":
                    self.display((float(self.txtDisplay.get()) - 32) / 1.8)
                    self.changeUnit("°C")
                case "°K":
                    self.display(float(self.txtDisplay.get()) - 273.15)
                    self.changeUnit("°C")
                case "°R":
                    self.display((float(self.txtDisplay.get()) - 491.67) / 1.8)
                    self.changeUnit("°C")
        else:
            self.changeUnit("°C")
    

    def F(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "°C":
                    self.display((float(self.txtDisplay.get()) * 1.8) + 32)
                    self.changeUnit("°F")
                case "°F":
                    pass
                case "°K":
                    self.display(round(
                        ((float(self.txtDisplay.get()) - 273.15) * 1.8) + 32,
                        10
                    ))
                    self.changeUnit("°F")
                case "°R":
                    self.display(float(self.txtDisplay.get()) - 491.67)
                    self.changeUnit("°F")
        else:
            self.changeUnit("°F")
    

    def K(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "°C":
                    self.display(float(self.txtDisplay.get()) + 273.15)
                    self.changeUnit("°K")
                case "°F":
                    self.display(((float(self.txtDisplay.get()) - 32) / 1.8) + 273.15)
                    self.changeUnit("°K")
                case "°K":
                    pass
                case "°R":
                    self.display(float(self.txtDisplay.get()) / 1.8)
                    self.changeUnit("°K")
        else:
            self.changeUnit("°K")
    

    def R(self):
        if self.converting:
            match self.txtUnitDisplay.get():
                case "°C":
                    self.display(round(
                        (float(self.txtDisplay.get()) * 1.8) + 491.67,
                        10
                    ))
                    self.changeUnit("°R")
                case "°F":
                    self.display(float(self.txtDisplay.get()) + 491.67)
                    self.changeUnit("°R")
                case "°K":
                    self.display(float(self.txtDisplay.get()) * 1.8)
                    self.changeUnit("°R")
                case "°R":
                    pass
        else:
            self.changeUnit("°R")