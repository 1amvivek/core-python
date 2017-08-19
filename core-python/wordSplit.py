s = "I apple"

import re

def main():
    list = re.split(' |, |; |: |\.', s)
    print(list)

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] != '' or list[i] != '.':
                if list[j] == list[i]:
                    return list[i]

print(main())





