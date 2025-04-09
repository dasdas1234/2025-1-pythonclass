
def collatz(i):
    ncount = 0
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = 3 * i + 1
        ncount = ncount + 1
    return ncount