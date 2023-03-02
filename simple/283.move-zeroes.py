# 283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/move-zeroes/


from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    # 可能需要两次遍历，例如全都是零
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 当前可以填充元素的位置
        current_index = 0
        # 将不等于 0 的元素不断地从前向后填充，并不会出现覆盖的场景，因为填充位置增长的慢
        for value in nums:
            if value != 0:
                nums[current_index] = value
                current_index += 1
        # 填充完毕后，剩余的位置全部置 0
        for i in range(current_index, len(nums)):
            nums[i] = 0


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 只需要一次遍历。即在交换的中就填充0，不需要最后重新填一遍
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 当前可以填充元素的位置
        current_index = 0
        # 快排的思想，找到锚点 0，然后将满足条件的移到锚点的左侧，不满足锚点的移到锚点的右侧
        for i, value in enumerate(nums):
            if value != 0:
                # 注意，因为这里强制赋 0，因此为了避免将非零元素覆盖掉，需要增加一次索引是否相同的判断
                if i != current_index:
                    nums[current_index], nums[i] = value, 0
                current_index += 1


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_3:
    # 只需要一次遍历。即在交换的中就填充0，不需要最后重新填一遍
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 当前可以填充元素的位置
        current_index = 0
        # 快排的思想，找到锚点 0，然后将满足条件的移到锚点的左侧，不满足锚点的移到锚点的右侧
        for i, value in enumerate(nums):
            if value != 0:
                # 这里直接交换，回避了 Solution_2 中索引相同的问题
                nums[current_index], nums[i] = value, nums[current_index]
                current_index += 1


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 只需要一次遍历。即在交换的中就填充0，不需要最后重新填一遍
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找到第一个 0 的位置，默认会被下面改变，不改变表示没有 0
        current_index = -1
        for i, value in enumerate(nums):
            if value == 0:
                # 当前可以填充元素的位置
                current_index = i
                break
        # 如果 current_index 没有改变，说明没有 0，不需要操作
        if current_index == -1:
            return
        # 快排的思想，找到锚点 0，然后将满足条件的移到锚点的左侧，不满足锚点的移到锚点的右侧
        for i in range(current_index + 1, len(nums)):
            # 注意不能使用 enumerate 生成器，因为后面会改变 nums 中的元素，会影响生成器
            # for i, value in enumerate(nums[current_index + 1:]):
            value = nums[i]
            if value != 0:
                # 这里可以采用 Solution_2 的方式直接赋 0，因为已经回避了中索引相同的问题，此时 i 一定 领先于 current_index
                nums[current_index], nums[i] = value, 0
                current_index += 1


def main():
    for clazz in (Solution, Solution_1, Solution_2, Solution_3):
        solution = clazz()

        a_list = [0, 1, 0, 3, 12]
        solution.moveZeroes(a_list)
        assert a_list == [1, 3, 12, 0, 0]

        a_list = [0]
        solution.moveZeroes(a_list)
        assert a_list == [0]

        a_list = [1]
        solution.moveZeroes(a_list)
        assert a_list == [1]

        a_list = [2, 1]
        solution.moveZeroes(a_list)
        assert a_list == [2, 1]


if __name__ == '__main__':
    main()
