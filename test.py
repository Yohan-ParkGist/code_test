import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    card = deque(map(int, sys.stdin.readline().split()))
    
    a = 0
    b = 0
    left_temp = card.popleft()
    right_temp = card.pop()
    turn = 0
    
    for _ in range(2*n):
        if turn == 0:
            turn = 1
            if left_temp > right_temp:
                a+=left_temp
                if card:
                    left_temp = card.popleft()
            else:
                a+=right_temp
                if card:
                    right_temp = card.pop()
                
        elif turn == 1:
            turn = 1
            if left_temp > right_temp:
                b+=left_temp
                if card:
                    left_temp = card.popleft()
            else:
                b+=right_temp
                if card:
                    right_temp = card.pop()
    
    print(a)