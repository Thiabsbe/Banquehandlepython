class CompteBanquaire:

    def __init__(self,proprietaire,solde):

        self.__proprietaire = proprietaire
        self.__solde = solde
    
    def afficher_info(self):
        print(f"{self.__proprietaire} - {self.__solde}")
    
    def deposer(self, montant):
        self.__solde += montant
        print(f" Vous avez fait un dépot de {montant}cfa - Nouveau solde : {self.__solde}")
        
    def retirer(self,montant):
        if self.__solde >= montant:
            self.__solde -= montant
            print(f"vous avez fait un retrait de {montant} - Nouveau solde: {self.get_solde()}")
        else:
            print("Solde insuffisant")
    
    def get_solde(self):
        return self.__solde
    
    def set_solde(self, nouveau_solde):
        self.__solde = nouveau_solde
    
    def __str__(self):
        return f"Compte de {self.__proprietaire} -{self.__solde}£"
        


class CompteEpargne(CompteBanquaire):

    def __init__(self, proprietaire, solde,taux_interet):
        super().__init__(proprietaire, solde)
        self.taux_interet = taux_interet
    
    def appliquer_interet(self):
        
        solde = self.get_solde()
        interet = (solde * self.taux_interet)/100
        self.set_solde(solde+interet)

        print(f"Nouveau solde après intérêt : {self.get_solde()}")



class ComptePayant(CompteBanquaire):

    def __init__(self, proprietaire, solde,frais_retrait):
        super().__init__(proprietaire, solde)
        self.frais_retrait=frais_retrait

    def retirer(self, montant):
        solde = self.get_solde()

        if solde >= (montant + self.frais_retrait):
            self.set_solde(solde -montant )
            print(f"Vous avez retirer {montant} - Nouveau Solde: {solde}")
        
        else:
            print("Solde Insuffisant")


# MENU INTERACTIF

comptes = []

while True:
    print(" Bienvenu dans ta console de gestion de compte Bancaire")

    print("-----------------------------------------------------------------")

    print("""
        ==== MENU ===
        1. Créer un Compte
        2. Afficher les infos d'un compte
        3. Déposer
        4. Retirer
        5. Appliquer intérêt
        6. Quitter
          """)
    
    """  print("Liste des compte")
    with open("compte.txt","r") as f:
        for ligne in f:
            print(ligne.strip()) """

    
   
    try:
        

        choix = int(input("Veuiilez indiquez votre choix: "))
        if choix == 1:
            proprio = input("Merci de renseigner  le nom du propriétaire du compte: ")
            solde_compte = float(input("Renseigner le solde: "))
            type_compte = int(input("""Choisissez le type de compte
                                1 = CompteBancaire
                                2 = Compte Epargne
                                3 = Compte Payant  : """))
            
            if type_compte == 1:
                compte = CompteBanquaire(proprio,solde_compte)
            
            if type_compte == 2:
                taux_intêré= float(input("Renseinger le taux d'intérêt: "))
                compte = CompteEpargne(proprio,solde_compte,taux_intêré)
            
            if type_compte == 3:
                frais_retrait = int(input("Merci de d'indiquer les frais de retrait: "))
                compte = ComptePayant(proprio,solde_compte,frais_retrait)

            comptes.append(compte)
            print("Compte crée avec succes")

            with open("compte.txt","a") as f:
                f.write(f"{proprio};{solde_compte}\n")

        
        if choix == 2:
            print("Liste des Compte")
            for index, compte in enumerate(comptes):
                print(f"{index} ➜ {compte}")
            
            afficher_compte_num= input("Voulez vous afficher Un compte spécifique O/N: ")
            if afficher_compte_num.lower() == "o":
                numero_compte = int(input("merci d'indiquez le numéro de compte: "))
                if numero_compte>= len(comptes) or numero_compte < 0:
                    print("❌ Numéro de compte invalide.")
                    continue
                compte = comptes[numero_compte]
                print(compte)
            
            else:
                continue
        
        if choix == 3:
            indice= int(input("Merci de renseigner nnuuméro de compte"))
            if indice >= len(comptes) or indice < 0:
                print("❌ Numéro de compte invalide.")
                continue
            compte = comptes[indice]
            montant_a_déposer = float(input("Merci de renseigner le montant à déposer: "))

            compte.deposer(montant_a_déposer)

            print("Dépot effectué avec succes")
        
        if choix == 4:
            indice= int(input("Merci de renseigner nnuuméro de compte"))
            if indice >= len(comptes) or indice < 0:
                print("❌ Numéro de compte invalide.")
                continue
            compte = comptes[indice]

            montant_a_retirer = float(input("Merci de renseigner le montant à retirer: "))
            
            compte.retirer(montant_a_retirer)

            print("Retrait effectué avec succes")

        if choix == 5:

            indice = int(input("Entrez le numéro de compte: "))
            if indice >= len(comptes) or indice < 0:
                print("❌ Numéro de compte invalide.")
                continue
        
            compte = comptes[indice]
            if isinstance(compte,CompteEpargne):
                compte.appliquer_interet()
            else:
                print(" Ce compte n'est pas un compte épargne")
        
        if choix == 6:
            print("Bye Bye!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break   
        
        
                    

    except(ValueError):
        print("Veuillez entrer un numero correcte")    
        continue
