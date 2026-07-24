class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)

        left = 0
        right = x

        while left <= right:

            i = (left + right) // 2
            j = (x + y + 1) // 2 - i

            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == x else nums1[i]

            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == y else nums2[j]

            if left1 <= right2 and left2 <= right1:

                if (x + y) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2

                return max(left1, left2)

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1  