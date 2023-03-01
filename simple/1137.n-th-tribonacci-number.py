# 1137. 第 N 个泰波那契数
# 泰波那契序列 Tn 定义如下：
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/n-th-tribonacci-number/


# noinspection PyPep8Naming,PyMethodMayBeStatic
# 也可以用矩阵快速幂来解，[Tn+3, Tn+2, Tn+1] = [[1, 1, 1], [1, 0, 0], [0, 1, 0]] * [Tn+2, Tn+1, Tn]
# 与 70.爬楼梯 只不过是三阶方阵，这里不再列出
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        a, b, c = 0, 1, 1
        while n != 2:
            a, b, c = b, c, a + b + c
            n -= 1
        return c


def main():
    for clazz in (Solution,):
        solution = clazz()
        assert solution.tribonacci(4) == 4
        assert solution.tribonacci(25) == 1389537


if __name__ == '__main__':
    main()
