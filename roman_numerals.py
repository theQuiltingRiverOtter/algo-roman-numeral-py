def to_roman(num):
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
    for numeral, number in ROMAN_NUMERAL_TO_ARABIC_MAP.entries():
        print(numeral, number)
