def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number//base
    return result

def test():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == '1F')
    print('Passed')

if __name__ == '__main__':
    test()
