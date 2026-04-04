second = int(input("Enter the number of seconds\t"))
minute = second // 60
heure = minute // 60
minute = minute % 60
second2 = second % 60
print(f"{second} secondes = {heure}h {minute}min {second2}s")