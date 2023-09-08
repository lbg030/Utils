import yaml
with open("/Users/ibyeong-gwon/Desktop/Git/Utils/test.yaml", 'r') as f:
  data = yaml.load(f, Loader=yaml.FullLoader)

data['train'] = '/Users/ibyeong-gwon/Desktop/Git/Utils/test.txt'

with open("/Users/ibyeong-gwon/Desktop/Git/Utils//test.yaml", 'w') as f:
  yaml.dump(data, f)
  