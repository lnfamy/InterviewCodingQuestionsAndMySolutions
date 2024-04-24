"""
https://leetcode.com/problems/design-in-memory-file-system/description/
"""
import collections
from typing import List

"""
define another class: fileNode
"""
class FileNode:
    def __init__(self):
        self.is_file = False
        self.contents = ''
        self.children = collections.defaultdict(FileNode)

class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> List[str]:
        # iterate over the given path using / as delimiter
        cur = self.root
        for pa in path.split('/'):
            # if not p == if string is empty
            if not pa:
                continue
            cur = cur.children[pa]
        if cur.is_file:
            return [pa]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        # same as ls, iterate over path using / as delimiter
        # then when we reach a directory that doesn't exist, make it
        cur = self.root
        for pa in path.split('/'):
            if not pa:
                continue
            cur = cur.children[pa]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        for pa in filePath.split('/'):
            if not pa:
                continue
            cur = cur.children[pa]
        cur.is_file = True
        cur.contents += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        for pa in filePath.split('/'):
            if not pa:
                continue
            cur = cur.children[pa]
        return cur.contents


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)