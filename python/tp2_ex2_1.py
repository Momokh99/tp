anne=int(input("Enter l'année\t"))
if (anne%4==0 and anne%100!=0) or (anne%400==0):
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")