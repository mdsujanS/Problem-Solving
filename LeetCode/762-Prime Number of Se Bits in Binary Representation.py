# problem link - https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/



class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeNumber = [2, 3, 5, 7, 11, 13, 17, 19]       # A Maximum Binary bit of a Number is 1-19 bit. store 1 - 19 between prime Number 
        countPrime = 0

        for n in range(left, right+1):
            countBit = bin(n).count("1")    #bin() for count 1 in a bianary number
            if countBit in primeNumber:
                countPrime += 1
        return countPrime

if __name__ == '__main__':
    left = int(input())
    right = int(input())
    obj = Solution()
    print(obj.countPrimeSetBits(left, right))