"""
https://leetcode.com/problems/design-a-text-editor/description/
"""
"""
idea: use string as our data structure (better performance than array) and use python text splicing
"""


class TextEditor:

    def __init__(self):
        self.str = "|"

    def addText(self, text: str) -> None:
        add_index = self.str.index('|')
        # splice text so you add the new text right in the position of the cursor
        # then add text using +, then add the rest of the remaining string using splicing again
        self.str = self.str[:add_index] + text + "|" + self.str[add_index + 1:]

    def deleteText(self, k: int) -> int:
        # make a copy of self.str to keep the og length
        temp = len(self.str)
        del_index = self.str.index('|')
        # check that we have enough room to delete stuff
        if len(self.str[:del_index]) >= k:
            # make our string to be everything until the elements we want to delete + the cursor sign |
            self.str = self.str[:del_index - k] + self.str[del_index:]
        else:
            # if we don't have enough characters, we just clip from the deletion index to the end (cursor mark)
            self.str = self.str[del_index:]

        # return number of characters deleted
        return temp - len(self.str)

    def cursorLeft(self, k: int) -> str:
        move_index = self.str.index('|')
        if move_index < k:
            self.str = self.str.replace("|", "")
            self.str = "|" + self.str
        else:
            self.str = self.str.replace("|", "")
            self.str = self.str[:move_index - k] + "|" + self.str[move_index - k:]

        new_index = self.str.index('|')
        if self.str.index("|") > 10:
            return self.str[new_index - 10: new_index]
        return self.str[:new_index]

    def cursorRight(self, k: int) -> str:
        move_index = self.str.index('|')
        if len(self.str) - move_index < k:
            self.str = self.str.replace("|", "")
            self.str = self.str + "|"
        else:
            self.str = self.str.replace("|", "")
            self.str = self.str[:move_index + k] + "|" + self.str[move_index + k:]

        new_index = self.str.index('|')
        if self.str.index('|') > 10:
            return self.str[new_index - 10: new_index]
        return self.str[:new_index]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
