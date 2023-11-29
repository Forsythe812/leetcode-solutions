# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root :
            return []
            
        paths = []
        self.dfs(root, "", paths)
        return paths

    def dfs(self, node, path, paths):
        if not node.left and not node.right:
            paths.append(path + str(node.val))
            return
        
        if node.left:
            self.dfs(node.left, path + str(node.val) + "->", paths)
        
        if node.right:
            self.dfs(node.right, path + str(node.val) + "->", paths)