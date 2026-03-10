class Vehicule:
    def demarrer(self):
        print("le Véhicule démarre")

class Voiture(Vehicule):
    def demarree(self):
        print("La voiture démarre en douceur"):

class Moto(Vehicule):
    def demarrer(self):
        print("La moto rugit au démarrage!")

        vehicules = [ Voiture(), Moto()]
        for v in vehicules :
            v.demarrer()
    