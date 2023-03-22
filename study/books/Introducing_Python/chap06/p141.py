word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

word = 'thud'

for letter in word:
    if letter == 'x':
        print("Eek! an 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")