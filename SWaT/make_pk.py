import numpy as np
import pandas as pd
import datetime as dt
import pickle as pk

pth = './'

trn = pd.read_csv('SWaT_Dataset_Normal_v1.csv')
tst = pd.read_csv('SWaT_Dataset_Attack_v0.csv')

channels = trn.columns[1:-1]
train_data = trn[trn.columns[1:-1]].to_numpy()
test_data = tst[tst.columns[1:-1]].to_numpy()
test_label = tst['Normal/Attack'].to_numpy()
test_label[test_label == 'Normal'] = 0
test_label[test_label == 'Attack'] = 1
test_label[test_label == 'A ttack'] = 1
lab_tst = np.array(test_label, dtype = int)


with open(pth + 'SWaT.pk', 'wb') as file:
    pk.dump({'train_data': train_data, 'test_data': test_data, 'test_label': test_label}, file)

print('done')
