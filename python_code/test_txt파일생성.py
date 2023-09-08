from glob import glob

base = "/Users/gwonsmpro/Downloads/pillipse/0822_labeled_pillip"

img_list = glob(f'{base}/train/images/*.png') # 트레인 이미지 경로
val_img_list = glob(f'{base}/test/images/*.png') # 테스트 이미지 경로

print(len(img_list))
with open(f"{base}/train/train.txt", "w") as f:
    f.write('\n'.join(img_list) + '\n')

print(len(val_img_list))
with open(f'{base}/train/test.txt', 'w') as f:
    f.write('\n'.join(val_img_list) + '\n')