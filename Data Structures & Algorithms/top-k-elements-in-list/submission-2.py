class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        #Count the freq of elements
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #create the bucket and store the values a/c to freq
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            bucket[count].append(num)
        #now traverse the bucket and find most freq element
        result = [] 
        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
