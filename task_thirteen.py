word = input('Enter a word: ')

count = 0
for num in word:
    if(num == 'e'):
        count = count + 1
    
print(count)
