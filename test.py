# 2 for et 2 while 
# au moins 3 input 
# plusieurs print
# 3 if 
# break
#continue
#else (dans une boucle ) 

# boucle pour permet de recommencer le programme 
while True:
    # défénir les agents disponibles
    agents = ["Ash", "Thermite", "Sledge", "Montagne", "Twitch", "Fuze", "Glaz", "IQ", "Buck", 
    "Blackbeard", "Capitao", "Hibana", "Jackal", "Maverick", "Nomad", "Lion", "Finka", 
    "Amaru", "Kali", "Ace", "Zero", "Oryx", "Aruni", "Sami", "Sofia", "Warden"]
    # deffinir les 2 équipes
    equipes = ["Att", "Def"]
    # liste oppérateur bannis
    ban_agents =[] 
    ban = "Lion"
    # dans la variable ban_agents on stock les agents qui on déja été bannis pour pas les rebannir a nouveau.
    start = input ("veut tu lancer une partie O/N : ")
    if start !="O" :
        exit()
    else :
        print("lancement de la partie")
        # 2 phase pour faire un totale de 4 ban
        for i in range(1, 3) : 
            print(f"\nPhase {i} ")
            for equipe in equipes :
                print(f"\n{equipe} : Choisissez un opérateur à bannir parmi les suivants :")
                print(agents)
                while ban in agents : 
                    
                    ban = input("Entrer un oppérateur a bannir : ")
                    if ban in agents:
                        agents.remove(ban)
                        ban_agents.append(ban)
                        print("Cet oppérateur à été bannis")
                        break
                    # cette boucle permet de vérifier et de mettre un agent dans la variable ban_agents 
                    # .remove enlève l'agent et .append les remets 
                else :
                        print(f"{ban} n'est pas un opérateur valide ou a déjà été banni. Essayez encore.")
                        
                    # temps que les 2 phases ne sont pas finis le programme demande des agents a bannir et break pour sortir de la boucle
                            
                     
        print(f"{ban_agents} Voici les oppérateurs qui on été bannis")            


            
            
                    


