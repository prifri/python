x = 10
if 5 < x and x < 11:
    print("done")

if 5 < x or x < 11:
    print("done1")

if 5 < x < 10 < 999:
    print("done2")

# (5 < x) && !(x < 10)
if 5 < x and not x < 10:
    print("done3")

# !(x > 10)
if not (x > 10):
    print("done4")