import json
from collections import defaultdict

filename = "testing.txt"

dict1 = defaultdict(list)

with open(filename) as fh:
    for line in fh:
        type,x,y,w,h = line.strip().split()
        pos = (x,y,w,h)
        
        dict1[type].append(pos)
        

out_file = open(f"{filename[:-4]}.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()