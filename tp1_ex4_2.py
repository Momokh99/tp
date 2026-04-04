poids=int(input("le poids en Kg\t"))
taille=float(input("la taille en m\t"))
imc=poids/(taille**2)
print("L'IMC est\t",imc)
if imc <18.5:
    print("sous-poids")   
elif imc <25:
    print("poids normal")
elif imc <29.9:
    print("surpoids")
else:
    print("obésité")