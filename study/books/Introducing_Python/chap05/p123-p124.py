poem = '''All that doth flow we cannot liquid name
or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
#All로 시작하는지 검사
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

word = 'the'
#처음으로 찾은 offset return.
print(poem.find(word))
print(poem.index(word))

#reverse
print(poem.rfind(word))
print(poem.rindex(word))

#못찾을경우 find는 -1, index는 예외
print(poem.find("kkr"))
#print(poem.index("kkr"))

print(poem.count(word))
#모든 문자가 알파벳과 문자인지.
print(poem.isalnum())