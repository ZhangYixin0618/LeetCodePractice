def romanToInt(s):
    sum = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for index in range(0, len(s)):
        try:
            if s[index:(index + 2)] == "IV":
                sum = sum + 4 - 5
            elif s[index:(index + 2)] == "IX":
                sum = sum + 9 - 10
            elif s[index:(index + 2)] == "XL":
                sum = sum + 40 - 50
            elif s[index:(index + 2)] == "XC":
                sum = sum + 90 - 100
            elif s[index:(index + 2)] == "CD":
                sum = sum + 400 - 500
            elif s[index:(index + 2)] == "CM":
                sum = sum + 900 - 1000
            else:
                sum = sum + roman_dict[s[index]]
        except IndexError:
            sum = sum + roman_dict[s[index]]
    return sum