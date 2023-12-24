import math
import basic_calculator


class ScientificCalculator(basic_calculator.BasicCalculator):
    def __init__(self):
        super().__init__("812x460")
        self.root.title("Scientific Calculator")

        # Creating Scientific Operation Buttons
        self.createButton(".", self.dot, "orange", "black", 0, 4)
        self.createButton("^", self.power, "aquamarine", "black", 1, 4)
        self.createButton("%", self.modulo, "aquamarine", "black", 2, 4)
        self.createButton("log10", self.log10, "aquamarine", "black", 3, 4)
        self.createButton("ln", self.loge, "aquamarine", "black", 4, 4)

        self.createButton("π", self.pi, "green", "black", 0, 5)
        self.createButton("!", self.fact, "aquamarine", "black", 1, 5)
        self.createButton("sin", self.sin, "aquamarine", "black", 2, 5)
        self.createButton("cos", self.cos, "aquamarine", "black", 3, 5)
        self.createButton("tan", self.tan, "aquamarine", "black", 4, 5)

        self.createButton("e", self.e, "green", "black", 0, 6)
        self.createButton("abs", self.abs, "aquamarine", "black", 1, 6)
        self.createButton("sec", self.sec, "aquamarine", "black", 2, 6)
        self.createButton("cosec", self.cosec, "aquamarine", "black", 3, 6)
        self.createButton("cot", self.cot, "aquamarine", "black", 4, 6)


    def dot(self):
        if "." not in self.txtDisplay.get():
            self.display(self.txtDisplay.get() + ".")


    def power(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) ** x
        self.display(0)
    

    def modulo(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) % x
        self.display(0)
    

    def log10(self):
        self.operator = None
        self.display(math.log10(float(self.txtDisplay.get())))
    

    def loge(self):
        self.operator = None
        self.display(math.log(float(self.txtDisplay.get())))
    

    def fact(self):
        self.operator = None
        self.display(math.factorial(int(self.txtDisplay.get())))
    

    def pi(self):
        if self.operator == None:
            self.display(math.pi)
        else:
            self.display(self.operator(math.pi))


    def sin(self):
        self.operator = None
        self.display(math.sin(math.radians(float(self.txtDisplay.get()))))


    def cos(self):
        self.operator = None
        self.display(math.cos(math.radians(float(self.txtDisplay.get()))))
    

    def tan(self):
        self.operator = None
        self.display(math.tan(math.radians(float(self.txtDisplay.get())))) 
    

    def e(self):
        if self.operator == None:
            self.display(math.e)
        else:
            self.display(self.operator(math.e))
    

    def abs(self):
        self.operator = None
        self.display(abs(float(self.txtDisplay.get())))
    

    def sec(self):
        self.operator = None
        self.display(1/math.sin(math.radians(float(self.txtDisplay.get()))))
    

    def cosec(self):
        self.operator = None
        self.display(1/math.cos(math.radians(float(self.txtDisplay.get()))))
    

    def cot(self):
        self.operator = None
        self.display(1/math.tan(math.radians(float(self.txtDisplay.get())))) 