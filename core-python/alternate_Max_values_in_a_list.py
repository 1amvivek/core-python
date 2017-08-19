from random import randint
maxList = []

def main():
    list = []
    for i in range(10):
        list.append(randint(1, 200))

    print(list)
    getMaxList(list)
    print("output: %s" % maxList)


def getMaxList(list):
    length = len(list)
    maxList.append(max(list))
    maxIndex = list.index(max(list))
    list[maxIndex] = 0
    if maxIndex != length-1:
        list[maxIndex+1] = 0
    if maxIndex !=0:
        list[maxIndex-1] = 0
    if max(list) == 0:
        return
    else:
        return getMaxList(list)

if __name__ == '__main__':
    main()