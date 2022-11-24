#strip 양옆에 대해서만 제거
world = " ear th "
print(world.strip())
print(world.lstrip())
print(world.rstrip())

print(world.strip('!'))
print(world.strip(' '))

blurt = "What .. the...!!?"
print(blurt.strip('.?!'))

import string
#repr 원시문자열로 변경
print(repr(string.whitespace))
print(repr(string.punctuation))

prospector = "What in tarnation ..####!!!@  @.???!!!"
print(prospector.strip(string.punctuation))
print(prospector.strip(string.whitespace + string.punctuation))