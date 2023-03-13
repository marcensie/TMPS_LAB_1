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
### OCP:The UnitConversion interface is open for extension (new conversion types can be added) but closed for modification, LengthConversion, VolumeConversion, TemperatureConversion, MassConversion classes each extend the UnitConversion.
```
class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass

class LengthConversion(UnitConversion):
    def convert(self, value):
        return value * 0.3048 
```
### LSP:The LengthConversion, VolumeConversion, TemperatureConversion, MassConversion classes can be used as a substitute for the UnitConversion class without affecting the correctness of the program.
```
class UnitConversion(ABC):
    @abstractmethod
    def convert(self, value):
        pass
 
 class VolumeConversion(UnitConversion):
    def convert(self, value):
        return value * 3.78541 
        
  choice = int(input("Enter choice: "))
                if choice == 1:
                    return LengthConversion()
                elif choice == 2:
                    return VolumeConversion()
                elif choice == 3:
                    return TemperatureConversion()
                elif choice == 4:
                    return MassConversion()
        
```
### ISP:

### DIP:




