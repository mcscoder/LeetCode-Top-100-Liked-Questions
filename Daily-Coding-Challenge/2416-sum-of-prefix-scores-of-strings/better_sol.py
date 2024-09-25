# Modified from time limit exceeded solution


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

    def calculateScores(self, prefix: str) -> int:
        currNode = self.root
        count = 0

        for ch in prefix:
            if ch not in currNode:
                return count

            count += currNode[ch].count

            currNode = currNode[ch].next

        return count


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = []
        for word in words:
            ans.append(trie.calculateScores(word))

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumPrefixScores(["abc", "ab", "bc", "b"]))
