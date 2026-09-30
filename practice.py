import math
def longe(arr):
    n = 1
    arr1 = []
    p = math.prod(arr)
    for i in range(len(arr)):
        pro = p // arr[i]
        arr1.append(pro)
    return arr1
n = int(input())
arr = list(map(int,input().split()))
print(longe(arr))