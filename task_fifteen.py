word = input('Enter a word: ')
letter = ''
for num in word:
    if(num.isupper()):
        num = num.lower()
        letter = num
    
        print(letter)
