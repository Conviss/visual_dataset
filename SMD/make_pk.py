import os
import pickle as pk

import numpy as np
import pandas as pd

pth = './'
# 定义自定义的排序键函数
def natural_sort_key(s):
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# 对文件名列表进行自然排序
ent_names = sorted(os.listdir(pth + 'train'), key=natural_sort_key)

train_data, test_data, test_label = [], [], []
for ent_name in ent_names:
    train_data.append(pd.read_csv(pth + 'train/' + ent_name, header=None).to_numpy())
    test_data.append(pd.read_csv(pth + 'test/' + ent_name, header=None).to_numpy())
    test_label.append(np.squeeze(pd.read_csv(pth + 'test_label/' + ent_name, header=None).to_numpy()))

train_data = np.concatenate(train_data, axis=0)
test_data = np.concatenate(test_data, axis=0)
test_label = np.concatenate(test_label, axis=0)

print('  Dumping pickle files...')
with open(pth + 'SMD.pk', 'wb') as file:
    pk.dump({'train_data': train_data, 'test_data': test_data, 'test_label': test_label}, file)

print('done')