#leetcode_144 二叉树的前序遍历

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        new, visited = 0, 1
        res = []
        stack = [(new, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == new:
                stack.append((new, node.right))
                stack.append((new, node.left))
                stack.append((visited, node))
            else:
                res.append(node.val)
        return res
