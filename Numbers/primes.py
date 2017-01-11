import math
import random

def find_prime(number):
    num = abs(number)
    if num < 4 : return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def find_prime_sqrt(number):
    num = abs(number)
    if num < 4 : return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def find_prime_fermat(number):
    if number <= 102:
        for x in range(2, number):
            if pow(x, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number-1)
            if pow(a, number-1, number) != 1:
                return False
        return True

def test():
    num1 = 17
    num2 = 20
    assert(find_prime(num1) == True)
    assert(find_prime(num2) == False)
    assert(find_prime_sqrt(num1) == True)
    assert(find_prime_sqrt(num2) == False)
    assert(find_prime_fermat(num1) == True)
    assert(find_prime_fermat(num2) == False)
    print('Passed')

if __name__ == '__main__':
    test()
