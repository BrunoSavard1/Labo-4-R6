# 2 for et 2 while 
# au moins 3 input 
# plusieurs print
# 3 if 
# break
#continue
#else (dans une boucle)

import random

class OperatorBanSystem:
    def __init__(self):
        # Liste des opérateurs disponibles dans Rainbow Six Siege
        self.operators = [
            "Ash", "Thermite", "Sledge", "Montagne", "Twitch", "Fuze", "Glaz", "IQ", "Buck", 
            "Blackbeard", "Capitao", "Hibana", "Jackal", "Maverick", "Nomad", "Lion", "Finka", 
            "Amaru", "Kali", "Ace", "Zero", "Oryx", "Aruni", "Sami", "Sofia", "Warden"
        ]
        self.banned_operators = []

    def ban_operator(self, team):
        """Permet à une équipe de bannir un opérateur parmi ceux disponibles avec boucle while pour validation."""
        print(f"\n{team} : Choisissez un opérateur à bannir parmi les suivants :")
        print(self.operators)
        
        # Boucle while pour garantir une entrée valide
        while True:
            banned_operator = input(f"Entrez le nom de l'opérateur à bannir pour {team} : ").strip()
            
            # Vérifier si l'opérateur est valide et disponible
            if banned_operator in self.operators:
                self.operators.remove(banned_operator)
                self.banned_operators.append(banned_operator)
                print(f"{team} a banni l'opérateur {banned_operator}.\n")
                break  # Sortir de la boucle si l'opérateur est valide
            else:
                print(f"{banned_operator} n'est pas un opérateur valide ou a déjà été banni. Essayez encore.")

    def simulate_ban_phase(self):
        """Simule la phase de bannissement des opérateurs pour une partie avec des boucles for et while."""
        print("Phase de bannissement des opérateurs...")

        # Première boucle for pour les deux équipes (Attaque et Défense) bannissant chacun deux opérateurs
        teams = ["Attaque", "Défense"]
        
        # Boucle for pour chaque équipe bannissant un opérateur
        for team in teams:
            self.ban_operator(team)
        
        # Seconde boucle for pour les équipes bannissant encore un autre opérateur
        for team in teams:
            self.ban_operator(team)

        # Afficher les opérateurs bannis
        print("\nLes opérateurs bannis pour cette partie sont :")
        
        # Boucle for pour afficher tous les opérateurs bannis
        for op in self.banned_operators:
            print(f"- {op}")
        
        # Vérification finale si tous les bans sont effectués
        while len(self.banned_operators) < 4:
            print("\nIl manque des bans. Veuillez ajouter un autre opérateur.")
            self.ban_operator("Attaque")  # Par exemple, tu peux redemander à Attaque ou Défense de bannir un opérateur
            break  # La boucle while est un moyen de garantir que le processus ne s'arrête pas tant que les 4 bans ne sont pas faits.

# Exemple d'utilisation du système
if __name__ == "__main__":
    system = OperatorBanSystem()
    system.simulate_ban_phase()



