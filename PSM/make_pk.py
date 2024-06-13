import os
import pickle as pk

import numpy as np
import pandas as pd

pth = './'

train_data = pd.read_csv('train.csv').to_numpy()
test_data = pd.read_csv('test.csv').to_numpy()
test_label = pd.read_csv('test_label.csv').to_numpy()

print('  Dumping pickle files...')
with open(pth + 'PSM.pk', 'wb') as file:
    pk.dump({'train_data': train_data[:, 1:], 'test_data': test_data[:, 1:], 'test_label': test_label[:, 1]}, file)

print('done')