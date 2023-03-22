count = 1
while count <= 5:
    print(count)
    count += 1


while True:
    stuff = input("String to capitalize [type q to quit]")
    if stuff == "q":
        break
    print(stuff.capitalize())