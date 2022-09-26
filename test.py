import os
import shutil
lst = []


# path = "/Users/ibyeong-gwon/Desktop/data/experiments/experiment19/bz/train"
# file_list = os.listdir(path)
# path = "/Users/ibyeong-gwon/Desktop/data/experiments/experiment19/bz/test"
# file_list += os.listdir(path)
# path = "/Users/ibyeong-gwon/Desktop/data/experiments/experiment19/bz/valid"
# file_list += os.listdir(path)

path = "/Users/ibyeong-gwon/Desktop/data/fst/yd/images"
file_list = os.listdir(path)

path2 = "/Users/ibyeong-gwon/Desktop/fst/yd/images" # 200장 experiments9
file2_list = os.listdir(path2)

for x in file_list:
    if x not in file2_list:
        lst.append(x)


print(len(lst))

for file in lst:
    try :
        shutil.copy("/Users/ibyeong-gwon/Desktop/data/fst/yd/images/" + file,"/Users/ibyeong-gwon/Desktop/회사/yd")
    except:
        print("1")