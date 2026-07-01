# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return -1
        out = []

        def lot(root):
            nonlocal out
            if root == None:
                return None
            
            lot(root.left)
            out.append(root.val)
            lot(root.right)

        lot(root)
        print(out) 
        return out[k-1]     


        # [1,2,3] 
