class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path):
            #base case 
            if len(nums) == len(path):
                result.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return result