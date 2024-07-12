
# https://www.hackerrank.com/challenges/lonely-integer/problem

def lonlyInteger(arr):
    result = 0
    for num in arr:
        # Xor Operation to find Unique
        result ^= num
    return result

if __name__=='__main__':
    n = int(input())
    List = list(map(int,input().split()))
    print(lonlyInteger(List))
