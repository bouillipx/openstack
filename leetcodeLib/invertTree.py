__author__ = 'bouilli'
def invertTree(root):
    if root:
        tmp = root.right
        root.right = root.left if root.left is None else invertTree(root.left)
        root.left = tmp if tmp is None else invertTree(tmp)
    return root

