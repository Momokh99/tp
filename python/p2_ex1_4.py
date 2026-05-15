note=float(input("Entrer la note\t"))
if note < 0 or note > 20:
    print("note pas valide")
elif note < 10:
    print("non admis")
elif note <= 10:
    print("Passable")
elif note <= 12:
    print("Assez bien")
elif note <= 14:
    print("Bien")
elif note <= 16:
    print("Très bien")