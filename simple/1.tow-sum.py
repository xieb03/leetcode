# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/two-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 保存每一个元素和其所在的位置
        value_dict = dict()
        for i, u in enumerate(nums):
            # 利用 get 可以直接判断 in 和取到 j，避免了 下一步再去做一次 value_dict[] 查询
            j = value_dict.get(target - u, None)
            if j is not None:
                return [i, j]
            else:
                value_dict[u] = i
