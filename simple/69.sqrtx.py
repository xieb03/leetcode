# 69. x 的平方根
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sqrtx/


# noinspection PyUnresolvedReferences
from utils import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# 二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            # 多 + 1 防止死循环，例如 x = 8, left = 2 right = 3, 计算的 root = 2，小了，那么后面 left 还是 2，进入死循环
            root = (left + right + 1) // 2
            # if root * root > x:
            # 为了避免移除，用除法而不是乘法
            if root > x // root:
                # 可以多减 1，因为一定不能大
                right = root - 1
            else:
                # 不可以多减 1，可以等于
                left = root

        return left


def ans(x: int) -> int:
    return int(math.sqrt(x))


def main():
    for clazz in (Solution,):
        solution = clazz()

        x = 4
        assert solution.mySqrt(x) == ans(x)

        x = 8
        assert solution.mySqrt(x) == ans(x)

        x = 90
        assert solution.mySqrt(x) == ans(x)


if __name__ == '__main__':
    main()
