import random
p1_score = 0
c_score = 0
for counter in range(1,11):
  computer = random.randint(1,5)
  print(f'Round{counter}')
  p1 = int(input("Enter a number between 1 to 5:  "))
  if computer == p1:
      print ("Excellent! You did it!")
      p1_score += 1
  else:
      print (f'Wrong choice!The computer chose {computer}')
      c_score += 1
print (f'p1s score is {p1_score}.Computers score is {c_score}')

