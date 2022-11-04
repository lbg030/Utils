import os
import shutil

if __name__ == "__main__":
    cnt = 0
    root_dir = "/Users/ibyeong-gwon/Desktop/mecaro"
    file_list = os.listdir(root_dir)
    for file in file_list:
        if file.endswith(".json"):
            jpg = file[:-4] + "jpg"
            # print(jpg)
            shutil.copy(f"{root_dir}/{file}", f"{root_dir}/labeling")
            shutil.copy(f"{root_dir}/{jpg}", f"{root_dir}/labeling")