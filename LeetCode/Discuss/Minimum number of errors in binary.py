# unfinished because i dont like this approach and i lost mine. cba to write it again

def minimum_errors(error_st: str, x: int, y: int) -> int:
    zero_before = 0
    one_before = 0

    mp = {}

    for i in range(len(error_st)):
        if error_st[i] == "0":
            zero_before += 1
        elif error_st[i] == "1":
            one_before += 1

        mp[i] = (zero_before, one_before)

    zero_after = 0
    one_after = 0

    errors = 0

    for i in range(len(error_st) - 1, -1, -1):
        if error_st[i] == "1":
            one_after += 1

            # counting 10 errors
            errors += zero_after * y
        elif error_st[i] == "0":
            zero_after += 1

            # counting 01 errors
            errors += one_after * x
        else:
            # choose 0, count 10 and 01 errors:
            one_before = mp[i][1]


    return (x + y) % (10 ** 9 + 7)
