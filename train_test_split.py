import os
import shutil

dir_name = "/Users/ibyeong-gwon/Desktop/data"
# dir_list = os.listdir(dir_name)
move_dir_name = ""
defect_list = ['yd', 'hz', 'bz', 'chem']
for defect in defect_list :
    cnt = 0 # Random Sampling 용
    file_list = os.listdir(f"{dir_name}/{defect}/raw_image")
    move_dir_name = f"{dir_name}/{defect}/"
    file_len = len(file_list)
    
    split_point = int(file_len * 0.8)
    
    for file in file_list[:split_point]:
        shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "train")
        if cnt < 100:
            shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "cls_train")
            cnt += 1
        
    for file in file_list[split_point:]:
        shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "test")
