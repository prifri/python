#format_string % data
print('%s' % 48)
print('%s' % '48')
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

print('%s%%' % 100)
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("abcde %s" % actor)
# 정수를 자동으로 string으로 변환시키는게 보인다.
print("abc %s abcd %s abc" % (cat, weight))