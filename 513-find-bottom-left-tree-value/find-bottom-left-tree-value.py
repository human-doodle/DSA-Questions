# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return None
        
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current_node = queue.popleft()

                # For the leftmost element in each level
                if i == 0:
                    leftmost_value = current_node.val

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return leftmost_value
            