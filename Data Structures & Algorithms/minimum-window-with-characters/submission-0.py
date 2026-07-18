from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # If t is longer than s, it's impossible
        if len(t) > len(s):
            return ""

        # Frequency map of characters we need
        need = Counter(t)

        # Frequency map of current window
        window = {}

        # Number of characters whose required frequency is satisfied
        have = 0

        # Total unique characters that must be satisfied
        needCount = len(need)

        # Result indices
        res = [-1, -1]

        # Length of smallest window found
        resLen = float("inf")

        # Left pointer
        l = 0

        # Expand the window
        for r in range(len(s)):

            c = s[r]

            # Add current character into window
            window[c] = 1 + window.get(c, 0)

            # Check if this character now satisfies its required frequency
            if c in need and window[c] == need[c]:
                have += 1

            # Window is valid
            while have == needCount:

                # Update answer if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove left character
                window[s[l]] -= 1

                # If requirement breaks, decrease have
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                # Shrink window
                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("inf") else ""