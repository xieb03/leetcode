# 66. 加一
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 提示：
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/plus-one/


# noinspection PyUnresolvedReferences
from utils import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# 递归
class Solution_1:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 递归退出机制，如果已知到最前面还要进位，则新增最高位 1 即可
        if len(digits) == 0:
            return [1]

        # 如果最后一位小于8，则不需要处理，直接加 1 返回即可
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        # 如果最后一位是 9，则需要进位，相当于前面的数重新考虑，调用递归即可
        return self.plusOne(digits[:-1]) + [0]


# noinspection PyPep8Naming,PyMethodMayBeStatic
# 非递归
class Solution_2:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 如果最后一位小于8，则不需要处理，直接加 1 返回即可
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        # 如果没有 return，说明最后一位是9，必然产生进位
        digits[-1] = 0
        index = len(digits) - 2
        while index >= 0:
            digit = digits[index]
            if digit <= 8:
                # 如果某一位是8，直接加 1 返回即可
                digits[index] += 1
                return digits
            else:
                digits[index] = 0
                index -= 1
        # while 执行完毕，说明全部都是 9，那么直接增加高位 1 返回即可
        return [1] + digits


# noinspection PyPep8Naming,PyMethodMayBeStatic
# 非递归
class Solution:
    # 当我们对数组 digits 加一时，我们只需要关注 digits 的末尾出现了多少个 99 即可。我们可以考虑如下的三种情况：
    # 如果 digits 的末尾没有 99，例如 [1, 2, 3]，那么我们直接将末尾的数加一，得到 [1, 2, 4] 并返回；
    # 如果 digits 的末尾有若干个 99，例如 [1, 2, 3, 9, 9]，那么我们只需要找出从末尾开始的第一个不为 99 的元素，即 33，
    #       将该元素加一，得到 [1, 2, 4, 9, 9]。随后将末尾的 99 全部置零，得到 [1, 2, 4, 0, 0] 并返回。
    # 如果 digits 的所有元素都是 99，例如 [9, 9, 9, 9, 9]，那么答案为 [1, 0, 0, 0, 0, 0]。
    #       我们只需要构造一个长度比 digits 多 1 的新数组，将首元素置为 1，其余元素置为 0 即可。
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index >= 0:
            digit = digits[index]
            # 如果某一位是8，注意一定是第一次遇到，直接加 1 返回即可
            if digit <= 8:
                digits[index] += 1
                return digits
            # 如果某一位是9，置 0 同时继续向前找
            # 如果能执行到这里，说明一直是9
            else:
                digits[index] = 0
                index -= 1
        # while 执行完毕，说明全部都是 9，那么直接增加高位 1 返回即可
        return [1] + digits


# 迭代法直接"硬算"
def ans(digits: List[int]) -> List[int]:
    return list(map(int, str(int("".join(map(str, digits))) + 1)))


def main():
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()

        digits = [0]
        assert solution.plusOne(digits.copy()) == ans(digits)

        digits = [1, 2, 3]
        assert solution.plusOne(digits.copy()) == ans(digits)

        digits = [4, 3, 2, 1]
        assert solution.plusOne(digits.copy()) == ans(digits)

        digits = [4, 3, 9, 9]
        assert solution.plusOne(digits.copy()) == ans(digits)

        digits = [9, 9]
        assert solution.plusOne(digits.copy()) == ans(digits)


if __name__ == '__main__':
    main()
