# Minhaj Alok
# 114868408
# malok
#
# IAE 101 (Fall 2024)
# HW 1, Problem 2

def tip_amount(bill, good_service):
    if bill <= 30:
        return 8.0
    else:
        if good_service:
            return bill * 0.29
        else:
            return bill * 0.16


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("tip_amount(23.37,True) is", tip_amount(23.37, True))
    print()
    print("tip_amount(23.37,False) is", tip_amount(23.37, False))
    print()
    print("tip_amount(81.75,True) is", tip_amount(81.75, True))
    print()
    print("tip_amount(63.59,True) is", tip_amount(63.59, True))
    print()
    print("tip_amount(63.59,False) is", tip_amount(63.59, False))
    print()
