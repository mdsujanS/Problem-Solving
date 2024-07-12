# problem link - https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # A Maximum Binary bit of a Number is 1-19 bit. store 1 - 19 between prime Number 
        primeNumber = [2, 3, 5, 7, 11, 13, 17, 19]
        countPrime = 0

        for n in range(left, right+1):
            #bin() for convert number in binary and coutn 1 in bit
            countBit = bin(n).count("1")  

            if countBit in primeNumber:
                countPrime += 1
        return countPrime

if __name__ == '__main__':
    left = int(input())
    right = int(input())
    obj = Solution()
    print(obj.countPrimeSetBits(left, right))