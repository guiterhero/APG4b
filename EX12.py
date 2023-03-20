s = input()

count = 1
length = len(s)

for i in range(length):
    if s[i] == "+":
        count += 1
    elif s[i] == "-":
        count -= 1
    else:
        pass

print(count)
