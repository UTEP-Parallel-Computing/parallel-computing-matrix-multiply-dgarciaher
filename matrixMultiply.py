#!/usr/bin/env python3
import argparse
import numpy as np
import matrixUtils
import time

a = matrixUtils.genMatrix() #[[3,5,6,3,5,6,3,5,6,3,5,6],[6,5,4,3,5,6,3,5,6,3,5,6],[7,3,2,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6]]#matrixUtils.genMatrix()
b = matrixUtils.genMatrix2()#[[3,5,6,3,5,6,3,5,6,3,5,6],[6,5,4,3,5,6,3,5,6,3,5,6],[7,3,2,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6],[3,5,6,3,5,6,3,5,6,3,5,6]]#matrixUtils.genMatrix2()

c = np.zeros((len(a),len(a)))

start = time.time()

for i in range(len(a)):
	for j in range(len(b[0])):
		for k in range(len(b)):
			c[i][j] += a[i][k] * b[k][j]

stop = time.time()

print("time: ", (stop-start))

matrixUtils.printSubarray(c, len(c))

