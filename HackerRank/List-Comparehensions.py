# Problem link - https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
value_1 = int(input())
value_2 = int(input())
value_3 = int(input())
num = int(input())
ansList = []
for i in range(value_1):
    for j in range(value_2 + 1):
        for k in range(value_3 + 1):
            if(i + j + k != num):
                ansList.append([i, j, k])
print(ansList)