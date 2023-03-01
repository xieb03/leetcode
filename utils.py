from typing import List


# 利用位运算判断是不是奇偶数，转化为二进制，最后一位是 1，则为奇数，否则是偶数
def isodd(x):
    return x & 1


# 获得全是默认值的 vector，注意这里的 vector 是铺平的，即 (1, a)
def get_equal_vector(a, default=0):
    result = list()
    for _ in range(a):
        result.append(default)
    return result


# 获得全 0 vector，注意这里的 vector 是铺平的，即 (1, a)
def get_zero_vector(a):
    return get_equal_vector(a, 0)


# 获得全 1 vector，注意这里的 vector 是铺平的，即 (1, a)
def get_one_vector(a):
    return get_equal_vector(a, 1)


# 获得全是默认值的 (a, b) 矩阵
def get_equal_matrix(a, b=None, default=0):
    if b is None:
        b = a
    result = list()
    for _ in range(a):
        result.append(get_equal_vector(b, default))
    return result


# 获得全 0 的 (a, b) 矩阵
def get_zero_matrix(a, b=None):
    if b is None:
        b = a
    return get_equal_matrix(a, b, 0)


# 获得全 1 的 (a, b) 矩阵
def get_one_matrix(a, b=None):
    if b is None:
        b = a
    return get_equal_matrix(a, b, 1)


# 获得 (a, b) 的单位矩阵
def get_eye_matrix(a, b=None):
    if b is None:
        b = a
    result = get_zero_matrix(a, b)
    for i in range(a):
        if i == b:
            break
        result[i][i] = 1
    return result


# 整数快速幂
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


# 通用矩阵乘法：(a, b) * (b, c) = (a, c)
def matrix_product_matrix(matrix_1: List[List[int]], matrix_2: List[List[int]]) -> List[List[int]]:
    a = len(matrix_1)
    b = len(matrix_1[0])
    assert b == len(matrix_2)
    c = len(matrix_2[0])
    result = get_zero_matrix(a, c)
    for i in range(a):
        for j in range(b):
            for k in range(c):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result


# 通用矩阵 * 向量：(a, b) * (b, 1) = (a, 1)，注意这里的向量都用平铺的 list 表示，相当于是 (1, b) 或者 (1, a)
# [[1, 1], [1, 0]] * [3, 2] = [5, 3]
def matrix_product_vector(matrix: List[List[int]], vector: List[int]) -> List[int]:
    a = len(matrix)
    b = len(matrix[0])
    assert b == len(vector)
    result = get_zero_vector(a)
    for i in range(a):
        for j in range(b):
            result[i] += matrix[i][j] * vector[j]
    return result


# 注意必须是方阵，方阵快速幂
def square_matrix_fast_power(matrix: List[List[int]], n: int):
    a = len(matrix)
    assert a == len(matrix[0])
    result = get_eye_matrix(a)
    while n:
        n, remainder = divmod(n, 2)
        if remainder == 1:
            result = matrix_product_matrix(result, matrix)
        matrix = matrix_product_matrix(matrix, matrix)
    return result


def main():
    assert isodd(37)
    assert not isodd(46)

    assert fast_power(3, 8) == 3 ** 8
    assert fast_power(4, 6) == 4 ** 6

    a_matrix = [[1, 1], [1, 0]]
    a_matrix_2 = [[2, 1], [1, 1]]
    a_matrix_3 = [[3, 2], [2, 1]]
    assert matrix_product_matrix(a_matrix, a_matrix) == a_matrix_2
    assert matrix_product_matrix(a_matrix_2, a_matrix) == a_matrix_3
    assert matrix_product_vector([[1, 1], [1, 0]], [3, 2]) == [5, 3]
    assert square_matrix_fast_power(a_matrix, 0) == get_eye_matrix(2)
    assert square_matrix_fast_power(a_matrix, 1) == a_matrix
    assert square_matrix_fast_power(a_matrix, 2) == a_matrix_2
    assert square_matrix_fast_power(a_matrix, 3) == a_matrix_3


if __name__ == '__main__':
    main()
