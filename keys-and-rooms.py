class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)
        que = deque()
        que.append(0)

        while que:
            room = que.popleft()
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    que.append(key)
        
        return n == len(visited)