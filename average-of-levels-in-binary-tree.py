# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        
        output = []

        while q:
            avg = 0
            n = len(q)

            for i in range(n):
                node = q.popleft()
                avg += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            avg /= n
            output.append(avg)
            
        return output