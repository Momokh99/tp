a=int(input("enter a number\t"))
b=int(input("entrer le second number\t"))
c=int(input("entrer le troisieme number\t"))
print("a=",a)
print("b=",b)
print("c=",c)
if a>b and a>c:
    print("le plus grand nombre est\t",a)
elif b>a and b>c:
    print("le plus grand nombre est\t",b)
else:    
    print("le plus grand nombre est\t",c)