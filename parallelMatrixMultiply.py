import argparse
import numpy as np
import matrixUtils
import time
import pymp

a = matrixUtils.genMatrix() 
b = matrixUtils.genMatrix2()
c = pymp.shared.array((len(a),len(b)))

start = time.time()


thread_num = 4

with pymp.Parallel(thread_num) as p1:
	for i in p1.range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				c[i][j] += a[i][k] * b[k][j]

stop = time.time()

print("time: ", (stop-start))
print("threads used:", thread_num)

matrixUtils.printSubarray(c, len(c))