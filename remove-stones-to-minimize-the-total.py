import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        length = len(piles)

        for i in range(length):
            heapq.heappush(heap, -(piles[i]))
        
    
        for i in range(k):
            x = (heapq.heappop(heap)) * -1
            x -= x // 2
            heapq.heappush(heap, -x)
        
        return -(sum(heap))