import math

carres = [i**2 for i in range(1,21)]
print(carres)


paires = [x for x in range(51) if x%2==0]
print(paires)


mots=["Python","est","un","language","puissant"]
longeurs=[len(m) for m in mots]
print(longeurs) 