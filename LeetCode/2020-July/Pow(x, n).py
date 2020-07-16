class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)

# Using bidichotomy (二分法) to calculate the number of multiplication.
    def myPow2(sefl, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
        n = abs(n)
        squares = {0: 1, 1: x}
        
        def square(x: float, n: int) -> float:
            if n in squares:
                return squares[n]
            if n not in squares:
                squares[n] = square(x, n//2) * square(x, n//2) * square(x, n%2)
            return squares[n]
        
        return square(x, n)

    # This method is not good enough especially for n which has a big value 
    # For redundency part, like 1^n, the 2nd method can easily solve it.
    def myPow3(self, x, n):
        if n<0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            res *= x
            n -= 1
            if abs(res) < 1e-7:
                break

        return res

s1 = Solution()
print(s1.myPow3(-2, -2))
print(s1.myPow(-2, -2))
print(s1.myPow3(1, 2147483647))
# 