sales = [3,1,2,1]
import math

if 3 <= sales[0] <= math.pow(10,5):
    for i in range(len(sales)):
        if isinstance(sales[i], int):
            front = 0
            back = 0
            for fIterator in range(i + 1):
                front = sales[fIterator]

            for bIterator in range(i):
                back = sales[len(sales) - i]

            if front == back:
                print(i)
                break







