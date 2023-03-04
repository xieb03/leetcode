# 26. 删除有序数组中的重复项
# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
#
# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
# 不需要 nums 中超出新长度 k 后面的元素。
#
# 将最终结果插入 nums 的前 k 个位置后返回 k 。
#
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 最近要比较的元素
        current_value = nums[0]
        # 可以插入的位置
        current_index = 1
        for value in nums[1:]:
            if value != current_value:
                nums[current_index] = value
                current_index += 1
                current_value = value
        return current_index


def main():
    for clazz in (Solution,):
        solution = clazz()

        a_list = []
        k = solution.removeDuplicates(a_list)
        assert a_list[:k] == []

        a_list = [3]
        k = solution.removeDuplicates(a_list)
        assert a_list[:k] == [3]

        a_list = [1, 1, 2]
        k = solution.removeDuplicates(a_list)
        assert a_list[:k] == [1, 2]

        a_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = solution.removeDuplicates(a_list)
        assert a_list[:k] == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    main()
