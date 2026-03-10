class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}ans"
        
personne1 =Personne("Halima", 20)
print(personne1.se_presenter())