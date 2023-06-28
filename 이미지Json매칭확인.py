import os
import shutil

source_directory = '/Users/gwonsmpro/Desktop/src/data/edited_train/train/1' # 원본 폴더 경로
destination_directory = '/Users/gwonsmpro/Desktop/edited_train/1' # 이동할 폴더 경로

for filename in os.listdir(source_directory):
    if filename.endswith('.png'): # 이미지 파일인 경우
        json_filename = filename.split('.')[0] + '.json' # 해당 이미지와 매칭되는 JSON 파일 이름 생성
        if os.path.isfile(os.path.join(source_directory, json_filename)): # 생성된 JSON 파일이 존재하는 경우
            # 이미지 파일과 JSON 파일을 새로운 폴더로 이동시킴
            shutil.copy(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))
            shutil.copy(os.path.join(source_directory, json_filename), os.path.join(destination_directory, json_filename))
            print(f"Moved files: {filename} and {json_filename} to {destination_directory}")
