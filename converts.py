import numpy as np
def string_to_hex_utf8(input_string):
    # Chuyển đổi chuỗi ký tự sang byte array sử dụng mã hóa UTF-8
    byte_array = input_string.encode('utf-8')
    
    # Chuyển đổi byte array sang chuỗi hex
    hex_string = byte_array.hex()
    return hex_string


def pad_hex_string(hex_string, length=32):
    # Đệm thêm '0' vào cuối chuỗi hex nếu chưa đủ độ dài yêu cầu
    if len(hex_string) < length:
        hex_string = hex_string.ljust(length, '0')
    return hex_string

def hex_string_to_matrix(hex_string):
    matrix = []
    for i in range(0, len(hex_string), 8):
        column = [hex_string[j:j+2] for j in range(i, i+8, 2)]
        matrix.append(column)
    return (matrix)

def hex_matrix_to_string(hex_matrix):
     #chuyen tu ma tra sang str
    hex_string= ""
    for row in hex_matrix:
        for value in row:
            if len(value)==1: value = '0'+value[0]
            hex_string = hex_string + value
    return hex_string