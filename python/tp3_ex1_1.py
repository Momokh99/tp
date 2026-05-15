import math

print("="*60)
print("\n"+ "="*60)
notes=[15,2,18,9,13,6,13]
print(f"notes:{notes}")
print(f"le premier élement est {notes[0]} \nle dernier element est {notes[-1]}")
print(f"les trois premier element sont {notes[0:3]}")
print(f"les element d'indice paire sont {notes[0::2]}")
print(f"la liste inverse est {notes[::-1]}")
print(f"le max est {max(notes)} le min est {min(notes)} la somme est {sum(notes)} la longeur est {len(notes)}")
print(f"le moyenne est {sum(notes)/len(notes)}")




