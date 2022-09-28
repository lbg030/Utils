import os
import shutil


bz = "/Users/ibyeong-gwon/Desktop/회사/bz"
chem = "/Users/ibyeong-gwon/Desktop/회사/chem"
hz = "/Users/ibyeong-gwon/Desktop/회사/hz"
yd = "/Users/ibyeong-gwon/Desktop/회사/yd"

destination = "/Users/ibyeong-gwon/Desktop/회사/real"

TYPE_LIST = [bz,chem,hz, yd]
defect_list = ['bz','chem','hz','yd']

for defect in TYPE_LIST:
    file_list = os.listdir(defect)

    for file in file_list:
        try:
            if defect == bz:
                shutil.copy(f"/Users/ibyeong-gwon/Desktop/fullfst/bz/raw_image/{file}", f"{destination}/bz")
            
            elif defect == chem: 
                shutil.copy(f"/Users/ibyeong-gwon/Desktop/fullfst/chem/raw_image/{file}", f"{destination}/chem")
                
            elif defect == hz:
                shutil.copy(f"/Users/ibyeong-gwon/Desktop/fullfst/hz/raw_image/{file}", f"{destination}/hz")
            
            else :
                shutil.copy(f"/Users/ibyeong-gwon/Desktop/fullfst/yd/raw_image/{file}", f"{destination}/yd")
        
        except:
            print(file)