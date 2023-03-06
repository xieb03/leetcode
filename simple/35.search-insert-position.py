# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/search-insert-position/

from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result_index = 0
        length = len(nums)
        # 在数组范围内找到最后一个小于 target 的数
        while result_index < length and nums[result_index] < target:
            result_index += 1
        # 1. 如果第一次就退出，说明第一个元素相等或者大于 target，那么返回 result_index，此时就是 0
        # 2. 如果因为因为遍历结束才退出，那么返回 result_index，此时就是 length，即插在最后
        # 3. 如果是中间退出，说明 result_index 小，但是 result_index + 1 大于或者等于，那么返回 result_index + 1
        return result_index


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 事先已经有序，想到用二分法，从 O(n) 变为 O(lgn)
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = nums[0]
        if first >= target:
            return 0
        length = len(nums)
        last = nums[length - 1]
        if last == target:
            return length - 1
        if last < target:
            return length
        # 如果到这里，说明必然在中间，就是说第 1 个数小于 target，最后一个数大于 target
        left = 0
        right = length - 1
        while True:
            middle = (left + right) // 2
            # left 一定小，所以返回 left + 1
            if left == middle:
                return left + 1
            # right 一定大，所以返回 right
            if right == middle:
                return right
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle
                continue
            if nums[middle] < target:
                left = middle
                continue


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 事先已经有序，想到用二分法，从 O(n) 变为 O(lgn)
    # 二分法的难点在于 left, right, middle 怎么赋值，划分区间的时候 left, right 和 middle 的关系怎么样，退出循环的时候要如何处理
    # 在 Solution_2 的基础上精简代码
    # 二分查找只有一个思想，那就是：逐步缩小搜索区间。使用 left 和 right 向中间靠拢的方法，有一个非常强的语义，
    # 所有的关于「二分查找」法的题解，要明确「下一轮搜索区间是什么」，设置左边界 left 和 右边界 right，即结果会在 [left, right] 内，都是闭区间
    # 而最终一定是 当 left 与 right 重合的时候，我们就找到了问题的答案，使用这种写法有一个巨大的好处，那就是返回值不需要考虑返回 left 还是 right，因为退出循环以后，它们是重合的。
    # 在做题的过程中，会遇到两个难点：
    #   取 mid 的时候，有些时候需要 +1，这是因为需要避免死循环；
    #   只把区间分成两个部分，这是因为：只有这样，退出循环的时候才有 left 与 right 重合，我们才敢说，找到了问题的答案。
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        # 注意 length 可能也是解，因此为了满足闭区间，将 right 设置成 length
        right = length
        # 寻找第一个大于或者等于的元素，返回它的 index，这样思考可以避免判断多重判断，例如
        # 最后一个元素 < target，返回 length
        # 最后一个元素 == target，返回 length - 1
        # 最后一个元素 > target，返回 length - 1
        # 可以综合为，如果最后一个元素 >= target，返回 length - 1
        # , = target 返回 length - 1，d最后一个元素
        while left < right:
            # 在 left < right 的语境下，left <= middle < right，虽然 right 可能越界，但是 middle 不会越界
            # 有时候也会用到 (left + 1 + right) // 2，使得 left < middle <= right，防止向上找的时候出现 left == middle 的死循环
            middle = (left + right) // 2
            # print(left, right, middle)
            # # 注意不能退出，因为可能有若干个相同的，如果题目明确没有相同的元素，则可以直接输出
            # if nums[middle] == target:
            #     return middle
            if nums[middle] < target:
                # 满足 left <= right，往上找的时候不会出现下一轮 left == left 的死循环
                left = middle + 1
            else:
                # 注意，这里保留 middle，因为我们要找大于等于的
                # 满足 left <= right，因为上面有 middle < right，所以往下找的时候不会出现下一轮 right == right 的死循环
                right = middle
        return left


def main():
    assert [1, 2, 3, 3].count(3) == 2
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()

        assert solution.searchInsert([1, 3, 5, 6], 5) == 2
        assert solution.searchInsert([1, 3, 5, 6], 2) == 1
        assert solution.searchInsert([1, 3, 5, 6], 7) == 4
        assert solution.searchInsert([1, 3, 5, 6, 7], 5) == 2
        assert solution.searchInsert([1, 3, 5, 6, 7], 2) == 1
        assert solution.searchInsert([1, 3, 5, 6, 7], 7) == 4
        assert solution.searchInsert([1, 3, 5, 6, 8], 7) == 4


if __name__ == '__main__':
    main()
