N = int(input())
soldier = list(map(int,input().split()))

array = [1] * N
for i in range(1,N):
    for j in range(0,i):
        if soldier[i] < soldier[j]:
            array[i] = max(array[i],array[j] + 1)
print(N - array[N-1])
