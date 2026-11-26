def calculer_moyenne(notes):
    if not notes:
        raise ValueError("La liste des notes est vide")
    return sum(notes) / len(notes)

def afficher_resultat(nom, notes):
    moyenne = calculer_moyenne(notes)
    print("Étudiant :", nom)
    print("Moyenne :", moyenne)
    if moyenne >= 10:
        print("Résultat : Admis")
    else:
        print("Résultat : Non admis")

def main():
    notes = [14, 16, 12, 18]
    afficher_resultat("Ahmed", notes)

if __name__ == "__main__":
    main()

def determiner_mention(moyenne):
    if moyenne >= 16:
        return "Très bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"
