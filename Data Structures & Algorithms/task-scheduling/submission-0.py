class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)
        for freq in count.values():
            heapq.heappush(heap, -freq)
        queue = deque()
        time = 0
        while heap or queue:
            if queue and queue[0][1] == time:
                freq, avail_time = queue.popleft()
                heapq.heappush(heap, freq)
            if heap:
                freq = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    queue.append((freq, time+n+1))
            time += 1
        return time