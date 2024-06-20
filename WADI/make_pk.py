import pandas as pd
import numpy as np
import pickle as pk
import datetime as dt

print('read csv files')
print('Note that this study takes the 2017 data')
trn = pd.read_csv('WADI_14days.csv', skiprows=3)
tst = pd.read_csv('WADI_attackdata.csv')

print('shorten column labels and separate labels')
# shorten column labels
cols = trn.columns.to_numpy()
target_str = '\\\\WIN-25J4RO10SBF\\LOG_DATA\\SUTD_WADI\\LOG_DATA\\'
for i in range(len(cols)):
    if target_str in cols[i]:
        cols[i] = cols[i][len(target_str):]
trn.columns = cols
lab_tst = tst[tst.columns[-1]].to_numpy()

assert len(set(lab_tst)) == 2

tst = tst.drop(columns = [tst.columns[-1]])
tst.columns = cols

print('drop columns and rows')
# drop Row, Date, Time
trn = trn[cols[3:]]
tst = tst[cols[3:]]
cols = cols[3:]

# drop columns that have excessive NaNs
drop_cols = cols[np.isnan(trn.to_numpy()).sum(axis=0) > len(trn) // 2]
tst = tst.drop(columns=drop_cols)
trn = trn.drop(columns=drop_cols)

# convert to numpy array
print('convert to numpy array')
trn_np = trn.to_numpy()
tst_np = tst.to_numpy()
cols = trn.columns.to_numpy()

# fill NAs
print('fill NAs for trn')
nanlist = np.isnan(trn_np).sum(axis=0)
print(nanlist)
for j, nancnt in enumerate(nanlist):
    if nancnt > 0:
        for i in range(len(trn_np)):
            if np.isnan(trn_np[i, j]):
                trn_np[i, j] = trn_np[i-1, j]
                nancnt -= 1
                if nancnt == 0:
                    break
assert np.isnan(trn_np).sum() == 0 and np.isnan(tst_np).sum() == 0

print('save to pickle file')
with open('WADI.pk', 'wb') as file:
    pk.dump({'x_trn': trn_np, 'x_tst': tst_np, 'lab_tst': lab_tst, 'cols': cols}, file)
    
print('done, final x_trn, x_tst, lab_tst shape: ', trn_np.shape, tst_np.shape, lab_tst.shape)
