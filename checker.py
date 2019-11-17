def checker(expected, observed):
    if expected.replace(" ", "") == observed.replace(" ", ""):
        return True
    else:
        return False
    
def amountCorrect(expected, observed):
    correctpart = ""
    i = 0
    j = 0
    while i < len(expected):
        try:
            if expected[i] == " ":
                i += 1
            elif observed[j] == " ":
                j += 1
                correctpart += " "
            elif expected[i] == observed[j]:
                correctpart += observed[j]
                i += 1
                j += 1
            else:
                break
        except:
            break

    incorrectpart = observed[len(correctpart):]

    return correctpart, incorrectpart

