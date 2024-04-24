
class readInput:
    def read(self):
        """
        READING INPUT GIVEN IN A SINGLE LINE, ARGUMENTS SEPARATED BY SPACES:
        """
        # for reading ints
        N, M = map(int, input().split())

        # for reading strings
        S1, S2 = input().split()

        # for reading floats
        F1, F2 = map(float, input().split())

        # getting two arrays. one array per line, each element in array separated by spaces:
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        # getting two integers, separated by lines
        num1 = int(input())
        num2 = int(input())