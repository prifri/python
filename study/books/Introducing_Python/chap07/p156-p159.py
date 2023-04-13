print(["blah"] * 3)

marxes = ['a', 'b', 'c']
others = [1, 2, 3]
marxes.extend(others)
print(marxes)
print(others)

marxes = ['a','b', 'c']
others = [1, 2, 3]
marxes += others
print(marxes)
print(others)

marxes = ['a','b', 'c']
others = [1, 2, 3]
marxes.append(others)
print(marxes)

marxes = ['a','b', 'c']
marxes[2] = 1
print(marxes)

numbers = [1, 2, 3, 4,]
print(numbers)
numbers[1:3] = [8, 9]
print(numbers)
numbers = [1, 2, 3, 4,]
numbers[1:3] = [7, 8, 9]
print(numbers)
numbers = [1, 2, 3, 4,]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4,]
numbers[1:3] = (99, 100, 101)
print(numbers)

numbers = [1, 2, 3, 4,]
numbers[1:3] = 'wat?'
print(numbers)

marxes = ['a', 'b', 'c', 'd', 'e']
print(marxes[-1])
del marxes[-1]
print(marxes)

marxes = ['a', 'b', 'c', 'd', 'e']
del marxes[1]
print(marxes)

marxes = ['a', 'b', 'c', 'd', 'e']
marxes.remove('c')
print(marxes)

marxes = ['a', 'b', 'c', 'd', 'e']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)