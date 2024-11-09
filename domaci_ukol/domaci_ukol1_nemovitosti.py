import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient


class Property:
    def __init__(self,locality):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
    
    def calculate_tax(self):
        if self.estate_type == "land":
            tax = self.area*0.85*self.locality.locality_coefficient
        elif self.estate_type == "building site":
            tax = self.area*9*self.locality.locality_coefficient
        elif self.estate_type == "forrest":
            tax = self.area*0.35*self.locality.locality_coefficient
        else:
            tax = self.area*2*self.locality.locality_coefficient
        return math.ceil(tax)

class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        if self.commercial == True:
            tax = self.area * self.locality.locality_coefficient * 15 * 2
        else: 
            tax = self.area * self.locality.locality_coefficient * 15
        return math.ceil(tax)


manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

print(zemedelsky_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())

