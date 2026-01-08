import sys

n, m = map(int, sys.stdin.readline().split())
word_freq = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word)>=m:
        word_freq[word]+=1
        
print(word_freq)