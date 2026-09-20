class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 and len(s) % 2 != 0:
            return False

        hashing = {"]": "[", "}": "{", ")": "("}

        lst = []

        for idx, val in enumerate(s):
            if val in hashing.values():
                lst.append(val)
            else:
                if hashing.get(val) not in lst or hashing.get(val) != lst[-1]:
                    return False
                else:
                    lst = lst[:-1]
        
        return True if lst == [] else False




            



        