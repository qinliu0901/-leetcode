# -*- coding: utf-8 -*-
"""
    binary tree二叉树的先序遍历，中序，后序；分治法；深度优先搜索dfs、广度优先搜索bfs
    @author: qinliu

"""



# 144. 二叉树的先序遍历 
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
    keypoints:
    1. 把root入栈
    2. 出栈的元素放入results
    3. 先把右儿子入栈，再把左儿子入栈，这样出栈的顺序是先左后右
    4. 直到stack全部pop出为空
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        results = []
        while stack:
            node = stack.pop()
            # 弹出栈的最后一个元素
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return results
        
        
        
# 94. 二叉树的中序遍历 
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        results = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            results.append(node.val)
            node = node.right  
        return results  


# 145. 二叉树的后序遍历 
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
# 中右左倒过来即为后序
class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        results = []
        
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            
        return results[::-1]  


# 104. 二叉树的最大深度
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
# 用分治法递归，左子树右子树的最大深度+1
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


# 110. 平衡二叉树
# https://leetcode-cn.com/problems/balanced-binary-tree/
# 当最大深度函数返回不为-1时为平衡二叉树，在maxDepth中加入二叉树每个节点的左右子树的高度差绝对值不超过1。
class Solution:
    def isBalanced(self, root):
        return self.maxDepth(root) != -1
        
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1



# 124. 二叉树中的最大路径和
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# 分治法与局部最大值结合起来，在遍历树的时候，一看当前子树的最大值，二看经过根节点的最大值即子树对父树贡献了啥
class Solution:
    def maxPathSum(self, root):
        # 当前子树的最大值用全局变量
        self.maxSum = -sys.maxsize - 1
        self.helper(root)
        return self.maxSum
    
    def helper(self, root):
        if not root:
            return 0
        leftSum = self.helper(root.left)
        if leftSum < 0:
            leftSum = 0
        rightSum = self.helper(root.right)
        if rightSum < 0:
            rightSum = 0
        self.maxSum = max(self.maxSum, leftSum + root.val + rightSum)
        return max(root.val + leftSum, root.val + rightSum)




# 102. 二叉树的层次遍历，层次遍历2
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# 使用队列不断压入节点遍历，每次弹出队列的第一个元素，遍历它的左右子节点加入队列中，直到当前层遍历结束
from collections import deque
# deque 双端队列double-ended queue, 是一种具有队列和栈的数据结构，元素可从两端弹出，两端插入
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        results = []
        while queue:
            level = []
            for _ in range(len(queue)):
                # _ 表示遍历列表中元素，不需要用到i
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)
        return results
# return results[::-1]返回其节点值自底向上的层次遍历



# 98. 验证二叉搜索树
# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 根要大于左子树中的Max，小于右子树的Min。或者验证它的中序遍历为升序的
class Solution:
    def isValidBST(self, root):
    
        if root is None:
            return True
        max = sys.maxsize
        min = -sys.maxsize - 1
        return self.dfs(root,min,max)
    def dfs(self, root, min, max):
        if root is None:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.dfs(root.left, min, root.val) and self.dfs(root.right, root.val, max)



# 450. 删除二叉搜索树中的节点
# https://leetcode-cn.com/problems/delete-node-in-a-bst/
# 递归的分治法求解，检查key在左子树还是右子树还是root里，若root为key，讨论root有子节点情况，0,1,2
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        # check key in left/right subtree/root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # check root has one/two/none sons
            if root.left and root.right:
                max = self.findMax(root)
                root.val = max.val
                # delete maximum in left tree
                root.left = self.deleteNode(root.left, max.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        return root         
    # find the maximum in subtree of root
    def findMax(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node
  