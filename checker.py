def checker(expected, observed):
    if expected.replace(" ", "") == observed.replace(" ", ""):
        return True
    else:
        return False
    
print(checker("hello", "hello"))