#!/bin/python3


if __name__ == '__main__':
    arr = []
    len = int(input())
    queries = int(input())
    for i in range(len):
        arr.append(i+1)
    for i in range(queries):
        counter = 0
        sum = 0
        qArr = list(map(int, input().split(" ")))
        for j in range(qArr[0], qArr[1]+1):
            arr[j-1] += qArr[2]

    print(max(arr))


