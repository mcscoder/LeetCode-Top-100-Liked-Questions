class TrieNode:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count
        self.next: dict[str, TrieNode] = {}


class Trie:
    def __init__(self) -> None:
        self.root: dict[str, TrieNode] = {}

    def insert(self, word: str) -> None:
        currNode = self.root

        for ch in word:
            if ch not in currNode:
                currNode[ch] = TrieNode(ch, 0)

            currNode[ch].count += 1
            currNode = currNode[ch].next

    def startsWith(self, prefix: str) -> int:
        currNode = self.root

        for i in range(len(prefix) - 1):
            if prefix[i] not in currNode:
                return 0

            currNode = currNode[prefix[i]].next

        if prefix[-1] not in currNode:
            return 0

        return currNode[prefix[-1]].count


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = []
        for word in words:
            count = 0
            for i in range(1, len(word) + 1):
                subStr = word[:i]
                prefixCount = trie.startsWith(subStr)
                count += prefixCount

            ans.append(count)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumPrefixScores(["abc", "ab", "bc", "b"]))
