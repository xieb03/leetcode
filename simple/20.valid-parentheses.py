# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-parentheses


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 新旧括号是否匹配
    letter_dict = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        # 如果不是偶数个字符，一定不匹配
        if len(s) % 2 != 0:
            return False
        letter_list = [s[0]]
        for letter in s[1:]:
            # 注意要加上是否为空的判断，因为中间有可能被清空
            if letter_list and self.letter_dict.get(letter, None) == letter_list[-1]:
                letter_list.pop()
            else:
                letter_list.append(letter)
        return len(letter_list) == 0


def main():
    for clazz in (Solution,):
        solution = clazz()
        assert solution.isValid("()")
        assert solution.isValid("()[]{}")
        assert not solution.isValid("(]")


if __name__ == '__main__':
    main()
