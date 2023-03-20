n = int(input())
scores = list(map(int, input().split()))
average = sum(scores) / n
average = int(average)

for i in range(n):
    print(abs(scores[i] - average))