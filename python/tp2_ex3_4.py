import random

n=random.randint(0, 100)
x=int(input("Enter a number\t"))
if n<x:
    print("Le nombre est plus petit que n")
elif n>x:
    print("Le nombre est plus grand que n")
else:
    print("Le nombre est égal à n")