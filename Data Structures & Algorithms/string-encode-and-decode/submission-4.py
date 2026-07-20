class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "AAAA"
        res = "\n".join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "AAAA":
            return []
        res = s.split("\n")
        return res
