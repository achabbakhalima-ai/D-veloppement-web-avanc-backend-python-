donnees = [
 ("Sara", "Math", 12, "G1"),
 ("Sara", "Info", 14, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Adam", "Chimie", 18, "G1"),
 ("Sara", "Math", 11, "G1"),
 ("Bouchra", "Info", "abc", "G2"),
 ("", "Math", 10, "G1"),
 ("Yassine", "Info", 22, "G2"),
 ("Ahmed", "Info", 13, "G2"),
 ("Adam", "Math", None, "G1"),
 ("Sara", "Chimie", 16, "G1"),
 ("Adam", "Info", 7, "G1"),
 ("Ahmed", "Math", 9, "G2"),
 ("Hana", "Physique", 15, "G3"),
 ("Hana", "Math", 8, "G3"),
]

#partie 1:Nettoyage et validation
def valider(enregistement):
    nom, matière, note, groupe = enregistement 
    if not nom and isinstance(nom, str):
        return (False, "Nom invalide")
    if not matière or not isinstance(matière, str):
        return (False, "Matière invalide")
    if not groupe or not isinstance(groupe, str):
        return (False, "Groupe invalide")
    try:
        note = float(note)
    except:
        return (False, "Note invalide")
    if note < 0 or note > 20 :
        return (False, "Note doit etre entre 0 et 20")
    return ( True, "")
valides = []
erreurs = []
doublons_exact = set()
vus = set()
for enregistement in donnees:
    if enregistement in vus:
        doublons_exact.add(enregistement)
    else:
        vus.add(enregistement)
    valide, raison = valider(enregistement)
    if valide:
        nom, matiere, note, groupe = enregistement
        note = float(note)
        valides.append(enregistement)
    else:
        erreurs.append({ "enregistement": enregistement, "raison": raison })

#partie 2:  Structuration
matières = set()
for nom, matière, note, groupe in valides:
    matières.add(matière)
etudiants = {}
for nom, matière, note, groupe in valides:
    if nom not in etudiants:
        etudiants[nom] = {}
    if matière not in etudiants[nom]:
        etudiants[nom][matière] = []
    etudiants[nom][matière].append(note)
groupes = {}
for nom , matière, note, grpoupe  in valides:
    if groupe not in groupes :
        groupes[groupe]=set()
    groupes[groupe].add(nom)

#partie 3 : : Calculs et statistiques
def somme_recursive(notes):
    if not notes:
        return 0 
    return notes[0] + somme_recursive(notes[1:])
def moyenne (notes):
    if not notes:
        return 0
    return somme_recursive(notes) / len(notes)
moyennes_par_matière= {}
for nom, matières in etudiants.items():
    moyennes_par_matière[nom] = {}
    for matière, notes in matières.items():
        moyennes_par_matière[nom][matière] = moyenne(notes)
moyenne_generale ={}
for nom, matieres in etudiants.items():
    toutes_les_notes = []
    for notes in matieres.values():
        toutes_les_notes.extend(notes)  
    moyenne_generale[nom] = moyenne(toutes_les_notes)

# partie 4 : Analyse avancée et détection d’anomalies
alertes = {
    "doublons_notes": [],        # étudiants avec plusieurs notes dans la même matière
    "profil_incomplet": [],      # étudiants n'ayant pas toutes les matières
    "moyenne_faible_groupes": [],# groupes avec moyenne générale faible
    "ecart_notes": []            # étudiants avec gros écart entre note max et min
}
for nom, matieres in etudiants.items():
    for matiere, notes in matieres.items():
        if len(notes) > 1:
            alertes["doublons_notes"].append({
                "etudiant": nom,
                "matiere": matiere,
                "notes": notes
            })
for nom, matieres_etudiant in etudiants.items():
    matieres_absentes = matieres - set(matieres_etudiant.keys())
    if matieres_absentes:
        alertes["profil_incomplet"].append({
            "etudiant": nom,
            "matieres_manquantes": list(matieres_absentes)
        })
SEUIL_MOYENNE = 10  # par exemple, seuil faible

for groupe, etudiants_du_groupe in groupes.items():
    toutes_les_notes = []
    for etu in etudiants_du_groupe:
        for notes in etudiants[etu].values():
            toutes_les_notes.extend(notes)
    if toutes_les_notes:
        moyenne_groupe = moyenne(toutes_les_notes)
        if moyenne_groupe < SEUIL_MOYENNE:
            alertes["moyenne_faible_groupes"].append({
                "groupe": groupe,
                "moyenne": moyenne_groupe
            })

SEUIL_ECART = 10

for nom, matieres_etudiant in etudiants.items():
    toutes_les_notes = []
    for notes in matieres_etudiant.values():
        toutes_les_notes.extend(notes)
    if toutes_les_notes:
        ecart = max(toutes_les_notes) - min(toutes_les_notes)
        if ecart > SEUIL_ECART:
            alertes["ecart_notes"].append({
                "etudiant": nom,
                "notes": toutes_les_notes,
                "ecart": ecart
            })


