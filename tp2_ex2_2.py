a=int(input("Enter the first number\t"))
b=int(input("Enter the second number\t"))
operateur=input("Enter the operator\t")
if operateur=="+":
    print("la somme de a et b est\t",a+b)
elif operateur=="-":
    print("la différence de a et b est\t",a-b)
elif operateur=="*":
    print("le produit de a et b est\t",a*b)
elif operateur=="/":
    if b!=0:
        print("le quotient de a et b est\t",a/b)
    else:
        print("division par zero n'est pas permise")
else:
    print("operateur non valide")