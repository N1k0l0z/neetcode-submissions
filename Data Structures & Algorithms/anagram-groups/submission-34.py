class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        fingerpring = {}

        for s in strs:
            sorted_str = "".join(sorted(s))

            if sorted_str in fingerpring:
                fingerpring[sorted_str].append(s)
            else:
                fingerpring[sorted_str] = [s]

        return list(fingerpring.values())