# 204. 计数质数
# 给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/count-primes/
import math


# 判断一个数是否是质数
def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_1:
    # 最慢，判断每一个是否是质数
    def countPrimes(self, n: int) -> int:
        prime_count = 0
        for i in range(n):
            if is_prime(i):
                prime_count += 1
        return prime_count


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_2:
    # 优化：利用已经找到的质数来判断
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime_count = 0
        prime_list = list()
        for i in range(2, n):
            sqrt_i = int(math.sqrt(n - 1)) + 1
            is_prime_ = True
            # 主要找已经找到的质数验算即可
            for prime in prime_list:
                if i % prime == 0:
                    is_prime_ = False
                    break
                if prime > sqrt_i:
                    break
            # 如果都没有，则说明该数本身是质数
            if is_prime_:
                prime_count += 1
                prime_list.append(i)
        return prime_count


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution_3:
    # 埃氏筛
    # 这是一个古老的筛素数的方法。方法如下：
    # 初始化长度 O(n) 的标记数组，表示这个数组是否为质数。数组初始化所有的数都是质数.
    # 从 2 开始（已经被标记过合数的不需要在考虑）将当前数字的倍数全都标记为合数。标记到 sqrt(n)
    # 注意每次找当前素数 x 的倍数时，是从 x^2 开始的。因为如果 x > 2，那么 2 * x 肯定被素数 2 给过滤了，最小未被过滤的肯定是 x^2
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # 注意，第一个无效，这样保证了索引和实际值一致
        is_prime_list = [True] * n
        is_prime_list[0] = False
        is_prime_list[1] = False
        for i in range(2, int(math.sqrt(n - 1)) + 1):
            # 如果已经被标记为合数，那么不再需要验证它的倍数，因为一定被它的因子筛选过
            if is_prime_list[i]:
                for j in range(i * i, n, i):
                    is_prime_list[j] = False
        prime_count = 0
        for value in is_prime_list:
            if value:
                prime_count += 1
        return prime_count


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 欧式筛，线性筛
    # 在埃氏筛基础上的改进，例如 60，在埃氏筛中会被重复多次筛，欧拉筛要求每个合数只需要被其最小的质因子筛掉，即 60 只会被 2 筛掉一次
    # 6 = 2 * 2 * 3 = 2 * 6 = 3 * 4，即 6 只会被 2 * 6 筛，而不会被 3 * 4 筛
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # 注意，第一个无效，这样保证了索引和实际值一致
        is_prime_list = [True] * n
        is_prime_list[0] = False
        is_prime_list[1] = False
        prime_list = list()
        for i in range(2, n // 2 + 1):
            if is_prime_list[i]:
                prime_list.append(i)
            for prime in prime_list:
                if i * prime >= n:
                    break
                is_prime_list[i * prime] = False
                # 这里的 break 保证了只会被筛一次，例如 i == 4, prime == 2，就会 break，而不会进行下一次 i == 4, prime == 3
                # 因为 12 要被最小质因子 prime == 2，即等待 i = 6 的时候筛掉，而不是提前被 prime == 3 筛掉
                if i % prime == 0:
                    break
        prime_count = 0
        for value in is_prime_list:
            if value:
                prime_count += 1
        return prime_count


def main():
    for clazz in (Solution, Solution_1, Solution_2, Solution_3):
        solution = clazz()
        assert solution.countPrimes(0) == 0
        assert solution.countPrimes(1) == 0
        assert solution.countPrimes(2) == 0
        assert solution.countPrimes(5) == 2
        assert solution.countPrimes(10) == 4
        assert solution.countPrimes(100) == 25


if __name__ == '__main__':
    main()
