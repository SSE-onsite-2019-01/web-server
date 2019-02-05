import os
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

models=[]
mean_on_train = np.array([0.01685,0.02573,0.03319,0.03294,2.84323,1.85255,0.00304,-5.80562,16.50286,168.92610,1.25952,2.05074,-14.76173])
std_on_train = np.array([0.01001,0.01668,0.02103,0.02227,1.45765,1.02858,0.01153,7.65851,14.74568,88.52231,2.10341,3.61305,1.44417])

class CalcStress:
    def __init__(self):
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        
        attNum = 13
        nHidden = 20
        activationMethod = 'relu'
        numOfHiddenLayer = 3
        turnNum = 10

        dir = os.path.dirname(__file__)
        
        for turn in range(turnNum):
            seed = 123 + turn
            np.random.seed(seed)
            model = Sequential()
            model.add(Dense(nHidden, activation=activationMethod, input_shape=(attNum,)))
            for j in range(numOfHiddenLayer - 1):
                model.add(Dense(nHidden, activation=activationMethod))
            model.add(Dense(1))
            model.compile(loss='mean_absolute_percentage_error', optimizer='adam')
            model.load_weights(dir + '/param' + str(turn) + '.hdf5')
            models.append(model)
            
    def Calc(self, X):
        X2 = np.array([X]);
        X_scaled = (X2 - mean_on_train) / std_on_train
        predict = 0
        for i in range(len(models)):
            predict += models[i].predict(X_scaled)[0][0]
        predict /= len(models)
        return predict
