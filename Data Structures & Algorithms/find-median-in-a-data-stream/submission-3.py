class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if not self.left_heap or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)
        
        if len(self.left_heap) > len(self.right_heap) + 1:
            num = -heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, num)
        elif len(self.right_heap) > len(self.left_heap) + 1:
            num = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -num)

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        elif len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        else:
            left = -self.left_heap[0]
            right = self.right_heap[0]
            return (left + right)/2
        