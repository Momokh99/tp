nom = input("Votre nom: ")
age = int(input("Vorte age : "))
ville = input("Votre ville : ")
print("=" *50)
print("Bonjour ",nom)
print("Vous aver ",age, " ans et habiter à ",ville)
print("Dans 10 ans ,vous aurez ",age + 10, "ans.")
print("=" *50)
print("  \n")
print("  \n")
print("  \n")



prix = float(input("Prix HT   :   "))
taux = float(input("Taux TVA (%) :  "))
taux=(prix/100)*taux
print("-" *10,"FACTURE","-"*10)
print("Prix HT       :      ",prix,"DH")
print("TVA  (20,0%)  :      ",taux,"DH")
ttc= taux + prix
print("Prix TTC      :      ",ttc,"DH")
