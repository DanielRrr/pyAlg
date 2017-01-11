from fractions import Fraction

def round_float(num1, places):
    return round(num1, places)

def float_to_frac(num):
    a = Fraction(*num.as_integer_ratio())

def get_denominator(num1, num2):
    a = Fraction(num1, num2)
    return a.denominator

def get_numerator(num1, num2):
    a = Fraction(num1, num2)
    return a.numerator

def test_floats(module_name='this module'):
    number1 = 1.25
    number2 = 1
    number3 = -1
    number4 = Fraction(5, 4)
    number6 = 6
    assert(round_float(number1, number2) == 1.2)
    assert(round_float(number1*10, number3) == 10)
    assert(get_denominator(number2, number6) == number6)
    assert(get_numerator(number2, number6) == number2)

    s = 'Tests in {name} have {cool}'
    print(s.format(name=module_name, cool='passed'))

if __name__ == '__main__':
    test_floats()
