from abc import ABC, abstractmethod

class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass

# feet to meter
class LengthConversion(UnitConversion):
    def convert(self, value):
        return value * 0.3048 

# gallon to litter
class VolumeConversion(UnitConversion):
    def convert(self, value):
        return value * 3.78541 

# fahrenheit to celsius
class TemperatureConversion(UnitConversion):
    def convert(self, value):
        return (value - 32) * 5/9 
    
# pound to kilogram  
class MassConversion(UnitConversion):
    def convert(self, value):
        return value / 2.20462

class Converter:
    def __init__(self, conversion_type, value):
        self.conversion_type = conversion_type
        self.value = value
    
    def convert(self):
        return self.conversion_type.convert(self.value)

class InputHandler:
    def get_input(self):
        while True:
            try:
                value = float(input("Enter value to convert: "))
                break
            except ValueError:
                print("Invalid input, please try again.")
        return value

class OutputHandler:
    def display_output(self, result):
        print("Result:", result)

class ConversionTypeSelector:
    def __init__(self):
        self.conversions = {
            1: LengthConversion(),
            2: VolumeConversion(),
            3: TemperatureConversion(),
            4: MassConversion()
        }

    def select_conversion_type(self, choice):
        try:
            return self.conversions[choice]
        except KeyError:
            raise ValueError("Invalid choice, please try again.")

def main():
    input_handler = InputHandler()
    value = input_handler.get_input()
    selector = ConversionTypeSelector()
    while True:
        print("Select conversion type:\n1. Feet to meters\n2. Gallons to liters\n3. Fahrenheit to Celsius\n4. Pound to Kilogram")
        try:
            choice = int(input("Enter choice: "))
            conversion_type = selector.select_conversion_type(choice)
            break
        except ValueError as e:
           print(str(e)) 
    converter = Converter(conversion_type, value)
    converter = Converter(conversion_type, value)
    result = converter.convert()
    output_handler = OutputHandler()
    output_handler.display_output(result)

if __name__ == "__main__":
    main()
