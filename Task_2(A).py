#!/bin/python3


if __name__ == '__main__':
    elem = int(input())
    ans = []
    for i in range(elem):
        counter = 0
        sum = 0
        array = list(map(str, list(input())))
        for j in array:
            if counter == 0:
                prev = sum
            if j == '<':
                counter += 1
            else:
                counter -= 1
                if counter < 0:
                    break
                else:
                    sum += 2

        if counter != 0:
            sum = prev
        ans.insert(i, sum)
    for i in ans:
        print(i)


