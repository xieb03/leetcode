# 67. 二进制求和
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
# 提示：
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-binary/


# noinspection PyUnresolvedReferences
from utils import *


# 两个二进制字符的相加，同时返回是否进位
def get_two_sum(a: str, b: str, carry: bool) -> (str, bool):
    if a == "0" and b == "0":
        if carry:
            return "1", False
        return "0", False
    elif a == "0" or b == "0":
        if carry:
            return "0", True
        return "1", False
    else:
        if carry:
            return "1", True
        return "0", True


# 一个二进制字符的相加，同时返回是否进位
def get_one_sum(a: str, carry: bool) -> (str, bool):
    if a == "0":
        if carry:
            return "1", False
        return "0", False
    else:
        if carry:
            return "0", True
        return "1", False


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length1 = len(a)
        length2 = len(b)

        # # 强制补 0 使得长度一致，方便后面处理
        # if length1 > length2:
        #     b = "0" * (length1 - length2) + b
        #     length = length1
        # else:
        #     a = "0" * (length2 - length1) + b
        #     length = length2
        # assert len(a) == len(b)

        # 保证 a 是长字符串，b 是短字符串
        if length1 < length2:
            a, b = b, a
            min_length = length1
            max_length = length2
        else:
            min_length = length2
            max_length = length1
        diff_length = max_length - min_length
        # python 中字符串是不可变对象，不支持原位修改，因此这里用数组代替
        long_list = list(a)

        # 先处理公共部分
        carry = False
        for i in range(min_length - 1, -1, -1):
            index_a = i + diff_length
            long_list[index_a], carry = get_two_sum(a[index_a], b[i], carry)

        # 再处理剩下的部分
        # 如果没有进位，那么直接返回即可，因为前面本身就是较长字符串的一部分
        if not carry:
            return "".join(long_list)
        else:
            for i in range(diff_length - 1, -1, -1):
                long_list[i], carry = get_one_sum(a[i], carry)
                # 如果某次计算没有进位，那么直接返回即可
                if not carry:
                    return "".join(long_list)
            # 执行到这里，说明还剩下进位，那么在初始位置填 1
            return "1" + "".join(long_list)


def ans(a: str, b: str) -> str:
    return bin(int(a, base=2) + int(b, base=2))[2:]


def main():
    for clazz in (Solution,):
        solution = clazz()

        a = "11"
        b = "1"
        assert solution.addBinary(a, b) == ans(a, b)

        a = "1010"
        b = "1011"
        assert solution.addBinary(a, b) == ans(a, b)

        a = "111"
        b = "111"
        assert solution.addBinary(a, b) == ans(a, b)


if __name__ == '__main__':
    main()
