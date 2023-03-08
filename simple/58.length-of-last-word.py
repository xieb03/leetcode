# 58. 最后一个单词的长度
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
# 提示：
#
# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/length-of-last-word/


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    # 从头遍历，遇到空格则清零，但要记住清零前的长度，因为最后可能也是空格，把长度清空了
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last_length = 0
        for letter in s:
            if letter == " ":
                # 碰到连续的 0，只在第一个 0 上处理
                if length != 0:
                    last_length = length
                    length = 0
            else:
                length += 1
        if length != 0:
            return length
        return last_length


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 从头遍历，遇到空格则清零，但要记住清零前的长度，因为最后可能也是空格，把长度清空了
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        index = len(s) - 1
        # 先去除末尾可能的空格
        while index >= 0 and s[index] == " ":
            index -= 1

        # 如果 while 全部执行完，说明全都是空格，返回 0
        if index < 0:
            return 0

        # 再来数最后一个单词的长度
        while index >= 0 and s[index] != " ":
            length += 1
            index -= 1
        # 无论 while 是否执行完，表示都遍历了一个完整的单词，返回 length 即可
        return length


def main():
    assert [1, 2, 3, 3].count(3) == 2
    for clazz in (Solution,):
        solution = clazz()

        assert solution.lengthOfLastWord("Hello World") == 5
        assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
        assert solution.lengthOfLastWord("luffy is still joyboy") == 6


if __name__ == '__main__':
    main()
