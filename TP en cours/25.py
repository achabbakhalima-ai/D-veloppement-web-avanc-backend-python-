class Personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}ans"
    
personne1 = Personne('Alice', 28, 'alice@email.com')
print(f"Nom: {personne1.nom}")
print(f"Âge: {personne1.age}")
print(f"Email: {personne1.email}")

personne1.nom =' Alice DUbois'
personne1.age+=1
personne1.email = 'alice.dubois@email.com'

print(f"Nouveau nom: {personne1.nom}")
print(f"Nouveau age: {personne1.age}")
