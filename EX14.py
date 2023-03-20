heights = list(map(int, input().split()))
answer = max(heights) - min(heights)
print(answer)