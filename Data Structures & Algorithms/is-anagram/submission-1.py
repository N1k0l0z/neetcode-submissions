class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_amounts = {}
        for i in s:
            if i in s_amounts:
                s_amounts[i] +=1
            else:
                s_amounts[i] = 1
        
        t_amounts = {}
        for i in t:
            if i in t_amounts:
                t_amounts[i] +=1
            else:
                t_amounts[i] = 1
        if s_amounts == t_amounts:
            return True
        else:
            return False
        

        