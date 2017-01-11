def convert_from_decimal(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num%base*multiplier
        multiplier *= 10
        num = num//base
    return result

def test():
    num, base = 9, 2
    assert(convert_from_decimal(num, base) == 1001)
    print('Passed')

if __name__ == '__main__':
    test()
