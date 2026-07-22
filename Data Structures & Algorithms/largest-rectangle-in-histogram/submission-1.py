class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height*(i-index))
                start = index
            stack.append((start, h))
        while stack:
            index, height = stack.pop()
            maxarea = max(maxarea, height*(len(heights)-index))
        return maxarea