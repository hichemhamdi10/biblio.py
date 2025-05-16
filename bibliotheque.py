import json

def charger_bibliotheque(fichier="bibliotheque.json"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def sauvegarder_bibliotheque(bibliotheque, fichier="bibliotheque.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, indent=4, ensure_ascii=False)

def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return

    print("\n Liste des livres :")
    for livre in bibliotheque:
        statut = "Lu" if livre["Lu"] else "Non lu"
        print(f'ID: {livre["ID"]} | {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) - {statut}')

def ajouter_livre(bibliotheque):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = int(input("Année de publication : "))
    nouvel_id = max([livre["ID"] for livre in bibliotheque], default=0) + 1
    livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None,
        "Commentaire": ""
    }
    bibliotheque.append(livre)
    print("Livre ajouté avec succès.")

def supprimer_livre(bibliotheque):
    id_suppr = int(input("donne moi ID du livre à supprimer : "))
    for livre in bibliotheque:
        if livre["ID"] == id_suppr:
            confirmation = input(f"Supprimer {livre['Titre']} ? (o/n) : ").lower()
            if confirmation == 'o':
                bibliotheque.remove(livre)
                print("Livre supprimé.")
                return
    print("Livre non trouvé.")

def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé (titre ou auteur) : ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]
    afficher_livres(resultats)

def marquer_lu(bibliotheque):
    id_livre = int(input("ID du livre lu : "))
    for livre in bibliotheque:
        if livre["ID"] == id_livre:
            livre["Lu"] = True
            livre["Note"] = int(input("Note sur 10 : "))
            livre["Commentaire"] = input("Commentaire : ")
            print(" Livre marqué comme lu.")
            return
    print("Livre non trouvé.")

def afficher_filtre(bibliotheque, lu=True):
    livres = [livre for livre in bibliotheque if livre["Lu"] == lu]
    afficher_livres(livres)

def trier_livres(bibliotheque):
    if not bibliotheque:
        print(" La bibliothèque est vide.")
        return

    correspondance_cles = {
        "annee": "Année",
        "auteur": "Auteur",
        "note": "Note"
    }

    critere = input("Trier par (annee / auteur / note) : ").lower()

    if critere in correspondance_cles:
        vraie_cle = correspondance_cles[critere]
        livres_tries = sorted(
            bibliotheque,
            key=lambda x: x[vraie_cle] if x[vraie_cle] is not None else -1
        )
        print(f"\n📊 Livres triés par {critere} :")
        afficher_livres(livres_tries)
    else:
        print(" Critère invalide. Choisis : annee, auteur ou note.")

def menu():
    print("""
===== MENU BIBLIOTHÈQUE =====
1. Afficher tous les livres
2. Ajouter un livre
3. Supprimer un livre
4. Rechercher un livre
5. Marquer un livre comme lu
6. Afficher les livres lus
7. Afficher les livres non lus
8. Trier les livres
9. Quitter
""")

def main():
    bibliotheque = charger_bibliotheque()
    while True:
        menu()
        choix = input("Choix : ")
        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_lu(bibliotheque)
        elif choix == "6":
            afficher_filtre(bibliotheque, True)
        elif choix == "7":
            afficher_filtre(bibliotheque, False)
        elif choix == "8":
            trier_livres(bibliotheque)
        elif choix == "9":
            sauvegarder_bibliotheque(bibliotheque)
            print("Données sauvegardées.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()