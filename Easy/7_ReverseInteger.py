def reverse(x) :
    if x < 0:
        flag_neg = True
        x = 0 - x
    else:
        flag_neg = False

    if x > (2 ** 31 - 1) or x < (-2 ** 31):
        return 0

    x = str(x)
    y = ''
    for i in range(len(x) - 1, -1, -1):
        y = y + x[i]
    y = int(y)
    if flag_neg:
        y = 0 - y
    if y > (2 ** 31 - 1) or y < (-2 ** 31):
        return 0
    return y