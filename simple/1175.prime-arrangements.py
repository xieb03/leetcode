# 1175. 质数排列
# 请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。
#
# 让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。
#
# 由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/prime-arrangements/
import math


# 计算 n 的阶乘，如果已经事先知道 m 的阶乘，可以只计算 m + 1 ~ n 的阶乘，减少计算
def factorial(n: int, m=1, default=1) -> int:
    if n == 0:
        return 1
    result = 1
    end_value = 1
    if n > m:
        result = default
        end_value = m
    while n != end_value:
        result *= n
        n -= 1
    return result


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
    # 1 ~ 5 有 2 个质数，所以 A22 * A33 = 12
    # 因此主要找有 m 个质数，返回为 Amm * A(n - m)(n - m)
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        for i in range(n + 1):
            if is_prime(i):
                prime_count += 1
        partial_factorial = factorial(prime_count)
        return (partial_factorial * factorial(n - prime_count, prime_count, partial_factorial)) % (10 ** 9 + 7)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    # 1 ~ 5 有 2 个质数，所以 A22 * A33 = 12
    # 因此主要找有 m 个质数，返回为 Amm * A(n - m)(n - m)
    # 欧式筛，线性筛，可以参见 204.count-primes.py
    # 在埃氏筛基础上的改进，例如 60，在埃氏筛中会被重复多次筛，欧拉筛要求每个合数只需要被其最小的质因子筛掉，即 60 只会被 2 筛掉一次
    # 6 = 2 * 2 * 3 = 2 * 6 = 3 * 4，即 6 只会被 2 * 6 筛，而不会被 3 * 4 筛
    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        if n >= 2:
            # 注意，第一个无效，这样保证了索引和实际值一致
            is_prime_list = [True] * (n + 1)
            is_prime_list[0] = False
            is_prime_list[1] = False
            prime_list = list()
            for i in range(2, n // 2 + 1):
                if is_prime_list[i]:
                    prime_list.append(i)
                for prime in prime_list:
                    if i * prime > n:
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
        partial_factorial = factorial(prime_count)
        return (partial_factorial * factorial(n - prime_count, prime_count, partial_factorial)) % (10 ** 9 + 7)


def main():
    factorial_24 = factorial(24)
    assert factorial_24 % (10 ** 9 + 7) == 657629300
    factorial_25 = factorial(25)
    assert factorial_25 % (10 ** 9 + 7) == 440732388
    factorial_25 = factorial(25, 24, factorial_24)
    assert factorial_25 % (10 ** 9 + 7) == 440732388

    for clazz in (Solution, Solution_1):
        solution = clazz()
        assert solution.numPrimeArrangements(5) == 12
        assert solution.numPrimeArrangements(100) == 682289015


if __name__ == '__main__':
    main()
