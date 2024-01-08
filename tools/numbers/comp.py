def sumofdigits(num):
    return sum(int(digit) for digit in str(num))

def ispal(num):
    return str(num) == str(num)[::-1]
