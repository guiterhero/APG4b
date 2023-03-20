n = int(input())

def sum_scores():
    scores = list(map(int, input().split()))
    total_score = sum(scores)
    return total_score

a_score = sum_scores()
b_score = sum_scores()
c_score = sum_scores()

print(a_score * b_score * c_score)

