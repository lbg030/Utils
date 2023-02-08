import os
import shutil
import json 
from pathlib import Path 
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default = "/Users/gwonsmpro/Desktop/lbg",help="원본 디렉토리")
    parser.add_argument("--move_dir", type=str, default="/Users/gwonsmpro/Desktop/lbg/labeled", help="옮길 폴더 경로")
    args = parser.parse_args()
    return args

def main(args):
    # label_paths = list(Path(args.dir).glob("*.json"))
    # img_paths = list(Path(args.dir).glob("*"))
    img_paths = os.listdir(args.dir)
    img_paths.sort()
    
    for idx,img in enumerate(img_paths):
        # print(img)
        img_json = img[:-4] + ".json"
        if img.endswith(".jpg") and img_json in img_paths:
            shutil.copy(f"{args.dir}/{img}", args.move_dir)
            shutil.copy(f"{args.dir}/{img_json}", args.move_dir)
            
        
    
if __name__=="__main__":
    args = parser()
    # parser를 사용하지 않을시, 아래 예시와 같이 args.dir에 십시일반 데이터가 위치한 경로를 넣어주세요 
    # 예시
    # args.dir = "/Users/injo/Library/Mobile Documents/com~apple~CloudDocs/injo/업무/RTM/projects/dd_aoi/data/십시일반_라벨링_230208/kij"
    main(args)