import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        dic = defaultdict(int)

        for string in words:
            dic[string] -= 1

        length = 0
        for key,  val in dic.items():
            heapq.heappush(heap, (val, key))
            length += 1
        
        output = []

        for _ in range(k):
            val, key = heapq.heappop(heap)
            output.append(key)
        
       
    
        return output