import os
import shutil

if __name__ == "__main__":
    cnt = 0
    root_dir = "/Users/ibyeong-gwon/Desktop/data/experiments"
    for (root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                if file_name.endswith(""): # 특정 type remove
                    file_path = root+"/"+file_name
                    try :
                        os.remove(file_path)
                    except:
                        print(root)
                        print("NO")
                        
                    print("file: " + root + file_name)
                    cnt += 1
    print(cnt)