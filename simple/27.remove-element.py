# 27. 移除元素
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-element/

from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        current_index = 0

        # 如果一直没有非法元素，那么就等于自己对自己赋值一遍
        # for value in nums:
        #     if value != val:
        #         nums[current_index] = value
        #         current_index += 1

        for i in range(len(nums)):
            if nums[i] != val:
                # 增加一次判断，避免重复赋值
                if i > current_index:
                    nums[current_index] = nums[i]
                current_index += 1
        return current_index


# 如果要移除的元素恰好在数组的开头，例如序列 [1,2,3,4,5]，当 val 为 1 时，我们需要把每一个元素都左移一位。
# 注意到题目中说：「元素的顺序可以改变」。实际上我们可以直接将最后一个元素 55 移动到序列开头，取代元素 11，得到序列 [5,2,3,4]，
# 同样满足题目要求。这个优化在序列中 val 元素的数量较少时非常有效。
#
# 实现方面，我们依然使用双指针，两个指针初始时分别位于数组的首尾，向中间移动遍历该序列。
#
# 如果左指针 left 指向的元素等于 val，此时将右指针 right 指向的元素复制到左指针 left 的位置，然后右指针 right 左移一位。
# 如果赋值过来的元素恰好也等于 val，可以继续把右指针 right 指向的元素的值赋值过来（左指针 left 指向的等于 val 的元素的位置继续被覆盖），
# 直到左指针指向的元素的值不等于 val 为止。
#
# 当左指针 left 和右指针 right 重合的时候，左右指针遍历完数组中所有的元素。
#
# 这样的方法两个指针在最坏的情况下合起来只遍历了数组一次。与方法一不同的是，方法二避免了需要保留的元素的重复赋值操作。
# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1

        # 注意要用 <= ，因为最后重合时候的元素也要判断
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1

        # 注意要用 <= ，因为最后重合时候的元素也要判断
        # 在 Solution_2 的基础上优化，Solution_2 中，即使 right 是非法值，也会赋值，等待下一次优化，这里会过滤掉 right 的非法值
        while left <= right:
            if nums[left] == val:
                # 找到右边满足条件的
                while left < right and nums[right] == val:
                    right -= 1
                # 如果一直没有找到，说明后续全部都是非法元素，直接退出即可
                if right == left:
                    return left
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left


def main():
    assert [1, 2, 3, 3].count(3) == 2
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()

        a_list = []
        k = solution.removeElement(a_list, 1)
        assert a_list[:k] == []

        a_list = [1]
        k = solution.removeElement(a_list, 1)
        assert a_list[:k] == []

        a_list = [1, 1]
        k = solution.removeElement(a_list, 1)
        assert a_list[:k] == []

        a_list = [3, 2, 2, 3]
        k = solution.removeElement(a_list, 3)
        assert sorted(a_list[:k]) == sorted([2, 2])

        a_list = [0, 1, 2, 2, 3, 0, 4, 2]
        k = solution.removeElement(a_list, 2)
        assert sorted(a_list[:k]) == sorted([0, 1, 4, 0, 3])


if __name__ == '__main__':
    main()
