# TMPS_LAB_1 - Unit Converter App 
## by Jardan Alexandru

## Description :
I created a Unit Converter app that follows SOLID principles.

### SRP: The LengthConversion, VolumeConversion, TemperatureConversion, MassConversion classes each have a single responsibility of performing a specific type of unit conversion. The Converter class has a single responsibility of converting a value using a given conversion type.
```
class TemperatureConversion(UnitConversion):
    def convert(self, value):
        return (value - 32) * 5/9 
        
class MassConversion(UnitConversion):
    def convert(self, value):
        return value / 2.20462

class Converter:
    def __init__(self, conversion_type, value):
        self.conversion_type = conversion_type
        self.value = value
    
    def convert(self):
        return self.conversion_type.convert(self.value)

```
### OCP: The UnitConversion interface is open for extension (new conversion types can be added) but closed for modification, LengthConversion, VolumeConversion, TemperatureConversion, MassConversion classes each extend the UnitConversion.
```
class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass

class LengthConversion(UnitConversion):
    def convert(self, value):
        return value * 0.3048 
```
### LSP: The LengthConversion, VolumeConversion, TemperatureConversion, MassConversion classes can be used as a substitute for the UnitConversion class without affecting the correctness of the program.
```
class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass
 
 class VolumeConversion(UnitConversion):
    def convert(self, value):
        return value * 3.78541 
```
### ISP: Each class has only the methods it needs, and no unnecessary methods or dependencies are added.
```
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
```

### DIP: The Converter class depends on the UnitConversion abstract class and not on its concrete implementations. This is achieved through the use of dependency injection in the Converter constructor, where an instance of a concrete subclass of UnitConversion is passed as an argument.
```
class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass

class Converter:
    def __init__(self, conversion_type, value):
        self.conversion_type = conversion_type
        self.value = value
    
    def convert(self):
        return self.conversion_type.convert(self.value)
        
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
```

