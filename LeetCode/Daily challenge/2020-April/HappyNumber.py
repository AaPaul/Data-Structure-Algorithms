def isHappy(n: int):
    dict1 = {}
    # lst = []
    # We also can use (n not in list)
    while n !=1 and (n not in dict1.keys()):
        # lst.append(n)
        dict1[n] = n
        temp = 0
        while (n != 0):
            # temp += (n%10) * (n%10)
            temp += pow(n%10, 2)
            n = n // 10
        n = temp
    if n == 1:
        return True
    else:
        return False


    # stupid method
    '''
    while n != 1 and (n not in dict1.keys()):
        dict1[n] = n
        if 1000 > n >= 100:
            a = n // 100
            b = (n - a * 100) // 10
            c = n % 10
            n = a ** 2 + b ** 2 + c ** 2
        elif 100 > n >= 10:
            a = n // 10
            b = n % 10
            n = a ** 2 + b ** 2
        # elif n < 10 and n > 0:
        elif 10 > n > 0:
            # a = n % 10
            n = n ** 2
        else:
            raise Exception("error")
            # return False
    if n == 1:
        return True
    else:
        return False
    '''

def main():
    print(isHappy(1221))

# 37 is not a happy number, 19,32, 28, 100,1221 are belonging to the happy number

if __name__ == "__main__":
    main()

