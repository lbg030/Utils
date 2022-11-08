import os
import shutil

# 400장 파일
path = "/Users/ibyeong-gwon/Desktop/test"
lst = os.listdir(path)

#원본 파일
path = "/Users/ibyeong-gwon/Desktop/lbg"
lst2 = os.listdir(path)

for x in lst:
    if x not in lst2 :
        print(x)
        