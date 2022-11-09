import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
## hz bz chem yd
## 1732 448 330 169 
## 12 3.5 3 1.5 -> 20

## -> 



dir_name = "/Users/ibyeong-gwon/Desktop/custom_data"
# dir_list = os.listdir(dir_name)
move_dir_name = ""
defect_list = ['yd', 'hz', 'bz', 'chem']

defect_dict = {'hz':120,
                'bz':35,
                'chem':30,
                'yd':15}

for defect in defect_list :
    cnt = 0 # Random Sampling 용
    file_list = os.listdir(f"{dir_name}/{defect}/train")
    # move_dir_name = f"{dir_name}/{defect}/"
    move_dir_name = f"/Users/ibyeong-gwon/Desktop/custom_data/cls/{defect}/"
    file_len = len(file_list)
    
    num = 5
    split_point = defect_dict[defect] * num
    
    print(defect, split_point)
    # for file in file_list[:split_point]:
    #     shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "train")
    #     if cnt < 100:
    #         shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "cls_train")
    #         cnt += 1
        
    # for file in file_list[split_point:]:
    #     shutil.copy(f"{dir_name}/{defect}/raw_image/{file}", move_dir_name + "test")

    
    for file in file_list[:split_point]:
        try :
            createFolder(f'/Users/ibyeong-gwon/Desktop/custom_data/cls/{defect}/cls_train{num}')
        except:
            print("Error")
            
        shutil.copy(f"{dir_name}/{defect}/train/{file}", move_dir_name + f"cls_train{num}")
        
