# Minhaj Alok
# 114868408
# malok
#
# IAE 101 (Fall 2024)
# HW 1, Problem 1

def population(year):
    if (year<2000) : return -1
    return 3*(year%100 - 10) + 310


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    test1 = population(2001)
    print("population(2001) is", test1)
    print()
    test2 = population(2010)
    print("population(2010) is", test2)
    print()
    test3 = population(2016)
    print("population(2016) is", test3)
    print()

