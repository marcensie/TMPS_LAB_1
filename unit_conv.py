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

# input output
class UserInterface:
    def get_input(self):
        while True:
            try:
                value = float(input("Enter value to convert: "))
                break
            except ValueError:
                print("Invalid input, please try again.")
        return value
    
    def get_conversion_type(self):
        while True:
            print("Select conversion type:\n1. Feet to meters\n2. Gallons to liters\n3. Fahrenheit to Celsius\n4. Pound to Kilogram")
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    return LengthConversion()
                elif choice == 2:
                    return VolumeConversion()
                elif choice == 3:
                    return TemperatureConversion()
                elif choice == 4:
                    return MassConversion()
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please try again.")
    
    def display_output(self, result):
        print("Result:", result)

def main():
    ui = UserInterface()
    value = ui.get_input()
    conversion_type = ui.get_conversion_type()
    converter = Converter(conversion_type, value)
    result = converter.convert()
    ui.display_output(result)

if __name__ == "__main__":
    main()
