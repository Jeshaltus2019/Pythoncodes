

print("Penrose Bake Shop")
print("-" * 30)

menu = {'Brownie': 2.5,
        'Croissant': 3,
        'Choco Cookie': 2.75}

for food, price in menu.items():
    print(f'{food:15} USD {price}')

bill = 0
while True:
    order = input("Kindly place your Order:\n").title()

    if order in menu.keys():

        for m, price in menu.items():
            if m == order:
                bill += price

    else:
        print(f'Sorry, Wrong Order!! We do not sell {order}')

    quantity = int(input(f'How Many {order}s do you wish to Order?\n'))

print('-' * 30)
print(f'The Total Bill Amount is $ {bill * quantity}')
