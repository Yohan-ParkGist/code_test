n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
# print(arr)
minumum_change = 64 
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if arr[k][l]=="W":
                        count+=1
                else:
                    if arr[k][l]=="B":
                        count+=1
        count = min(count, 64-count)
        minumum_change = min(minumum_change, count)
        
print(minumum_change)