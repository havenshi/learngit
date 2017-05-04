def rand7():
    x = 1<<31
    while x > 21:
        x = 5 * (rand5() - 1) + rand5() # random 1-25, if 22-25, change it to 1-21
        return x % 7 + 1