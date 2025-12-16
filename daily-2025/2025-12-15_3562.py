"""

You are given an integer n, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to n, and employee 1 is the CEO. You are given two 1-based integer arrays, present and future, each of length n, where:
present[i] represents the current price at which the ith employee can buy a stock today.
future[i] represents the expected price at which the ith employee can sell the stock tomorrow.
The company's hierarchy is represented by a 2D integer array hierarchy, where hierarchy[i] = [ui, vi] means that employee ui is the direct boss of employee vi.
Additionally, you have an integer budget representing the total funds available for investment.
However, the company has a discount policy: if an employee's direct boss purchases their own stock, then the employee can buy their stock at half the original price (floor(present[v] / 2)).
Return the maximum profit that can be achieved without exceeding the given budget.
Note:
You may buy each stock at most once.
You cannot use any profit earned from future stock prices to fund additional investments and must buy only from budget.

[Solution description]
def dfs(u, p) = res0, res1, where:
res0[b] : max profit for budget b with no discount
res1[b] : max profit for budget b with this node discounted
Consider all direct children v of u. We have to aggregate all v.res0 and v.res1 together, since either we purchase stock u and all these v's are discounted, or we don't and they aren't.
The aggregation is done using C := merge(A, B). A[b1] and B[b2] represent possible choices to spend budgets b1 and b2 and C[b1+b2] = max(A[b1] + B[b2], ...) is the best choice.
Afterwards, we have to account for purchasing at node u, which adds cost to the budget. There are two cases, full cost and half cost, depending on if we got the discount from the parent.
"""
fmax = lambda x, y: x if x > y else y
def merge(A, B):
    C = [-inf] * len(A)
    for i, a in enumerate(A):
        for j in range(len(A) - i):
            C[i + j] = fmax(C[i + j], a + B[j])
    return C

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            u -= 1
            v -= 1
            adj[u].append(v)

        def dfs(u, p):
            # res0[b] : max profit for budget b with no discount
            # res1[b] : max profit for budget b with this node discounted
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            for v in adj[u]:
                if v != p:
                    res0, res1 = dfs(v, u)
                    dp0, dp1 = merge(dp0, res0), merge(dp1, res1)

            ans0 = dp0[:]
            ans1 = dp0[:]

            cost = present[u]
            for b in range(cost, budget + 1):
                ans0[b] = fmax(ans0[b], dp1[b - cost] + future[u] - cost)

            cost >>= 1
            for b in range(cost, budget + 1):
                ans1[b] = fmax(ans1[b], dp1[b - cost] + future[u] - cost)

            return ans0, ans1

        return max(dfs(0, -1)[0])