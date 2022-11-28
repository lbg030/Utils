import json
from pathlib import Path
from collections import defaultdict


data_dir = "/Users/ibyeong-gwon/Downloads/train"
file_list = []

for path in Path(data_dir).glob(f'*') : 
    if path.suffix in ['.txt'] :
        # file_list.append(str(path).split('/')[-1])
        file_list.append(str(path))

dict1 = defaultdict(list)

for filename in file_list:
    dict1 = defaultdict(list)
    file_name = filename.split('/')[-1]

    with open(filename) as fh:
        for line in fh:
            type,x,y,w,h = line.strip().split()
            
            pos = (x,y,w,h)
            
            dict1[type].append(pos)
        
            break
    out_file = open(f"{filename[:-4]}.json", "w")
    json.dump(dict1, out_file, indent = 4, sort_keys = False)
    out_file.close()
    
# import json
# with open("/Users/ibyeong-gwon/Downloads/test/BF31845_210912_133839_PATTERN_3_47_4_0.json", 'r') as f:
#     data = json.load(f)
    
#     print(list(data.keys()))
#     for key in data.keys():
        
#         x,y,w,h = (data[list(data.keys())[0]][0])
        
#         print(x,y,w,h)