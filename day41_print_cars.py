class Ford:

    def __init__(self,model,color,year,transmission,electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    def print_cars(self):
        print(f"car_model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")

class BMW:
    
    def __init__(self,model,color,year,transmission,electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
        
    def print_cars(self):
        print(f"car_model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")

class Tesla:
    
    def __init__(self,model,color,year,transmission,electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
        
    def print_cars(self):
        print(f"car_model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")
    
ford1 = Ford("focus","white",2020,"Auto",False)
bmw1 = BMW("x6","silver",2018,"Auto",False)
tesla1 = Tesla("S","beige",2017,"Auto",True)

ford1.print_cars()
    