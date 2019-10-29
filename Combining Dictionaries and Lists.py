player = {'Messi': [31,'Argentina','FC Barcelona']}
print(f'{"Player":10} {"Age":3} {"Country":10}  {"Club":10}')
print('-'*50)

for name,info in player.items():
  print(f'{name:10} {info[0]:10} {info[1]:10} {info[2]:10}')



