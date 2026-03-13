# TP : Système de gestion de boissons

## Description
Ce projet implémente un petit système de gestion de boissons pour un café.  
Il permet de :

- Créer des boissons (Café, Thé)  
- Ajouter des ingrédients (Lait, Sucre, Caramel) via le pattern décorateur  
- Combiner des boissons  
- Gérer des clients et leurs points de fidélité  
- Passer des commandes sur place ou à emporter  

---

## Organisation des fichiers
```bat
tp_boissons/
│
├── boissons.py # Classes Boisson, Cafe, The, BoissonCombinee
├── ingredients.py # Décorateurs Lait, Sucre, Caramel
├── client.py # Data class Client
├── fidelite.py # Classe Fidelite
├── commandes.py # Commande, CommandeSurPlace, CommandeEmporter, CommandeFidele
├── main.py # Exemple d'utilisation
└── README.md

```
---


## 3. Fonctionnalités principales

1. Créer et enrichir des boissons avec des ingrédients.
2. Combiner deux boissons avec l’opérateur `+`.
3. Créer des clients et suivre leur fidélité.
4. Passer une commande, ajouter plusieurs boissons et calculer le prix total.
5. Afficher le contenu complet de la commande avec description, prix et points de fidélité.

---

## Exemple d’utilisation

```python
from boissons import Cafe, The
from ingredients import Lait, Sucre, Caramel
from commandes import CommandeFidele
from client import Client

client = Client("Ali", 1)

cafe = Cafe()
cafe = Lait(cafe)
cafe = Sucre(cafe)

the = The()
the = Caramel(the)

menu = cafe + the

commande = CommandeFidele(client)
commande.ajouter_boisson(cafe)
commande.ajouter_boisson(the)
commande.ajouter_boisson(menu)

commande.afficher()
commande.valider()

print("Points fidélité du client :", client.points)
