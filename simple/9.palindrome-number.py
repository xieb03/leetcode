# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 例如，121 是回文，而 123 不是。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/palindrome-number

# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        # 取出每一位数，注意是逆序的
        # 也可以推广为 n 进制数的每一位
        number_list = list()
        while x != 0:
            # x 是商，b 是余数
            x, b = divmod(x, 10)
            number_list.append(b)
        length_1 = len(number_list) - 1
        for i in range((length_1 + 1) // 2):
            if number_list[i] != number_list[length_1 - i]:
                return False
        return True


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedeclaration
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        # 反转整数
        y = 0
        copy_x = x
        while x != 0:
            # x 是商，b 是余数
            x, b = divmod(x, 10)
            y = y * 10 + b
        return copy_x == y


# noinspection PyPep8Naming,PyMethodMayBeStatic,PyRedeclaration
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        # 反转整数，但只要反转一半即可
        y = 0
        while x > y:
            # x 是商，b 是余数
            x, b = divmod(x, 10)
            y = y * 10 + b
        return x == y or x == y // 10


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(-1) == False
    assert solution.isPalindrome(0) == True
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(123) == False
    assert solution.isPalindrome(1001) == True
    assert solution.isPalindrome(1023) == False
    assert solution.isPalindrome(10201) == True
    assert solution.isPalindrome(10202) == False
    assert solution.isPalindrome(1023201) == True
    assert solution.isPalindrome(1023202) == False
    assert solution.isPalindrome(10) == False
