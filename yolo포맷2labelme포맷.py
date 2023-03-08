import json
import os
import cv2

def convert_yolo_to_labelme(txt_file_path, img_file_path, labelme_file_path):
    with open(txt_file_path, 'r') as f:
        yolo_lines = f.readlines()

    # 이미지 파일을 읽어서 이미지 크기를 가져옵니다.
    img = cv2.imread(img_file_path)
    height, width, channels = img.shape

    labelme_data = {"version": "4.5.7", "flags": {}, "shapes": [], "imagePath": "", "imageData": None}

    # LabelMe 데이터 구조에 이미지 크기를 설정합니다.
    labelme_data["imageWidth"] = width
    labelme_data["imageHeight"] = height

    # 이미지 파일명에서 .jpg 확장자를 제거한 이름을 이미지 경로로 설정합니다.
    img_file_name = os.path.splitext(os.path.basename(img_file_path))[0]
    labelme_data["imagePath"] = img_file_name + ".jpg"

    # YOLO 파일의 각 줄마다 반복합니다.
    for line in yolo_lines:
        label, x_center, y_center, box_width, box_height = line.strip().split(' ')

        # YOLO 형식의 좌표 값을 float형으로 변환합니다.
        x_center, y_center, box_width, box_height = float(x_center), float(y_center), float(box_width), float(box_height)

        # 좌표 값을 x1, y1, x2, y2로 변환합니다.
        x1 = round((x_center - box_width / 2) * width), 
        y1 = ((y_center - box_height / 2) * height)
        x2 = ((x_center + box_width / 2) * width)
        y2 = ((y_center + box_height / 2) * height)

        # LabelMe 모양 데이터 구조를 만듭니다.
        shape = {"label": label, "points": [[x1, y1], [x2, y2]], "group_id": None, "shape_type": "rectangle", "flags": {}}

        # LabelMe 데이터 구조의 모양 목록에 모양을 추가합니다.
        labelme_data["shapes"].append(shape)

    # LabelMe 데이터 구조를 .json 파일로 쓰기
    with open(labelme_file_path, 'w') as f:
        json.dump(labelme_data, f)

# 사용 예시:
name ="test"
txt_file_path = f'{name}.txt'
img_file_path = f'{name}.jpg'
labelme_file_path = f'{name}.json'
convert_yolo_to_labelme(txt_file_path, img_file_path, labelme_file_path)
