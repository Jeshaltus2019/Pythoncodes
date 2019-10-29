word = input("Enter a word:  ")
reverse =''
total_letters = len(word)
for counter in range(total_letters):
  reverse += word[total_letters -1]
  total_letters -= 1
print(f'{word} when reversed reads {reverse}')