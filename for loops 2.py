number = int(input("Enter a number of your choice:   "))
for row in range(12):
  print(f'{number} - {row + 1} = {number - (row + 1)}')