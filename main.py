import basic_calculator
import scientific_calculator
import conversion_calculator

if __name__ == "__main__":
    calculatorType = int(input(
        "Type of Calculator:\n"+
        "  0 = Basic\n"+
        "  1 = Scientific\n" +
        "  2 = Conversion"
    ))

    if calculatorType == 1:
        calculator = scientific_calculator.ScientificCalculator()
    elif calculatorType == 2:
        calculator = conversion_calculator.ConversionCalculator()
    else:
        calculator = basic_calculator.BasicCalculator()
    calculator.root.mainloop()