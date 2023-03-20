numbers = list(map(int, input().split()))
for i in range(4):
    if numbers[i] == numbers[i + 1]:
        print("YES")
        break
else:
    print("NO")