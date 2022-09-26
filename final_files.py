import yaml

save_dic = {'bz': {'train' :[], 'valid' : [], 'test': []} ,
            'chem':  {'train' :[], 'valid' : [], 'test': []},
            'hz':  {'train' :[], 'valid' : [], 'test': []},
            'yd' :  {'train' :[], 'valid' : [], 'test': []}}

for defect in ['bz','chem','hz','yd']:
    for type in ['train','valid','test']:
        path = f"/Users/ibyeong-gwon/Desktop/data/conv/{defect}/"
        with open(path + f"{defect}_{type}_experiment9.yaml") as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
            save_dic[defect][type].extend(file[type])
            
