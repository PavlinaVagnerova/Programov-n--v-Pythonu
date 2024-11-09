import math

# Bonus vytvoření abstraktní třídy
from abc import ABC, abstractmethod
class Property (ABC):
    def __init__(self,locality):
        self.locality = locality

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

# Bonus enum třídy - nedořešeno
import enum
class Estate_type(enum.Enum):
    land = 1
    building_site = 2
    forrest = 3
    garden = 4
di = {}
di[Estate_type.land] = "land"
di[Estate_type.building_site] = "building site"
di[Estate_type.forrest] = "forrest"
di[Estate_type.garden] = "garden"

if di == {Estate_type.land: "land", Estate_type.building_site: "building site", Estate_type.forrest: "forrest", Estate_type.garden: "garden"}:
    print("Typ nemovitosti existuje")
else:
    print("Typ nemovitosti neexistuje.")


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
    # Bonus - doplnění metody __str__
    def __str__(self):
        if self.estate_type == "land":
            return f"Zemědělský pozemek, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        elif self.estate_type == "building site":
            return f"Stavební pozemek, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        elif self.estate_type == "forrest":
            return f"Les, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        else:
            return f"Zahrada, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

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
# Bonus - doplnění metody __str__
    def __str__(self):
        if self.commercial == True:
            return f"Byt nebo dům pro komerční použití, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        else:
            return f"Byt nebo dům pro nekomerční použití, lokalita {self.locality.name} (koeficient {self.locality.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
      
# Bonus - doplnění třídy TaxReport
class TaxReport:
    def __init__(self, name):
        self.name = name
        self.property_list = []
    
    def add_property(self, property_obj):
        self.property_list.append(property_obj)
    
    def calculate_tax(self):
        total_tax = 0
        for item in self.property_list:
            total_tax = total_tax + item.calculate_tax()
        return total_tax

    
manetin = Locality("Manětín", 0.8)
brno = Locality("Brno", 3)

zemedelsky_pozemek = Estate(manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)


print(zemedelsky_pozemek)
print(dum)
print(kancelar)
print(zemedelsky_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())

# Pokračování bonusu - TaxReport
tax_report = TaxReport("Roční daňové přiznání")
tax_report.add_property(zemedelsky_pozemek)
tax_report.add_property(dum)
tax_report.add_property(kancelar)

print(f"Celková daň z nemovitostí je: {tax_report.calculate_tax()} Kč.")


