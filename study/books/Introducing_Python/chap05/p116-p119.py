letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[:1])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
# 문자 한개출력 -> 7개 건너뜀 -> 문자한개출력 반복
print(letters[::7])
# 4~20범위에서 7개씩 건너뛰면서 한개씩 출력
print(letters[4:20:3])
#19~끝의 범위에서 4개씩 건너뛰면서 한개씩 출력
print(letters[19::4])
print(letters[:21:5])
# -1 부터 끝가지 -1칸씩 움직이면서 출력
print(letters[-1::-1])
print(letters[-50:])
print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])
print(len(letters))
print(len(""))