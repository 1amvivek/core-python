arr = [6,1,2,2,3,4,2,1]


from operator import itemgetter
import math


def subArrayLength(arr, number):
    max = 0
    min = 0
    flag = True
    for arrayIndex in range(len(arr)):
        if number == arr[arrayIndex]:
            if flag:
                min = arrayIndex
                flag = False
            else:
                max = arrayIndex
    return ((max - min) + 1)


def degreeOfArray(arr):
    sortedData = {}
    for arrayIndex in range(len(arr)):
        currentValue = arr[arrayIndex]
        if 2 <= currentValue <= math.pow(10, 6):
            if currentValue not in sortedData:
                sortedData[currentValue] = 1
                max = arrayIndex
            else:
                sortedData[currentValue] = sortedData[currentValue] + 1
                min =  arrayIndex
    data = sorted(sortedData.items(), key=itemgetter(1))
    return subArrayLength(arr, data[len(data) - 1][0])


print(degreeOfArray(arr))
