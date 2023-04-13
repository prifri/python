marxes = ['a', 'b', 'c']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])
print(id(marxes))

marxes.append('d')
print(id(marxes))
print(marxes)

marxes = ['a', 'b', 'c']
marxes.insert(2, 'd')
print(marxes)
marxes.insert(10, 'z')
print(marxes)