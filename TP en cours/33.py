class Vehicule:
    def __init__(self,marque,vitesse):
        self._marque = marque
        self.vitesse = vitesse
    def accelerer(self):
        print(f"{self.marque} accelere")
    def freiner(self):
        print(f"{self.marque} freine")
class Voiture(Vehicule):
    def __init__(self, marque,vitesse,nb_portes):
        super().__init__(marque, vitesse)
        self.nb_portes = nb_portes
    def klaxonner(self):
        print(f"{self.marque} klaxonne")

ma_voiture = Voiture("peugeot", 0, 5)
ma_voiture.accelerer()
ma_voiture.klaxonner()