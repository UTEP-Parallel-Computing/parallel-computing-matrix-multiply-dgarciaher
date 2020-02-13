#!/usr/bin/env python3
import argparse
import numpy as np
import matrixUtils
import time


a = matrixUtils.genMatrix() 
b = matrixUtils.genMatrix2()

c = np.zeros((len(a),len(a)))

start = time.time()

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			c[i][j] += a[i][k] * b[k][j]

stop = time.time()

print("time: ", (stop-start))

matrixUtils.printSubarray(c, len(c))

