import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # next time have patience

        length = len(heights)
        heap = []

        for i in range(length - 1):
            jump = heights[i + 1] - heights[i]

            if jump <= 0:
                continue
            
            else:
                heapq.heappush(heap, jump)
                
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                    if bricks < 0:
                        return i

                
        
        return length - 1




           
            

           
           
        
        return count