letter = 'o'
list = "abcdo"

if letter in list:
    print("ok")

list = ['a', 'b', 'c', 'o']

if letter in list:
    print("ok1")

set = {'a', 'b', 'c', 'o'}

if letter in set:
    print("ok2")

_tuple = ('a', 'b', 'c', 'o')

if letter in _tuple:
    print("ok3")

if letter in "abco":
    print("ok4")

dict = {'a': "ab", 'b': "bb", 'o':"oo"}

if letter in dict:
    print("ok5")