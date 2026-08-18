class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        def backtrack(index, path):
            if index == len(nums):
                self.result.append(path[:])
                return

            #include number
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            #does not include number
            backtrack(index + 1, path)
        backtrack(0, [])
        return self.result