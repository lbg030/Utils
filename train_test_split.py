import os
import shutil
from pathlib import Path 
import argparse

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


#TODO : Valid 까지 split 추가
#TODO : multi defect에 관해서 한번에 처리할 수 있는 logic 필요
#TODO : Json 추가

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default = "/home/lbg030/luna/data/Laser")
    parser.add_argument("--ratio", type=float, default = 0.2, help= "Train과 Test Split 비율")
    
    args = parser.parse_args()
    
    return args

def main(args):
    # dir_paths = os.listdir(args.dir)
    defect_class = os.listdir(args.dir)
    
    train_paths = []
    test_paths = []
    
    train_img_dir = f"{args.dir}/train/images"
    train_label_dir = f"{args.dir}/train/labels"
    test_img_dir = f"{args.dir}/test/images"
    test_label_dir = f"{args.dir}/test/labels"
    
    createFolder(train_img_dir)
    createFolder(train_label_dir)
    createFolder(test_img_dir)
    createFolder(test_label_dir)
    
    
    print(defect_class)
    
    for defect in defect_class:
        img_paths = []
        for path in Path(args.dir).glob(f"{defect}/*"):
            if path.suffix in ['.jpg', '.png']:
                img_paths.append(str(path))
                
        img_paths.sort()
        
        split_points = int(len(img_paths) * args.ratio)
        
        train_img = img_paths[split_points:]
        test_img = img_paths[:split_points]
        
        train_paths.extend(train_img)
        test_paths.extend(test_img)
        
        print(defect)
        print(len(img_paths))
        print(len(train_img))
        print(len(test_img))
        
        for file in train_img:
            json_file = file[:-4] + '.json'
            txt_file = file[:-4] + '.txt'
            # shutil.copy(f"{args.dir}/{file}", f"{train_img_dir}")
            # shutil.copy(f"{args.dir}/{json_file}", f"{train_label_dir}")
            shutil.copy(f"{file}", f"{train_img_dir}")
            shutil.copy(f"{json_file}", f"{train_label_dir}")
            shutil.copy(f"{txt_file}", f"{train_label_dir}")
            
        for file in test_img:
            json_file = file[:-4] + '.json'
            txt_file = file[:-4] + '.txt'
            
            shutil.copy(f"{file}", f"{test_img_dir}")
            shutil.copy(f"{json_file}", f"{test_label_dir}")
            shutil.copy(f"{txt_file}", f"{test_label_dir}")
        
    
if __name__ == "__main__":
    args = parser()
    main(args)
    print("it's done")