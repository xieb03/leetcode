from typing import List


# 利用位运算判断是不是奇偶数，转化为二进制，最后一位是 1，则为奇数，否则是偶数
def isodd(x):
    return x & 1


# 快速幂

def fast_power(a: int, n: int):
    # value 1       1       a^2     a^2     a^10
    # a     a       a^2     a^4     a^8     a^16
    # n     1010    101     10      1       0
    # 二进制  0        1     2       3       4
    # a 始终按照二进制位数自乘，即保留该二进制最高位对应的数对应的幂次方
    # value 始终保存之前的结果，即从左到右，如果二进制新增了一位 1，那么需要将历史 value * 当前新增的最高位对应的值，即 a，如果新增了一位 0，那么 value 不变
    value = 1
    while n:
        if isodd(n):
            value *= a
        a *= a
        n = n // 2
    return value


# 二阶矩阵乘法 (2 * 2) * (2, 2) = (2, 2)
# [[1, 1], [1, 0]] * [[1, 1], [1, 0]] = [[2, 1], [1, 1]]
def matrix_2d_product_matrix_2d(matrix_1: List[List[int]], matrix_2: List[List[int]]) -> List[List[int]]:
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result


# 二阶矩阵 乘 一阶向量 (2 * 2) * (2, 1) = (2, 1)
# [[1, 1], [1, 0]] * [3, 2] = [5, 3]
def matrix_2d_product_vector_1d(matrix: List[List[int]], vector: List[int]) -> List[int]:
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += matrix[i][j] * vector[j]
    return result


# 二阶矩阵快速幂
def matrix_2d_fast_power(matrix: List[List[int]], n: int):
    value = [[1, 0], [0, 1]]
    while n:
        n, remainder = divmod(n, 2)
        if remainder == 1:
            value = matrix_2d_product_matrix_2d(value, matrix)
        matrix = matrix_2d_product_matrix_2d(matrix, matrix)
    return value


def main():
    assert isodd(37)
    assert not isodd(46)

    assert fast_power(3, 8) == 3 ** 8
    assert fast_power(4, 6) == 4 ** 6

    a_matrix = [[1, 1], [1, 0]]
    a_matrix_2 = [[2, 1], [1, 1]]
    a_matrix_3 = [[3, 2], [2, 1]]
    assert matrix_2d_product_matrix_2d(a_matrix, a_matrix) == a_matrix_2
    assert matrix_2d_product_matrix_2d(a_matrix_2, a_matrix) == a_matrix_3
    assert matrix_2d_product_vector_1d([[1, 1], [1, 0]], [3, 2]) == [5, 3]
    assert matrix_2d_fast_power(a_matrix, 0) == [[1, 0], [0, 1]]
    assert matrix_2d_fast_power(a_matrix, 1) == a_matrix
    assert matrix_2d_fast_power(a_matrix, 2) == a_matrix_2
    assert matrix_2d_fast_power(a_matrix, 3) == a_matrix_3


if __name__ == '__main__':
    main()
