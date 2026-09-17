class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "#"

        string = ""

        for i in strs:
            string += f"{len(i)}#"
            string += i
        return string
        
    def decode(self, s: str) -> List[str]:

        if s.startswith("#"):
            return []
        lst = []

        while True:
            first_sep = s.find("#")
            
            jump = int(s[0: first_sep]) 
            
            lst.append(s[first_sep + 1 :first_sep + 1 + jump]) #"3#ghy4#hdko"
            
            s = s[first_sep + jump + 1:]
            if s == "":
                break
        return lst
            



        
