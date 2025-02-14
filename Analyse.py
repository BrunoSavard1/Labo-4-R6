agents = ["Ash", "Thermite", "Sledge", "Montagne", "Twitch", "Fuze", "Glaz", "IQ", "Buck", 
"Blackbeard", "Capitao", "Hibana", "Jackal", "Maverick", "Nomad", "Lion", "Finka", 
"Amaru", "Kali", "Ace", "Zero", "Oryx", "Aruni", "Sami", "Sofia", "Warden"]

# Définir les 2 équipes
equipes = ["Att", "Def"]
# Liste des opérateurs bannis
ban_agents = []

# Lancer la partie
start = input("Veux-tu lancer une partie O/N : ")
if start != "O":
    print("Partie non lancée. Au revoir !")
    exit()
else:
    print("Lancement de la partie...")
    
    # Phase de bannissement : boucle pour chaque phase et chaque équipe
    for phase in range(1, 3):  # Phase 1 et Phase 2
        print(f"\nPhase {phase}")
        
        for equipe in equipes:
            print(f"\n{equipe} : Choisissez un opérateur à bannir parmi les suivants :")
            print(agents)
            
            # Boucle pour permettre à l'équipe de bannir 2 opérateurs
            for _ in range(2):  # Chaque équipe bannit 2 opérateurs
                while True:
                    ban = input("Entrer un opérateur à bannir : ")
                    if ban in agents:  # Si l'opérateur est valide et pas déjà banni
                        agents.remove(ban)
                        ban_agents.append(ban)
                        print(f"{ban} a été banni.")
                        break  # On sort de la boucle pour passer à l'autre opérateur
                    elif ban not in agents:
                        print(f"{ban} n'est pas un opérateur valide ou a déjà été banni. Essayez encore.")
                        continue  # Redemander l'entrée tant qu'elle n'est pas valide
                    else:
                        print("Erreur inattendue. Veuillez réessayer.")
                        break
                if len(ban_agents) == 4:  # Si les 4 opérateurs sont bannis, on arrête
                    break
            else:
                print(f"\nFin de bannissement pour {equipe}.")
    
    print("\nOpérateurs bannis : ", ban_agents)
