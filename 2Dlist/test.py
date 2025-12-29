arr = [['']*15 for _ in range(15)]

for i in range(5):
    word = input()
    for j in range(len(word)):
        arr[i][j] = word[j]

for j in range(15):
    for i in range(5):
        if arr[i][j]!='':
            print(arr[i][j], end='')