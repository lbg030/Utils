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
        
        
        

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default = "/Users/gwonsmpro/Downloads/LASER불량이미지/쏠림")
    
    args = parser.parse_args()
    
    return args


def main(args):
    # dir_paths = os.listdir(args.dir)
    defect_class = os.listdir(args.dir)
    defect_class.sort()
    
    
    top_list = []
    bottom_list = []
    
    top_path = f"{args.dir}/top"
    bottom_path = f"{args.dir}/bottom"
    
    createFolder(top_path)
    createFolder(bottom_path)
    
    print(len(defect_class))

    img_paths = []
    for idx, path in enumerate(Path(args.dir).glob("*")):
        if path.suffix in ['.jpg','.png']:
            name = str(path).split("/")[-1].split(".")[0]

            if int(name) < 100:
                if int(name) % 2 == 0:
                    shutil.copy(f"{str(path)}", f"{top_path}")
                else :
                    shutil.copy(f"{str(path)}", f"{bottom_path}")
            else :
                # if int(name) % 2 == 0:
                shutil.copy(f"{str(path)}", f"{bottom_path}")
                # else :
                #     shutil.copy(f"{str(path)}", f"{top_path}")
                    
if __name__ == "__main__":
    args = parser()
    main(args)
    print("it's done")