# 125. 验证回文串
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
#
# 字母和数字都属于字母数字字符。
#
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-palindrome/

# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    def isPalindrome(self, s: str) -> bool:
        valid_string_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        length = len(s)
        first = 0
        last = length - 1
        # 增加标识符，这样在寻找第 2 个有效字符的时候，第一个不用重新判断
        first_valid = False
        while first < last:
            if not first_valid and s[first] not in valid_string_set:
                first += 1
                continue
            first_valid = True
            if s[last] not in valid_string_set:
                last -= 1
                continue
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
            first_valid = False
        return True


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string_set = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        length = len(s)
        first = 0
        last = length - 1
        while first < last:
            # 找到下一个有效为止，注意要加上 first，否则如果都是非法字符串，可能会越界
            while first < last and s[first] not in valid_string_set:
                first += 1
            # 找到下一个有效为止
            while first < last and s[last] not in valid_string_set:
                last -= 1
            # 注意要重新判断，因为可能已经越过中间了，就不用再判断了
            if first < last:
                if s[first].lower() != s[last].lower():
                    return False
                first += 1
                last -= 1
        return True


if __name__ == '__main__':
    for clazz in (Solution,):
        solution = clazz()
        assert solution.isPalindrome("A man, a plan, a canal: Panama")
        assert not solution.isPalindrome("race a car")
        assert solution.isPalindrome(" ")
        assert solution.isPalindrome(".,")
