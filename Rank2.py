# 2 for et 2 while 
# au moins 3 input 
# plusieurs print
# 3 if 
# break
#continue
#else (dans une boucle ) 
# défénir les agents disponibles
agents = ["Ash", "Thermite", "Sledge", "Montagne", "Twitch", "Fuze", "Glaz", "IQ", "Buck", 
"Blackbeard", "Capitao", "Hibana", "Jackal", "Maverick", "Nomad", "Lion", "Finka", 
"Amaru", "Kali", "Ace", "Zero", "Oryx", "Aruni", "Sami", "Sofia", "Warden"]
# deffinir les 2 équipes
equipes = ["Att", "Def"]
# liste oppérateur bannis
ban_agents =[] 
start = input ("veut tu lancer une partie O/N : ")
if start !="O" :
    exit()
else :
    print("lancement de la partie")
    for i in range(1, 2) : 
        print(f"\nPhase {i} ")
        for equipe in equipes :
            print(f"\n{equipe} : Choisissez un opérateur à bannir parmi les suivants :")
            print(agents)
            while True : 
                ban = input("Entrer un oppérateur a bannir : ")
                if ban in agents:
                    agents.remove(ban)
                    ban_agents.append(ban)
                    print("Cet oppérateur à été bannis")
                    break
                else :
                    print(f"{ban} n'est pas un opérateur valide ou a déjà été banni. Essayez encore.")
            
            
                    


