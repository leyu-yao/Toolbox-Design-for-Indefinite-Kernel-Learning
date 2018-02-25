# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 20:39:12 2018

@author: Dynasting
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:23:45 2017

@author: Dyt
"""
import LSSVM
import numpy
import Dataset


Train = numpy.loadtxt('dataset//SPECT_train.txt')

X = Train[:,1:-1]

Y = Train[:,0]




NorX = Dataset.Normalization()
NorX.fit(X)

NorY = Dataset.Normalization()
NorY.fit(Y)

X_N = NorX.fT(X)

Y_N = NorY.fT(Y)

Y_N = Y_N * 2 -1



Test = numpy.loadtxt('dataset//SPECT_test.txt')

X_t = Test[:,1:-1]

Y_t = Test[:,0]






X_N_t = NorX.fT(X_t)

Y_N_t = NorY.fT(Y_t)

Y_N_t = Y_N_t * 2 -1



(alpha,b,K) = LSSVM.LSSVM_CV(X_N,Y_N,'RBF',[0.01,0.1,1,10,100],[0.01,0.1,1,10,100],arg2 = None)

Y_predict = LSSVM._LSSVMpredict(X_N_t,K,alpha,b)

acc = LSSVM._compare(Y_N_t,Y_predict)

print(acc)