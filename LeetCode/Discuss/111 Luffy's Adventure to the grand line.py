"""
One day, Luffy is on an adventure and comes across a stone bridge that takes him to the grand line.
The stone bridge has each stone labeled with a random string of characters S.
Luffy has to cross the bridge by jumping only onto special characters. Else if he jumps on any other character, he falls
into the ocean.
Now make sure he steps on all stones labeled with special characters on the way. Obviously, he has to take multiple
consecutive jumps throughout this path. He is interested in finding out the maximum length of a single jump he has to
take to cross the stone bridge. Each character on the bridge is at a distance of 1. Formally, consider that luffy is
initially located directly at the start of the bridge. His goal is to reach the end of the bridge. In every jump, luffy
jumps anywhere on the next stone with a special character on the bridge.
If luffy can't cross the bridge, return -1.

NOTE: All characters apart from A..Z, a...z are treated as special characters.
"""
class sol1:
    def sol():
        s = input()
        n = len(s)
        j = -1
        r = 0
        for i in range(n):
            if s[i].isalpha():
                continue
            else:
                r = max(r, i - j)
                j = i
        if r == 0:
            print(-1)
        else:
            r = max(r, n - j)
            print(r)

    if __name__ == "__main__":
        sol()

class sol2:
    def luffy_adv(self,s):
        init = -1
        for i in range(len(self)):
            if not self[i].isalpha():
                init = i
                break

        if init == -1:
            return -1

        ans = init + 1
        for i in range(init, len(self)):
            if not self[i].isalpha():
                ans = max(ans, i - init)
                init = i
        return ans

    if __name__ == '__main__':
        s = input()
        ans = luffy_adv(s)
        print(ans)

