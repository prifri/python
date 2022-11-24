takes = 'get gloves, a, b, c, d, e,f'
print(takes.split(','))
# 공백 문자(줄바꿈, 스페이스, 탭)기준으로 나눈다.
print(takes.split())

crypto_list = ['abc', 'def', '513']
crypto_string = ', '.join(crypto_list)
print(crypto_string)