class Solution:
    def kClosest(self, points: List[List[int]], k: int) ->List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            dist = x*x + y*y
            heapq.heappush(heap, (-dist,point))
        while len(heap) > k:
            heapq.heappop(heap)
        return [point for dist, point in heap]