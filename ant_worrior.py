N = int(input())
array = list(map(int,input().split()))
alist = [0] * 100
alist[0] = array[0]
alist[1] = max(array[0],array[1])

for i in range(2,N):
    alist[i] = max(alist[i-1],array[i]+alist[i-2])

print(alist[N-1])
