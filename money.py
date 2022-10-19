N,M = map(int,input().split())
money = []
for _ in range(N):
    money.append(int(input()))
array = [10001] * (M + 1)
array[0] = 0
for i in range(N):
    for j in range(array[i],M+1):
        if array[j - array[i]] != 10001:
            array[j] = min(array[j-array[i]]+1,array[j])

if array[M] == 10001:
    print(-1)
else:
    print(array[M])
