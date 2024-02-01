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

        
        
        