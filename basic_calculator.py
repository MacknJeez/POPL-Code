import calculator_util


class BasicCalculator(calculator_util.CalculatorUtil):
    def __init__(self, geometry = "464x456"):
        super().__init__(geometry)
        self.root.title("Basic Calculator")
        self.createEntryField()

        # Creating Basic Buttons
        self.createNumberPad(1, 0, "789456123")
        self.createButton("0", lambda x=0:self.numberEnter(x), "black", "white", 4, 0)
        self.createButton("C", self.clearEntry, "orange", "black", 4, 1)
        self.createButton("=", self.onEnter, "orange", "black", 4, 2)

        # Creating Basic Operation Buttons
        self.createButton("+", self.addition, "aquamarine", "black", 1, 3)
        self.createButton("-", self.subtraction, "aquamarine", "black", 2, 3)
        self.createButton("*", self.multiplication, "aquamarine", "black", 3, 3)
        self.createButton("/", self.division, "aquamarine", "black", 4, 3)


    def addition(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) + x
        self.display(0)
    
    def subtraction(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) - x
        self.display(0)

    def multiplication(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) * x
        self.display(0)
    
    def division(self):
        curr = self.txtDisplay.get()
        self.operator = lambda x: float(curr) / x
        self.display(0)