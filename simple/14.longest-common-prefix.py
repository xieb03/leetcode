# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-common-prefix/


from typing import List


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 纵向扫描时:从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，
    # 如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for current_index, current_letter in enumerate(strs[0]):
            for str_ in strs:
                if len(str_) <= current_index or str_[current_index] != current_letter:
                    return strs[0][:current_index]
        # 如果没有进入循环，说明第一个字符串是空字符串，直接返回
        # 如果进入循环但一直没有退出，那么说明第一个字符串就是公共前缀，直接返回
        return strs[0]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    # 横向扫描：依次遍历字符串数组中的每个字符串，对于每个遍历到的字符串，更新最长公共前缀，当遍历完所有的字符串以后，
    # 即可得到字符串数组中的最长公共前缀。
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for str_ in (strs[1:]):
            length = min(len(common_prefix), len(str_))
            if length == 0:
                return ""
            for i in range(length):
                if common_prefix[i] != str_[i]:
                    common_prefix = common_prefix[:i]
                    break
        return common_prefix


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 分治
    def lcp(self, strs: List[str], start_index, end_index) -> str:
        if start_index == end_index:
            return strs[start_index]
        min_index = (start_index + end_index) // 2
        first_prefix = self.lcp(strs, start_index, min_index)
        second_prefix = self.lcp(strs, min_index + 1, end_index)
        min_length = min(len(first_prefix), len(second_prefix))
        if min_length == 0:
            return ""
        for i in range(min_length):
            if first_prefix[i] != second_prefix[i]:
                return first_prefix[:i]
        return first_prefix[:min_length]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.lcp(strs, 0, len(strs) - 1)


def main():
    for clazz in (Solution, Solution_1, Solution_2):
        solution = clazz()
        assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
        assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
        assert solution.longestCommonPrefix(["ab", "ab", "ab"]) == "ab"
        assert solution.longestCommonPrefix(["", "ab", "ab"]) == ""
        assert solution.longestCommonPrefix(["ab", "", "ab"]) == ""


if __name__ == '__main__':
    main()
