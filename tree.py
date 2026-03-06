class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1,
    TreeNode(2,
        TreeNode(4), TreeNode(5)),
    TreeNode(3,
        TreeNode(6)))



def dfs(node):
    if not node:
        return

    print(node.val)
    dfs(node.left)
    dfs(node.right)

dfs(root)
