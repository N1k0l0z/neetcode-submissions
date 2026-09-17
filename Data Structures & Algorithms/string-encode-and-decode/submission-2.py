class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if strs == []:
            return "<empty>"
        return "<sep>".join(strs)

    def decode(self, s: str) -> List[str]:

        if s == "<empty>":
            return []

        return s.split("<sep>")
