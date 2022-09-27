import os
root = "/Users/ibyeong-gwon/Desktop/data/experiments"
files = {}
walk = [root]
tmp = []
while walk:
    folder = walk.pop(0)+"/"
    items = os.listdir(folder) # items = folders + files
    for i in items:
        i=folder+i
        (walk if os.path.isdir(i) else tmp).append(i)
    files[folder] = tmp
    tmp = []
# print(files.keys())
# print(files.values())
for x in files.keys():
    if len(files[x]):
        print(x)
        print(len(files[x]))