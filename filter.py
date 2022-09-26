# import yaml

# save_dic = {'bz': {'train' :[], 'valid' : [], 'test': []} ,
#             'chem':  {'train' :[], 'valid' : [], 'test': []},
#             'hz':  {'train' :[], 'valid' : [], 'test': []},
#             'yd' :  {'train' :[], 'valid' : [], 'test': []}}

# for defect in ['bz','chem','hz','yd']:
#     for type in ['train','valid','test']:
#         path = f"/Users/ibyeong-gwon/Desktop/data/conv/{defect}/"
#         with open(path + f"{defect}_{type}_experiment9.yaml") as f:
#             file = yaml.load(f, Loader=yaml.FullLoader)
#             save_dic[defect][type].extend(file[type])
            

JUMP = 20
TRAIN = 12
VALID = 15
TEST = 20
EX_NUM = 10

bz = "/Users/ibyeong-gwon/Desktop/회사/bz"
chem = "/Users/ibyeong-gwon/Desktop/회사/chem"
hz = "/Users/ibyeong-gwon/Desktop/회사/hz"
yd = "/Users/ibyeong-gwon/Desktop/회사/yd"

TYPE_LIST = [bz,chem,hz, yd]

import os
import shutil


dic = {'bz': [], 'chem': [], 'hz': [], 'yd' : []}
save_dic = {'bz': {'train' :[], 'valid' : [], 'test': []} ,
            'chem':  {'train' :[], 'valid' : [], 'test': []},
            'hz':  {'train' :[], 'valid' : [], 'test': []},
            'yd' :  {'train' :[], 'valid' : [], 'test': []}}

yaml_dic = {"bz":[],
            "chem": [],
            "hz": [],
            "yd": []}

for _ in range(10):
    
    for dir in TYPE_LIST:
        file_list = os.listdir(dir)[JUMP-20:JUMP]

        defect = (dir.split('/')[-1])

        dic[defect].extend(file_list)
        train_add = file_list[:TRAIN]
        valid_add = file_list[TRAIN:VALID]
        test_add = file_list[VALID:TEST]
        
        train_list = train_add
        save_dic[defect]['train'].extend(train_add)
        yaml_dic[defect].extend(train_add)
        
        valid_list = valid_add
        save_dic[defect]['valid'].extend(valid_add)
        yaml_dic[defect].extend(valid_add)
        
        test_list = test_add
        save_dic[defect]['test'].extend(test_add)
        yaml_dic[defect].extend(test_add)
        
        
        for train in save_dic[defect]['train']:
            shutil.copy(dir+"/"+train, f"/Users/ibyeong-gwon/Desktop/data/experiments/experiment{EX_NUM}/{defect}/train")
            
        for valid in save_dic[defect]['valid']:
            shutil.copy(dir+"/"+valid, f"/Users/ibyeong-gwon/Desktop/data/experiments/experiment{EX_NUM}/{defect}/valid")
            
        for test in save_dic[defect]['test']:
            shutil.copy(dir+"/"+test, f"/Users/ibyeong-gwon/Desktop/data/experiments/experiment{EX_NUM}/{defect}/test")

        # for x in save_dic[defect]:
        #     dic_list = {x: save_dic[defect][x]}
        
        #     with open(f'experiment{EX_NUM}_{x}.yaml', 'w') as f:
        #         yaml.dump(yaml_dic, f)
        
    # shutil.move(f"/Users/ibyeong-gwon/Desktop/data/experiment{EX_NUM}_{x}.yaml", f"/Users/ibyeong-gwon/Desktop/data/experiments/experiment{EX_NUM}/{defect}")

    JUMP += 20
    EX_NUM += 1