##Suzette Irizarry
##File: M03_LabCarClasses
##This program is meant to get user input about the car that they have
##and to store that information in the variables

###Vehicle() - is the parent class
###vehicle_type - is a user input for the type of vehicle they have
###Year - is the year of the vehicle
###Make - the make of the vehicle
###Model - the model of the vehicle
###Doors - how many doors the vehicle has
###Roof - what kind of roof the vehicle has
###Automobile - is the child class of Vehicle class, it inherits the variables of the parent 

class Vehicle():
    def __init__(self, vehicle_type) -> None:
        self.vehicle_type: str = vehicle_type
        
    def vehicleType(self) -> str:
        return self.vehicle_type
    
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors
        self.roof: str = roof
        
    def Year(self) -> int:
        return self.year
    
    def Make(self) -> str:
        return self.make
    
    def Model(self) -> str:
        return self.model
    
    def Doors(self) -> int:
        return self.doors
    
    def Roof(self) -> str:
        return self.roof
    
vehicleType: input("Vehicle type:")
Year: int(input("Year:"))
Make: input("Make:")
Model: input("Model:")
Doors: int(input("Number of doors:"))
Roof: input("Type of roof:")

        
        
        
        