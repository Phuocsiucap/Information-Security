from boxs import*
from functions import *

# ham trans
def trans(w, j):
    #rotword  sử dụng hàm left_shift() dịch trái trong file functions.py
    result = left_shift(w,1) 
    # subWord: sử dụng hàm permutation2() hàm chuyển đổi cho ma trận bậc1
    result = permutation2(result, S) 
    # tạo khóa con sử dụng bảng RC trong file boxs.py
    Rcon = [RC[int(j-1)], '00', '00', '00']\
    # Xor với r Rcon sử dụng hàm XOR1 hàm xor 2 ma trận bậc 1 với nhau trong functions.py
    result = XOR1(result, Rcon)
    return result

def key():
    w = []
    #biến các cột của ma trận khóa ban đầu thành các w0 w1 w2 w3
    for col1 in zip(*key_box):
        w.append(col1)

    #tạo lần lượt các w từ w4 đến w33
    for j in range(4,44):
        #hàm XOR1 hàm xor 2 ma trận bậc 1 với nhau trong functions.py
        if j%4==0:
            w.append(XOR1(trans(w[j-1], j/4) , w[j-4]))
        else:
            w.append(XOR1(w[j-1] , w[j-4]))
    return w

# đây là ma trận khóa ban đầu cần giữ bí mật
key_box = [
    ['2b', '28', 'ab', '09'],
    ['7e', 'ae', 'f7', 'cf'],
    ['15', 'd2', '15', '4f'],
    ['16', 'a6', '88', '3c']
]