import sys

n, m = map(int, sys.stdin.readline().split())

def generate_combinations_4(n, k):
    results = []
    combination = []
    def backtrack(start):
        if len(combination) == k:
            results.append(combination[:])
            return 

        for i in range(start, n+1):
            combination.append(i)
            backtrack(i)
            combination.pop()


    backtrack(1)
    return results

final_result = generate_combinations_4(n, m)

for line in final_result:
    print(*line)