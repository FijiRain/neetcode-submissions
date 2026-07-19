class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        exclude = []

        for i in strs:
            if i in exclude:
                continue
            sublist = []
            for j in strs:
                if self.isAnagram(i, j):
                    sublist.append(j)
                    exclude.append(j)
            res.append(list(sublist))
        return res