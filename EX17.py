n, s = map(int, input().split())
apple_prices = list(map(int, input().split()))
pine_prices = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(n):
        if apple_prices[i] + pine_prices[j] == s:
            count += 1

print(count)