import os

class Fahrzeug:
    Fahrzeug_count = 0
    def __init__(self, marke, modell, ps):
        type(self).Fahrzeug_count +=1
        self.marke = marke
        self.modell = modell
        self.ps = ps
    def __del__(self):
        type(self).Fahrzeug_count -= 1
    def __str__(self):
         return f"{self.marke=}, {self.modell=},{self.ps=}"
os.system("cls")


vw = Fahrzeug("VW", "Gold", 90)
print(vw)
print(f"Anzahl der Instanzen: {Fahrzeug.Fahrzeug_count}")
Porsche = Fahrzeug("porsche", "911", 500)
print(Porsche)
print(f"Anzahl der Instanzen: {Fahrzeug.Fahrzeug_count}")
del vw
print(f"Anzahl der Instanzen: {Fahrzeug.Fahrzeug_count}")
del Porsche
print(f"Anzahl der Instanzen: {Fahrzeug.Fahrzeug_count}")