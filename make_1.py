X = int(input())
array = [0] * 30001
array[1] = 0

if(X>1):
    for i in range(2,X+1):
        array[i] = array[i - 1] + 1
        if i % 5 == 0:
            array[i] = min(array[i],array[i//5] + 1)
        elif i % 3 == 0:
            array[i] = min(array[i],array[i//3] + 1)
        elif i % 2 == 0:
            array[i] = min(array[i],array[i//2] + 1)

print(array[X])
