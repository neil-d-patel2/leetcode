# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = [[root.val]]

        q = collections.deque()
        q.append(root)
        while q:
            l = []
            while q:
                node = q.popleft()
                if node.left != None:
                    l.append(node.left.val)
                if node.right != None:
                    l.append(node.right.val)
            if l:
                out.append(l)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return out
