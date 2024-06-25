from functions import *
from boxs import*
from converts import*
import numpy as np

#hàm chia chuỗi string dạng hex thành các khối mỗi khối 32 byte
def divide_into_blocks(data):
        blocks = []
        block_size = 32
        num_blocks = len(data) // block_size + (1 if len(data) % block_size > 0 else 0) #số bocks
        for i in range(num_blocks):
            block_start = i * block_size
            block_end = min((i + 1) * block_size, len(data))
            block = data[block_start:block_end]
            # thêm kí tự 0 để đủ 32 bit trong block cuối
            block = pad_hex_string(block)
            blocks.append(block)
        return blocks

#hàm mã hóa
def encrypt(data, keys):
    print(data)
    # #chuyển sang hệ hex dùng utf8
    str_hex = string_to_hex_utf8(data)
    print(str_hex)
    # chia thành các khối 32 bit
    block_data = divide_into_blocks(str_hex)
    
    # finall output
    hex_string= ""

    # do đã chia thành các khối 32 nên sử dụng vòng for để mã hóa từng khôi
    for input_hex in block_data:
        #chuyen sang ma trận
        matrix_hex = (hex_string_to_matrix(input_hex))

        # thực hiện mã hóa
        result = XOR(matrix_hex, np.array(keys[0:4]).T)
        #lặp qua 10 vòng lặp
        for i in range(1,11):
            # subbytes 
            result = permutation(result, S)
            
            new_result= []
            # shift rows
            for j in range(4):
                new_result.append(left_shift(result[j], j))
            result = new_result
        
            # mix columns (vòng thứ 10 thì không thực hiện mix column)
            if i<10:
                result = multiply_matrices_hex(mix_columns_matrix1, result) 

            # xor vói khóa tương ứng (AddRoundKey)
            current_key = np.array(keys[(i)*4:(i)* 4 +4]).T  # lấy khóa tại vòng thứ i
            result = XOR(result, current_key) 


        #chuyen tu ma tra sang str
        for row in result:
            for value in row:
                if len(value)==1: value = '0'+value[0]
                hex_string = hex_string + value     #thêm từng byte sau khi mã hóa và ket qua
    return hex_string 

#hàm giải mã
def cripher(hex_string, keys):
    final_hex = ''
    blocks = divide_into_blocks(hex_string)
    for data in blocks:
        # Chuyển dữ liệu sang dạng ma trận
        data_matrix = hex_string_to_matrix(data)

        # XOR với khóa cuối cùng
        result = XOR(data_matrix, np.array(keys[40:44]).T)

        for i in range(9, -1, -1): 
            # invShift rows
            new_result = []
            for j in range(4):
                new_result.append(right_shift(result[j], j))
            result = new_result

            # invSubBytes (permutation with inverse S-box)
            result = permutation(result, inverse_s_box)

            # XOR với khóa hiện tại (invAddRoundKey)
            current_key = np.array(keys[i * 4 : i * 4 + 4]).T
            result = XOR(result, current_key)

            if i > 0:  # inverse Mix columns
                result = multiply_matrices_hex(mix_columns_matrix2, result)

        # Chuyển từ ma trận sang chuỗi hex
        
        final_hex += hex_matrix_to_string(result)
    
    
    while True:
      
        if final_hex[len(final_hex)-2: len(final_hex)]== '00':
            final_hex = final_hex[:i-2]
        else: break
        
    # Giải mã bytes thành chuỗi tiếng Việt sử dụng UTF-8
    try:
        
        decoded_string = bytes.fromhex(final_hex).decode('utf-8')
        
    except ValueError as e:
        print("Error decoding hex string:", e)
        return None

    return decoded_string
