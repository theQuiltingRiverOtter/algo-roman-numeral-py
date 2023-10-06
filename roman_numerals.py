def to_roman_lazy(num):
    output = ""
    ROMAN_NUMERAL_TO_ARABIC_MAP = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    for numeral, number in ROMAN_NUMERAL_TO_ARABIC_MAP.items():
        if num >= number:
            value = num // number
            output += numeral * value
            num -= value * number
    return output


def to_roman(num):
    output = ""
    ROMAN_NUMERAL_TO_ARABIC_MAP = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    for numeral, number in ROMAN_NUMERAL_TO_ARABIC_MAP.items():
        if num >= number:
            value = num // number
            output += numeral * value
            num -= value * number
    return output


print(to_roman(4))
print(to_roman(9))
print(to_roman(14))
print(to_roman(44))
print(to_roman(944))
