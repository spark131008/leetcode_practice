class Solution:
    def numTrees(self, n: int) -> int:
        # 0 node - 1 root option 1
        # 1 node - 1 root option - 1
        # 2 nodes - 2 root options - left(0) * right(1) + left(1) * right(0)
        # 3 dnoes - 3 root options
        # - left(0) * right(2)
        # - left(1) * right(1)
        # - left(2) * right(0)

        trees = [1] * (n + 1)
        for nodes in range(2, n + 1):
            totalTrees = 0
            for root in range(1, nodes + 1):
                left = trees[root - 1]
                right = trees[nodes - root]
                totalTrees += left * right
            trees[nodes] = totalTrees
        return trees[n]