class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        currNode = self.trie

        for ch in word:
            if ch not in currNode:
                currNode[ch] = {}

            currNode = currNode[ch]

        currNode["#"] = True  # Use a special marker to indicate the end of a word.

    def search(self, word: str) -> bool:
        currNode = self.trie

        for ch in word:
            if ch not in currNode:
                return False

            currNode = currNode[ch]

        return "#" in currNode  # Check for the end-of-word marker.

    def startsWith(self, prefix: str) -> bool:
        currNode = self.trie

        for ch in prefix:
            if ch not in currNode:
                return False

            currNode = currNode[ch]
        return True


if __name__ == "__main__":
    sol = Trie()
    sol.insert("apple")
    print(sol.search("apple"))
    print(sol.startsWith("app"))
    print(sol.search("A"))
    print(sol.startsWith("aP"))
