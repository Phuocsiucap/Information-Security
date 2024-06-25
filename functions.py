# hàm chuyển đổi cho ma tran bậc 2 trở lên
def permutation(data, mordel):
    result = []
    for row in data:
        newRow = []
        for value in row:
            if(len(value)==1):
                value ='0' + value[0]
            newRow.append(mordel[int(value[0],16)][int(value[1],16)])
        result.append(newRow)
    return result

# hàm chuyển đổi cho ma tran bậc 1 
def permutation2(data, mordel):
    result = []
    for value in data:
        if(len(value)==1):
            value ='0' + value[0]
        result.append(mordel[int(value[0],16)][int(value[1],16)])
    return result

# ham XOR1 giua cac array 1 chiều
def XOR1 (a, b):
    result = []
    for i in range(4):
        result.append(hex(int(a[i], 16) ^ int(b[i], 16))[2:])
    return result

# ham XOR giua cac array n chiều
def XOR (a, b):
    result = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(hex(int(a[i][j], 16) ^ int(b[i][j], 16))[2:])
        result.append(row)
    return result

#ham dich byte sang trai n byten 
def left_shift(data, shifts):
    return data[shifts:] + data[:shifts]

#ham dich byte sang phai n byten 
def right_shift(data, shifts):
    return data[(len(data)-shifts):] + data[:(len(data)-shifts)]

#Nhan 2 ma tran
def multiply_matrices_hex(matrix1, matrix2):
    result = [[0] * 4 for _ in range(4)]
    
    for i in range(4):
        for j in range(4):
            result[i][j] = (hex(galois_multiply(int(matrix1[i][0], 16), int(matrix2[0][j], 16)) ^
                            galois_multiply(int(matrix1[i][1], 16), int(matrix2[1][j], 16)) ^
                            galois_multiply(int(matrix1[i][2], 16), int(matrix2[2][j], 16)) ^
                            galois_multiply(int(matrix1[i][3], 16), int(matrix2[3][j], 16))))[2:]
    return result



def galois_multiply(a, b):
    # Số nguyên thủy trong trường Galois 2^8
    p = 0x11B
    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        high_bit_set = a & 0x80
        a <<= 1
        if high_bit_set:
            a ^= p
        b >>= 1
    return result & 0xFF


