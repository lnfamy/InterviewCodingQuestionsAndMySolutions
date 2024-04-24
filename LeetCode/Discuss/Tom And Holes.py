"""
As you know Tom always wants to catch Jerry. This time he is planning to dig M holes on a straight track. Digging one
hole will take one unit of time. Since Tom is a lazy cat, he asks N fellow cats for help. Tom assigns each N cats some
consecutive holes to dig. Two cats will not dig the same hole. Tom is very keen in catching Jerry, so he wants to assign
holes to each cat optimally such that total time required to dig holes is minimum. But since Tom is weak in mathematics,
can you help him find minimum amount of time required to dig all holes if he assigns holes to cats optimally.

INPUT:
First line contains T: number of test cases
For each test case:
    First line denotes to integers N M: Ie. number of cats and number of holes
    Next line contains M space separated integers denoting depth of each hole.

OUTPUT:
For each test case, output on a new line, minimum amount of time required to dig all holes.

"""
# SOL 1 USES BISECT, SOL 2 IMPLEMENTS BINARY SEARCH INSTEAD OF RELYING ON BISECT
class sol2:
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low  # Return the insertion point

    def min_time_to_dig_holes(t, test_cases):
        for _ in range(t):
            n, m = test_cases[_][0], test_cases[_][1]
            arr = test_cases[_][2]

            s = max(arr)
            e = n * max(arr)

            for i in range(1, n):
                arr[i] += arr[i - 1]

            while e > s:
                mid = s + (e - s) // 2
                total_time = 0
                fff = False

                for i in range(n):
                    index = binary_search(arr, total_time + mid)
                    if index == m:
                        fff = True
                        break
                    if index == 0:
                        break
                    total_time -= arr[index - 1]
                    if total_time == 0:
                        break
                    total_time = arr[index]

                if fff:
                    e = mid
                else:
                    s = mid + 1

            print(e)

    # Example usage
    t = 2
    test_cases = [
        (2, 5, [2, 5, 4, 6, 8]),
        (3, 4, [4, 7, 6, 3])
    ]

    min_time_to_dig_holes(t, test_cases)


class sol1:
    def min_time_to_dig_holes(t, test_cases):
        for _ in range(t):
            n, m = test_cases[_][0], test_cases[_][1]
            arr = test_cases[_][2]

            s = max(arr)
            e = n * max(arr)

            for i in range(1, n):
                arr[i] += arr[i - 1]

            while e > s:
                mid = s + (e - s) // 2
                total_time = 0
                fff = False

                for i in range(n):
                    index = bisect.bisect_left(arr, total_time + mid)
                    if index == m:
                        fff = True
                        break
                    if index == 0:
                        break
                    total_time -= arr[index - 1]
                    if total_time == 0:
                        break
                    total_time = arr[index]

                if fff:
                    e = mid
                else:
                    s = mid + 1

            print(e)


if __name__ == '__main__':
    # Example usage
    import bisect

    t = 2
    test_cases = [
        (2, 5, [2, 5, 4, 6, 8]),
        (3, 4, [4, 7, 6, 3])
    ]

    min_time_to_dig_holes(t, test_cases)
