import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        
        hashing = {}
        for i, j in enumerate(strs):
            hashing[i] = j
        return json.dumps(hashing)

    def decode(self, s: str) -> List[str]:

        hashing = json.loads(s)

        lst = []

        for j in hashing:
            lst.append(hashing[j])
        return lst
