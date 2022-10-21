T = int(input())
for _ in range(T):
    num = 0
    N,M = map(int,input().split())
    gold = list(map(int,input().split()))
    array = []
    index = 0
    for i in range(N):
        array.append(gold[index:index+M])
        index += M
    for j in range(1,M):
        for i in range(0,N):
            if i > 0 and i + 1 < N:
                array[i][j] = array[i][j] + max(array[i-1][j-1],array[i][j-1],array[i+1][j-1])
            elif i == 0:
                array[i][j] = array[i][j] + max(array[i][j-1],array[i+1][j-1])
            else:
                array[i][j] = array[i][j] + max(array[i-1][j-1],array[i][j-1])
    for i in range(N):
        num = max([array[i][M-1],num])
    print(num)
