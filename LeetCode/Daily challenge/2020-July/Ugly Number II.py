from typing import List
class Solution:
    
        
    # Method 1    
    # This method combine 3 calculation into a loop. factors is the list of aimed factors given by the question.
    # k is the length of the factor list
    # starts is the start position to loop corresponding to each factor.
    def nthUglyNumber(self, n: int) -> int:
        factors, k = [2, 3, 5], 3
        starts, res = [0] * k, [1]
        # 这里能在n次解决的原因是，每次循环是对3个值都进行了检测
        # for i in range(n-1):
        while len(res) < n:
            numbers = [factors[i] * res[starts[i]] for i in range(k)]
            newNumber = min(numbers)
            res.append(newNumber)
            starts = [starts[i] + (numbers[i] == newNumber) for i in range(k)]
        return res[-1]

    # Method 2 
    # 
    def isUgly(self, n):
        factors = [2, 3 , 5]
        for i in factors:
            while n % i == 0:
                n /= i
        return (n==1)

    def nthUglyNumber2(self, n: int) -> int:
        res = 0
        while n>0:
            res += 1
            if self.isUgly(res):
                n -= 1
        return res

    # Method 3
    # The mechanism is the same as the first method. This way is much easier understanding. 
    def nthUglyNumber3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        t2 = t3 = t5 = 0
        ugly = [0]*n
        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = min(ugly[t2]*2, ugly[t3]*3, ugly[t5]*5)
            if ugly[i] == ugly[t2]*2: t2 += 1
            if ugly[i] == ugly[t3]*3: t3 += 1
            if ugly[i] == ugly[t5]*5: t5 += 1
        
        return ugly[n-1]

s1 = Solution()
res = s1.nthUglyNumber2(10)
print (res)

# reference
# https://leetcode.com/problems/ugly-number-ii/discuss/718879/Python-O(n)-universal-dp-solution-explained