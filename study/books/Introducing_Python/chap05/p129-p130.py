thing = 'woodchuck'
print('%s' % thing)
#최소 12글자까지 채워서 표시
print('%12s' % thing)
print(repr('%+12s' % thing))
print('%-12s' % thing)
print('%.3s' % thing)
print(repr('%12.3s' % thing))
print(repr('%-12.3s' % thing))

thing = 98.6
print(repr('%f' % thing))
print(repr('%12f' % thing))
print(repr('%+12f' % thing))
print(repr('%-12f' % thing))
print(repr('%.3f' % thing))
print(repr('%12.3f' % thing))
print(repr('%-12.3f' % thing))

thing = 9876
print(repr('%d' % thing))
print(repr('%12d' % thing))
#+강제출력
print(repr('%+12d' % thing))
print(repr('%-12d' % thing))
# 정수는 .3이 의미없다.
print(repr('%.3d' % thing))
print(repr('%12.3d' % thing))
print(repr('%-12.3d' % thing))