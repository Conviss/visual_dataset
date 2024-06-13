import numpy as np
import pandas as pd
import pickle as pk

pth = './'

labeled_anomalies = pd.read_csv(pth + 'labeled_anomalies.csv')

data_dims = {'SMAP': 25, 'MSL': 55}

for smap_or_msl in ['MSL']:
    print(f'Creating dataset for {smap_or_msl}')
    train_data = []
    test_data = []
    test_label = []
    total_anomaly_points = 0
    for i in range(len(labeled_anomalies)):
        print(f'  -> {labeled_anomalies["chan_id"][i]} ({i+1} / {len(labeled_anomalies)})')
        if labeled_anomalies['spacecraft'][i] == smap_or_msl:
            # load corresponding .npy file in test and train
            np_trn = np.load(pth + 'train/' + labeled_anomalies['chan_id'][i] + '.npy')
            assert np_trn.shape[-1] == data_dims[smap_or_msl]
            print(np_trn)
            train_data.append(np_trn)
            
            np_tst = np.load(pth + 'test/' + labeled_anomalies['chan_id'][i] + '.npy')
            assert np_tst.shape[-1] == data_dims[smap_or_msl]
            test_data.append(np_tst)
            
            labs = labeled_anomalies['anomaly_sequences'][i]
            labs_s = labs.replace('[', '').replace(']', '').replace(' ', '').split(',')
            labs_i = [[int(labs_s[i]), int(labs_s[i+1])] for i in range(0, len(labs_s), 2)]
            
            assert labeled_anomalies['num_values'][i] == len(np_tst)
            y_lab = np.zeros(len(np_tst))
            for sec in labs_i:
                y_lab[sec[0]:sec[1]] = 1
                total_anomaly_points += sec[1] - sec[0]
            test_label.append(y_lab)
    
    print('  There are a total of', total_anomaly_points, 'anomaly points')
    print('  Dumping pickle files...')
    with open(pth + smap_or_msl + '.pk', 'wb') as file:
        pk.dump({'train_data': train_data, 'test_data': test_data, 'test_label': test_label}, file)
    
print('Done')

