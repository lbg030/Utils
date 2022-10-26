import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 



dir_name = "/Users/ibyeong-gwon/Desktop/fst/data"
# dir_list = os.listdir(dir_name)
move_dir_name = ""
defect_list = ['yd', 'hz', 'bz', 'chem']

defect_dict = {'hz':253,
                'bz':29,
                'chem':66,
                'yd':52}

for defect in defect_list :
    cnt = 0 # Random Sampling 용
    file_list = os.listdir(f"{dir_name}/{defect}/raw_image")
    # move_dir_name = f"{dir_name}/{defect}/"
    move_dir_name = f"/Users/ibyeong-gwon/Desktop/fst/{defect}/"
    file_len = len(file_list)
    
    split_point = defect_dict[defect]-1
    
    # for file in file_list[:split_point]:
    #     shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "train")
    #     if cnt < 100:
    #         shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "cls_train")
    #         cnt += 1
        
    # for file in file_list[split_point:]:
    #     shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "test")

    num = 5
    for file in file_list[:split_point]:
        try :
            createFolder(f'/Users/ibyeong-gwon/Desktop/fst/{defect}/cls_train{num}')
        except:
            print("Error")
            
        shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + f"cls_train{num}")
        
