class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        window = {}
        if len(s1) > len(s2):
            return False
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if count1 == window:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == count1:
                return True
        return False