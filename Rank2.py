while True:
    # Définir les agents disponibles
    agents = ["Ash", "Thermite", "Sledge", "Montagne", "Twitch", "Fuze", "Glaz", "IQ", "Buck", 
              "Blackbeard", "Capitao", "Hibana", "Jackal", "Maverick", "Nomad", "Lion", "Finka", 
              "Amaru", "Kali", "Ace", "Zero", "Oryx", "Aruni", "Sami", "Sofia", "Warden"]
    
    # Définir les 2 équipes
    equipes = ["Att", "Def"]
    
    # Liste des opérateurs bannis
    ban_agents = []
    
    start = input("Veux-tu lancer une partie O/N : ")
    if start != "O":
        print("Fermeture du programme.")
        break  # Quitter la boucle si l'utilisateur ne veut pas lancer une partie
    else:
        print("Lancement de la partie...")

        # 2 phases pour faire un total de 4 bans
        for i in range(1, 3):
            print(f"\nPhase {i}")
            
            # Chaque équipe choisit un opérateur à bannir
            for equipe in equipes:
                print(f"\n{equipe} : Choisissez un opérateur à bannir parmi les suivants :")
                print(agents)
                
                while True:  # Tant que les agents sont disponibles à bannir
                    ban = input("Entrer un opérateur à bannir : ")
                    
                    # Si l'opérateur est valide et disponible
                    if ban in agents:
                        agents.remove(ban)
                        ban_agents.append(ban)
                        print(f"L'opérateur {ban} a été banni.")
                        break  # Sortir de la boucle après un bannissement réussi
                    
                    # Si l'opérateur a déjà été banni
                    elif ban in ban_agents:
                        print(f"{ban} a déjà été banni. Veuillez en choisir un autre.")
                        continue  # Demander à nouveau un opérateur
                    
                    # Si l'opérateur est invalide
                    else:
                        print(f"{ban} n'est pas un opérateur valide. Essayez encore.")
                        continue  # Demander à nouveau un opérateur

        # Afficher les agents bannis à la fin de la partie
        print(f"\nVoici les opérateurs bannis au total : {ban_agents}")
    
    # Demander si l'utilisateur veut relancer une autre partie
    replay = input("Veux-tu relancer une autre partie O/N : ")
    if replay != "O":
        print("Fin de la partie.")
        break  # Quitter la boucle principale si l'utilisateur ne veut plus continuer
