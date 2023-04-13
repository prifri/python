work_quotes = ['a', 'b', 'c', 'd']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

marxes = ['a', 'b', 'c', 'd', 'b']
print(marxes.index('b'))
# 유무 확인
print('b' in marxes)
print('x' in marxes)

print(marxes.count('b'))
print(marxes.count('x'))

# 문자열로 변환
print(', '.join(marxes))

separator = ' * '
joined = separator.join(marxes)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
# 정렬된것을 생성
sorted_marxes = sorted(marxes)
print(id(marxes))
print(id(sorted_marxes))
print(sorted_marxes)

marxes.sort()
# list를 정렬.
print(id(marxes))
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = ['2', '1', '3.1', '3']
numbers.sort()
print(numbers)

marxes = ['a', 'b', 'c', 'd']
print(len(marxes))
# 비추.
print(marxes.__len__())

# int *str = "abc"; 
# int *p = str;
# 와 동일한 개념.
a = [1, 2, 3]
print(a)
b = a
print(b)
b[1] = 4
print(a)
# id가 같음을 알수있다.
print(id(a)," ",id(b))

# 얕은 복사
# int str[4] = "abc"; 
# int str2[4];
# memcpy(str2, str, sizeof(str));
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
print(id(a), " ", id(b), " ", id(c), " ", id(d))
a[0] = "aaa"
print(a, " ", b, " ", c, " ", d)

# 깊은 복사
# 전용 copy가 있어야된다. 파이썬에선 자동으로 copy를 지원하는 타입들은 해주는것 같음.
# 깊은 복사 필요 경우 예시.
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(id(a), " ", id(b), " ", id(c), " ", id(d))
a[2][0] = "aaa"
print(a, " ", b, " ", c, " ", d)

import copy

a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(id(a), " ", id(b))
a[2][0] = "aaa"
print(a, " ", b)
