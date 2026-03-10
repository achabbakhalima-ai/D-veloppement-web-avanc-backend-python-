class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def afficher_infos(self):
        print(f"Nom: {self.nom}, Âge: {self.age}")

class Etudiant(Personne):
    def __init__(self, nom, age, cne, notes):
        Personne.__init__(self,nom, age)
        self.cne = cne
        self.notes = notes
    def calculer_moyenne(self):
        if len(self.notes) == 0:
            return 0
        return sum(self.notes) / len(self.notes)
    def afficher_infos(self):
        super().afficher_infos()
        print(f"CNE:{self.cne}, Notes:{self.notes} ")

class Salarie(Personne):
    def __init__(self, nom, age, numero_somme, salaire):
        Personne.__init__(self,nom, age)
        self.numero_somme = numero_somme
        self.salaire = salaire
    def calculer_salaire(self):
        return self.salaire
    def afficher_infos(self):
        super().afficher_infos()
        print(f"Numéro Somme:{self.numero_somme}, Salaire: {self.salaire}")



class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, numero_somme, salaire, cne, notes):
        Salarie.__init__(self, nom, age, numero_somme, salaire)
        Etudiant.__init__(self, nom, age, cne, notes)
    def afficher_infos(self):
        Salarie.afficher_infos(self)
        Etudiant.afficher_infos(self)



notes = [17, 16, 15]

d = Doctorant("Mohamed",28,"1314", 5000,"M7894262145",notes)
d.afficher_infos()