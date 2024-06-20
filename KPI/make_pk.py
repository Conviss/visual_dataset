import numpy as np
import pandas as pd
import pickle as pk

pth = './'

df_train = pd.read_csv(pth + "phase2_train.csv")

df_test = pd.read_hdf(pth + "phase2_ground_truth.hdf")
df_test["KPI ID"] = df_test["KPI ID"].astype(str)

name_dfs = df_train.groupby("KPI ID")
train_data = []
train_timestamp = []
train_label = []
for name, df in name_dfs:
    train_data.append(df['value'].to_numpy().reshape(-1,1))
    train_timestamp.append(df['timestamp'].to_numpy().reshape(-1,1))
    train_label.append(df['label'].to_numpy().reshape(-1,1))

name_dfs = df_test.groupby("KPI ID")
test_data = []
test_timestamp = []
test_label = []
for name, df in name_dfs:
    test_data.append(df['value'].to_numpy().reshape(-1,1))
    test_timestamp.append(df['timestamp'].to_numpy().reshape(-1,1))
    test_label.append(df['label'].to_numpy().reshape(-1,1))


print('  Dumping pickle files...')
with open(pth + 'KPI' + '.pk', 'wb') as file:
    pk.dump({'train_data': train_data, 'train_timestamp': train_timestamp,  'train_label': train_label,
             'test_data': test_data, 'test_timestamp': test_timestamp,  'test_label': test_label, }, file)

print('Done')