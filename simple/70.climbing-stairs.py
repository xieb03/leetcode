# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/roman-to-integer/

from typing import List


# 二阶矩阵乘法 (2 * 2) * (2, 2) = (2, 2)
# [[1, 1], [1, 0]] * [[1, 1], [1, 0]] = [[2, 1], [1, 1]]
def matrix_2d_product_matrix_2d(matrix_1: List[List[int]], matrix_2: List[List[int]]) -> List[List[int]]:
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result


# 二阶矩阵 乘 一阶向量 (2 * 2) * (2, 1) = (2, 1)
# [[1, 1], [1, 0]] * [3, 2] = [5, 3]
def matrix_2d_product_vector_1d(matrix: List[List[int]], vector: List[int]) -> List[int]:
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += matrix[i][j] * vector[j]
    return result


# 二阶矩阵快速幂
def matrix_2d_fast_power(matrix: List[List[int]], n: int):
    value = [[1, 0], [0, 1]]
    while n:
        n, remainder = divmod(n, 2)
        if remainder == 1:
            value = matrix_2d_product_matrix_2d(value, matrix)
        matrix = matrix_2d_product_matrix_2d(matrix, matrix)
    return value


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    def climbStairs(self, n: int) -> int:
        # s(1)
        if n == 1:
            return 1
        # s(2)
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 2^(ab) = (2^a)^b
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # s(n) = s(n - 1) + s(n - 2)
        a = 1
        b = 2
        for _ in range(3, n + 1):
            b, a = a + b, b
        return b


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # s(n) = 1 * s(n - 1) + 1 * s(n - 2)
    # s(n - 1) = 1 * s(n - 1) + 0 * s(n - 2)
    # [s(n), s(n - 1)].T = [[1, 1], [1, 0]] * [s(n - 1), s(n - 2)].T
    # [s(n), s(n - 1)].T = [[1, 1], [1, 0]]^2 * [s(n - 2), s(n - 3)].T
    # ...
    # [s(n), s(n - 1)].T = [[1, 1], [1, 0]]^(n - 2)) * [s(2), s(1)].T
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a_matrix = [[1, 1], [1, 0]]
        return matrix_2d_product_vector_1d(matrix_2d_fast_power(a_matrix, n - 2), [2, 1])[0]


if __name__ == '__main__':
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()
        assert solution.climbStairs(2) == 2
        assert solution.climbStairs(3) == 3
        assert solution.climbStairs(4) == 5
