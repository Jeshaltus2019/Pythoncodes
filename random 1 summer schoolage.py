import random
five_to_seven =["Lego blocks","Painting"]
age = int(input("Enter your age:  "))
eight_to_ten =["chess","coding"]
eleven_to_fifteeen =["coding","robotics"]
if age>=5 and age<=7:
  print(random.choice(five_to_seven))
elif age>=8 and age<=10:
  print(random.choice(eight_to_ten))
elif age>=11 and age<=15:
  print(random.choice(eleven_to_fifteeen))
else:
  print("Sorry! Wrong input!")