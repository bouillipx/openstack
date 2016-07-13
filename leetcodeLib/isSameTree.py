__author__ = 'bouilli'

def isSameTree(p, q):
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p == q

