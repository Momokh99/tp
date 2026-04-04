a=float(input("Enter a\t"))
b=float(input("Enter b\t"))
c=float(input("Enter c\t"))
if a+b>c and a+c>b and b+c>a:
    print("triangle valide")
else:    print("triangle non valide")
if a==b and b==c:
    print("triangle équilatéral")
elif a==b or b==c or a==c:
    print("triangle isocèle")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("triangle rectangle")
else:    print("triangle scalène")