class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = [ord(char) for char in s]
        tt = [ord(char) for char in t]
         
        ss.sort()
        tt.sort()
        if ss == tt:
            return True
        else:
            return False
        