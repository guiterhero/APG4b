a, op, b = input().split()
a = int(a)
b = int(b)

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    try:
        print(int(a / b))
    except:
        print("error")
else:
    print("error")