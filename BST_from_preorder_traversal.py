"""

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and
any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, 
then traverses node.left, then traverses node.right.)

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        head = None
        
        for elem in preorder :
            node = TreeNode(elem)
            if head == None:
                head = node
            
            else:
                temp = head
                while temp:
                    #tempp = temp
                    if temp.val < elem :
                        if temp.right :
                            temp = temp.right
                        else:
                            temp.right = node
                            break
                        
                    else:
                        if temp.left :
                            temp = temp.left
                        
                        else:
                            temp.left = node
                            break
                    
        return head
