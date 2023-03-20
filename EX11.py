n = int(input())
a = int(input())

for i in range(n):
    op, b = input().split()
    b = int(b)
    if op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    else:
        try:
            a /= b
            a = int(a)
        except ZeroDivisionError:
            print("error")
            break
    print(f"{i + 1}:{a}")
