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

# 