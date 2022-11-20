tweet_limit = 280
tweet_string = "blah" * 50
print(tweet_string)

# diff를 ()로 안감싸면 diff가 bool이 되버린다. 책 오류
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

print("diff : ", diff)

secret = 2
guess = 5

if guess < secret:
    print("too low")
elif secret < guess:
    print("too high")
else:
    print("just right")

small = True
green = False

if small and green:
    print("완두콩")
elif small and not green:
    print("체리")
elif not small and green:
    print("수박")
else:
    print("호박")