import os
import shutil
from pathlib import Path 
import argparse

def create_folder(directory):
    os.makedirs(directory, exist_ok=True)

def split_data(args):
    defect_classes = os.listdir(args.dir)

    for defect in defect_classes:
        img_paths = [str(path) for path in Path(f"{args.dir}/{defect}").glob("*.png")]
        split_point = int(len(img_paths) * args.ratio)
        train_img_paths = img_paths[split_point:]
        test_img_paths = img_paths[:split_point]

        print(defect)
        print(f"Train files: {len(train_img_paths)}")
        print(f"Test files: {len(test_img_paths)}")

        copy_files(train_img_paths, f"{args.dir}/train")
        copy_files(test_img_paths, f"{args.dir}/test")

def copy_files(file_paths, target_dir):
    img_target_dir = f"{target_dir}/images"
    label_target_dir = f"{target_dir}/labels"

    
    
    create_folder(img_target_dir)
    create_folder(label_target_dir)

    for file in file_paths:
        txt_file = file[:-4] + '.txt'
        # json_file = file[:-4] + '.json'
        
        shutil.copy(file, img_target_dir)
        shutil.copy(txt_file, label_target_dir)
        # shutil.copy(json_file, label_target_dir)
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, default="/Users/gwonsmpro/Downloads/pillipse/0822_labeled_pillip")
    parser.add_argument("--ratio", type=float, default=0.2, help="Train and Test split ratio")

    args = parser.parse_args()
    split_data(args)

    print("Done")

if __name__ == "__main__":
    main()
