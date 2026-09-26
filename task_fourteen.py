word = input('Enter a word: ')
letter = ''
for num in word:
    if(num.islower()):
        num = num.upper()
        letter = num
    
        print(letter)
