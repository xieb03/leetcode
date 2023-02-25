# 7. 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 - 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 提示：
#
# -2^31 <= x <= 2^31 - 1
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reverse-integer/

# noinspection PyMethodMayBeStatic

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        is_positive = 1
        if x < 0:
            is_positive = -1
            x = -x
        y = 0
        while x != 0:
            x, b = divmod(x, 10)
            y = y * 10 + b

        y = y * is_positive
        if y >= 1 << 31 or y < -(1 << 31):
            return 0
        return y


if __name__ == '__main__':
    assert (1 << 32) == 2 ** 32
    assert -(1 << 32) == -2 ** 32

    for clazz in (Solution,):
        solution = clazz()
        assert solution.reverse(123) == 321
        assert solution.reverse(-123) == -321
        assert solution.reverse(120) == 21
        assert solution.reverse(0) == 0
