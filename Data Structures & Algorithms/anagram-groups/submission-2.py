from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):

        groups = defaultdict(list)

        for word in strs:

            # Frequency array for 26 lowercase letters
            count = [0] * 26

            # Count each character
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Convert list to tuple so it can be used as a dictionary key
            groups[tuple(count)].append(word)

        return list(groups.values())