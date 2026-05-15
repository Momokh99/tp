Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
print("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk")
answer1 = int(input('Enter your answer (1-2): '))
if answer1 == 1:
  Gryffindor=Gryffindor+1
  Ravenclaw=Ravenclaw+1
elif answer1 ==2:
  Hufflepuff=Hufflepuff+1
  iSlytherin=Slytherin+1
else:
  print("Wrong input.")
print("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold")
answer2 = int(input('Enter your answer (1-4): '))
if answer2 == 1:
  Hufflepuff=Hufflepuff+2
elif answer2 ==2:
  Slytherin=Slytherin+2
elif answer2 == 3:
  Ravenclaw=Ravenclaw+2
elif answer2 == 4:
  Gryffindor=Gryffindor+2
else:
  print("Wrong input.")
print("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum")
answer3 = int(input('Enter your answer (1-4): '))
if answer3 == 1:
  Slytherin=Slytherin+4
elif answer3 ==2:
  Hufflepuff=Hufflepuff+4
elif answer3 == 3:
  Ravenclaw=Ravenclaw+4
elif answer3 == 4:
  Gryffindor=Gryffindor+4
else:
  print("Wrong input.")
max_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if max_points == Gryffindor:
  print("You are in Gryffindor!")
elif max_points == Ravenclaw:
  print("You are in Ravenclaw!")
elif max_points == Hufflepuff:
  print("You are in Hufflepuff!")
elif max_points == Slytherin:
  print("You are in Slytherin!")