import math
notes = []
notes_refus=[]
notes_admis = []
for i in range(10):
    x = int(input(f'entrer la {i} note :'))
    notes.append(x)
print(f'les note est {notes}')
for note in notes:
    if note < 10:notes_refus.append(note)
    else:notes_admis.append(note)
print(f'''

les note des etudiant reusit est {notes_admis} avec un moyenne de reussit egal à {sum(notes_admis)/len(notes_admis)}
les etudiant qui ont echoie est {notes_refus} avec un moyenne egal à {sum(notes_refus)/len(notes_refus)}
le taux de ressit est {(len(notes_admis)/len(notes))*100}%
la moyenne general est {sum(notes)/len(notes)}
''')
