# from glob import glob
# train_img_list = glob('/Users/ibyeong-gwon/Desktop/custom_data/bz/train/*.jpg')

# with open('/Users/ibyeong-gwon/Desktop/Git/Utils/test.txt', 'w') as f:
# 	f.write('\n'.join(train_img_list) + '\n')
 
 
import yaml
with open("/Users/ibyeong-gwon/Desktop/Git/Utils/test.yaml", 'r') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)

data['train'] = '/Users/ibyeong-gwon/Desktop/Git/Utils/test.txt'

with open("/Users/ibyeong-gwon/Desktop/Git/Utils//test.yaml", 'w') as f:
  yaml.dump(data, f)
  