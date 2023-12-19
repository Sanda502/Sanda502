
print("Bienvenue dans notre système de gestion des comptes utilisateurs")


with open("comptes.txt", "r+") as fichier_comptes:
   
    comptes_existants = fichier_comptes.readlines()
    dernier_numero = len(comptes_existants) + 1

    choix = input("Voulez-vous :\n1. Créer un nouveau compte\n2. Utiliser un compte existant\n3. Accéder en tant qu'administrateur\n")
    
    # Option 1: Créer un nouveau compte
    if choix == '1':
        nom_utilisateur = input("Entrez un nom d'utilisateur : ")
        mot_de_passe = input("Entrez un mot de passe : ")
        compte = f"nom:{nom_utilisateur} mot de passe:{mot_de_passe}"
        if any(nom_utilisateur in compte for compte in comptes_existants):
            print("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        else:
            fichier_comptes.write(str(dernier_numero) + " " + compte + "\n")
            print("Le compte a été créé avec succès. Votre numéro de compte est " + str(dernier_numero))
    
    # Option 2: Utiliser un compte existant
    elif choix == '2':
        num_utilisateur = input("Entrez le numéro de votre compte : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        if any((f"{num_utilisateur} nom:" in compte) and (f"mot de passe:{mot_de_passe}" in compte) for compte in comptes_existants):
            print("Bienvenue sur votre compte.")
        else:
            print("Numéro de compte ou mot de passe incorrect. Veuillez créer un nouveau compte ou réessayer.")
    
    # Option 3: Accès administrateur
    elif choix == '3':
        mot_de_passe_admin = input("Entrez le mot de passe administrateur : ")
        if mot_de_passe_admin == "Sarobidy@5866":
            print("Accès administrateur autorisé. Voici la liste des comptes :")
            for numero, compte in enumerate(comptes_existants, start=1):
                print(f"{numero}: {compte.strip()}")
        else:
            print("Mot de passe administrateur incorrect.")
