import os
import shutil
from pathlib import Path 
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default = "/Users/gwonsmpro/Downloads/LASER불량이미지/미가공/bottom")
    args = parser.parse_args()
    
    return args


def main(args):
    # dir_paths = os.listdir(args.dir)
    defect_class = os.listdir(args.dir)
    try :
        defect_class.sort(key=lambda x : int(x.split('.')[0]))
    except:
        print("C")
    
    print(defect_class)    
    jpg_list = []
    json_list = []
    
    for file in defect_class:
        if file.endswith('.jpg'):
            jpg_list.append(file)
        else:
            json_list.append(file)
        
    # print(jpg_list)
    # print(json_list)
    
    print(len(jpg_list))
    print(len(json_list))
    
    for idx,file in enumerate(jpg_list):
        idx += 1
        os.rename(f"{str(args.dir)}/{file}", f"{str(args.dir)}/ssol_{idx}_bottom.jpg")
    
    for idx,file in enumerate(json_list):
        idx += 1
        os.rename(f"{str(args.dir)}/{file}", f"{str(args.dir)}/ssol_{idx}_bottom.json")
        
if __name__ == "__main__":
    args = parser()
    main(args)