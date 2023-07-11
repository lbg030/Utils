from glob import glob



img_list = glob('/Users/gwonsmpro/Downloads/pillipse/histogram_equal_test/train/images/*.png') # 트레인 이미지 경로
val_img_list = glob('/Users/gwonsmpro/Downloads/pillipse/histogram_equal_test/test/images/*.png') # 테스트 이미지 경로

print(len(img_list))
with open("/Users/gwonsmpro/Downloads/pillipse/histogram_equal_test/train/train.txt", "w") as f:
    f.write('\n'.join(img_list) + '\n')

print(len(val_img_list))
with open('/Users/gwonsmpro/Downloads/pillipse/histogram_equal_test/train/test.txt', 'w') as f:
    f.write('\n'.join(val_img_list) + '\n')