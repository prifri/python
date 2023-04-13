a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)
a = [3, 2]
b = [1, 2, 3]
print(a > b)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)

for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)

for cheese in cheeses:
    if cheese.startswith('x'):
        print('This shop has some lovely', cheese)
        break
else:
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'icecream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

A = 'a', 'b', 'c'
B = 1, 2, 3,

print(list(zip(A, B)))
print(dict(zip(A, B)))

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

#list comprehension
number_list = [number - 1 for number in range(1,6)]
print(number_list)

number_list = [number for number in range(1,6) if number & 1 == 1]
print(number_list)

#위와 동치.
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

#range type
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

#tuple unpacking
for row, col in cells:
    print(row, col)

small_birds = ['small 1', 'small 2']
extinct_birds = ['eb 1', 'eb 2', 'eb 3']
carol_birds = ['c 1', 'c 2', 'c 3']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])

# tuple은 comprehension이 없다.
# [] -> ()로 변경하면 tuple comprehension이 되는게 아니라 제네레이터 객체를 반환한다고 한다.
number_thing = (number for number in range(1, 6))
print(number_thing)
print(type(number_thing))