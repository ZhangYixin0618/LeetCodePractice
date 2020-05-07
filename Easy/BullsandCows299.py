def getHint(secret: str, guess: str):
    secret_num_count = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0,
                        "8": 0, "9": 0}
    bull = 0
    cow = 0
    secret = list(secret)
    guess = list(guess)
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            secret[i] = "-1"
            guess[i] = "-1"
            bull += 1
    for i in range(len(secret)):
        if secret[i] != "-1":
            secret_num_count[secret[i]] += 1
    for i in guess:
        if i != "-1":
            if secret_num_count[i] != 0:
                cow += 1
                secret_num_count[i] -= 1
    return f"{bull}A{cow}B"


print(getHint("1807", "7810"))
print(getHint("1123", "0111"))
print(getHint("1122", "1222"))
