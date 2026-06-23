class Solution:
    def checkInclusion(self, s1: str, s2: str) -> boo

        if len(s1) > len(s2):
            return False

        h = Counter(s1)
        L = 0 
        for L in range (0, len(s2) - len(s1) + 1):
            R = L + len(s1) - 1
            sub_s = text[L:R]
            counts = Counter(sub_s)
            if (h == counts):
                return True


        return False
