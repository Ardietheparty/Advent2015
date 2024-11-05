from hashlib import md5
input = "iwrupvqb"
for i in range(1000000000):
    test = md5((input + str(i)).encode()).hexdigest()
    if test[:5] == "00000":
        print(i)
        break
for i in range(1000000000):
    test = md5((input + str(i)).encode()).hexdigest()
    if test[:6] == "000000":
        print(i)
        break