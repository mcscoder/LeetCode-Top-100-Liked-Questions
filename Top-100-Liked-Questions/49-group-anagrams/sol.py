class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmapuh: dict[str, list[str]] = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in hashmapuh:
                hashmapuh[sortedS] = []

            hashmapuh[sortedS].append(s)

        return list(hashmapuh.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
