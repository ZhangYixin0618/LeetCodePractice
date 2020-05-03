def romanToInt(s):
    sum = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'A': 4, 'B': 9, 'E': 40, 'F': 90,
                  'G': 400, 'H': 900}
    s = s.replace("IV", "A").replace("IX", "B").replace("XL", "E").replace("XC", "F").replace("CD", "G").replace("CM",
                                                                                                                 "H")
    for item in s:
        sum += roman_dict[item]
    return sum
print(romanToInt('IV'))
