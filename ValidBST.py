class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Solution(object):
    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True  
        val = n.val
        if((val>low and val<high) and self._isValidBSTHelper(n.left, low, val) and self._isValidBSTHelper(n.right,val, high)):
            return True     
        return False

    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))


#example
#     5
#    /  \
#   4    7
#       /
#      6
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(6)


print(Solution().isValidBST(node))
#True