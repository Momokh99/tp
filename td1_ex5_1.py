a = float(input("Enter a\t"))
b = float(input("Enter b\t"))
c = float(input("Enter c\t"))
delta = b**2 - 4*a*c
if delta < 0:
    print("L'équation n'a pas de solution réelle")
elif delta == 0:
    x = -b / (2*a)
    print("L'équation a une solution réelle double: x =", x)
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("L'équation a deux solutions réelles: x1 =", x1, "et x2 =", x2)
