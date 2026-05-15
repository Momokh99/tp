phrase = input("ecrir une phrase\t")
print("Nombre de caracteres :", len(phrase))
print("En majiscule :", phrase.upper())
print("En miniscule :", phrase.lower())
print("le 5 premier caracteres :", phrase[:5])
print("Phrase intersèe:", phrase[::-1])
voy = "aeiouyAEIOUY"
nb_voy = 0
for char in phrase:
    if char in voy:
        nb_voy += 1
print("Nombre de voyelles :", nb_voy)