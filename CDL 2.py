vacations = {'Maldives':[2017,'Chilli Chicken']}
print(f'{"vacation":10} {"Year":4} {"Food":10}')
print('-'*30)

for vacation,info in vacations.items():
    print(f'{vacation:10} {info[0]:4} {info[1]:10}')