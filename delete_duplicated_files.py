import os
cnt = 0
type_list = ['bz','chem','dis','hz','ul','yd']
list_200 = os.listdir("/Users/ibyeong-gwon/Desktop/회사/200per/raw_image")
for file in list_200:
    if file[-4:] == '.jpg':
        os.remove(file)
        cnt += 1
        
print(cnt)


# os.path.exists(f"/Users/ibyeong-gwon/Desktop/회사/200per/ul")