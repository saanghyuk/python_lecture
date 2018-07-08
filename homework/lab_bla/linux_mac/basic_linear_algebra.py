from functools import reduce

def vector_size_check(*vector_variables):

    length = [len(i) for i in vector_variables]
    result_bool = True
    check=length[0]
    for i in range(0, len(length)):
        if(length[i] != check):
            result_bool = False
            break;
    return result_bool



def vector_addition(*vector_variables):
    results=""
    if not (vector_size_check(*vector_variables)):
        raise ArithmeticError
    else:
        results = [sum(t) for t in zip(*vector_variables)]

    return results



def vector_subtraction(*vector_variables):
    results=""
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    else:
        # pair_tuple = [t for t in zip(*vector_variables)]
        pair_tuple = [ t for t  in zip(*vector_variables)]
        list=[]
        for i in pair_tuple:
            sub=i[0]
            for j in range(1, len(i)):
                sub -= i[j]
            list.append(sub)
        results=list
        return results

# print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
# print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]


def scalar_vector_product(alpha, vector_variable):
    results = [i*alpha for i in vector_variable]
    return results



def matrix_size_check(*matrix_variables):
    row_num = [len(i) for i in matrix_variables]
    col_num = [[len(j) for j in i ] for i in matrix_variables ]
    # print("===========")
    # print(row_num)
    # print(col_num)
    results = True
    check=row_num[0]
    for j in row_num:
        if(j != check):
            results = False
            break
        else:
            check=j


    # for i in zip(*col_num):
    #     for j in range(0, len[0]):


    return results
#
#
# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]
#
# print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
# print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
# print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True


def is_matrix_equal(*matrix_variables):
    results =True
    if not matrix_size_check(*matrix_variables):
        results = False
    for i in zip(*matrix_variables):
        print(i)
        for j in zip(*i):
            compare_num=j[0]
            for k in range(0, len(j)):
                if (j[k] == compare_num):
                    compare_num=j[k]
                else:
                    results= False
                    break
        # for j in range(0, len(i)):
        #     print(i[j])
    return results

def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    # print(*matrix_variables)
    sum = [i for i in zip(*matrix_variables)]
    list=[]
    for i in range(0, len(sum)):
        list.append(vector_addition(*sum[i]))
    results=list
    return results

def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    sub = [i for i in zip(*matrix_variables)]
    list=[]
    for i in range(0, len(sub)):
        list.append(vector_subtraction(*sub[i]))
    results=list
    return results

def matrix_transpose(matrix_variable):
    result = [[element for element in t] for t in zip(*matrix_variable)]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    result = [[alpha*element for element in t] for t in matrix_variable]
    return result




def is_product_availability_matrix(matrix_a, matrix_b):
    if(len(matrix_a[0])==len(matrix_b)):
        # print(len(matrix_a[0]))
        # print(len(matrix_b))
        results = True
    else:
        # print(len(matrix_a[0]))
        # print(len(matrix_b))
        results = False
    # print(len[])
    return results

def matrix_product(mat1, mat2):
    matR = [ len(mat2[0])*[0] for i in range (len(mat1)) ]

    for i in range (len(matR) ):
        for j in range ( len(matR[i]) ):
            for k in range ( len(mat1[i] ) ):
                matR[i][j] += mat1[i][k]*mat2[k][j]

    return matRm


# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
# print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
# print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
# print(matrix_product(matrix_z, matrix_w)) # Expected value: False
