#leetcode_94 二叉树的中序遍历


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        new, visited = 0, 1
        res = []
        stack = [(new, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == new:
                stack.append((new, node.right))
                stack.append((visited, node))
                stack.append((new, node.left))
            else:
                res.append(node.val)
        return res