class Trie:
    def __init__(self) -> None:
        self.trie = {}

    def insert(self, word: str) -> None:
        currNode = self.trie

        for ch in word:
            if ch not in currNode:
                currNode[ch] = {}

            currNode = currNode[ch]

        currNode["#"] = True

    def startsWith(self, prefix: str) -> bool:
        currNode = self.trie

        for ch in prefix:
            if ch not in currNode:
                return False

            currNode = currNode[ch]

        return True


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = Trie()
        for num in arr2:
            st = str(num)
            trie.insert(st)

        longestPrefix = 0
        for num in arr1:
            st = str(num)

            for i in range(len(st), 0, -1):
                subSt = st[:i]
                if trie.startsWith(subSt):
                    longestPrefix = max(longestPrefix, len(subSt))
                    break

        return longestPrefix
