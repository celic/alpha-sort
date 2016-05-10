import verify_list
import argparse
import time
import numpy as np
# Each test boosts the algorithm and records the correct rate
def test(file_name, iterations, alpha, size, delta, error, timeIO):
	average = []
	results = []
	io_time = 0
	for i in xrange(iterations):
		t, io = verify_list.verify(file_name, alpha, size, delta, error, timeIO)
		average.append(t[0])
		results.append(t[1])
		io_time += io

	avg = sum(average)/float(len(average))
	if io_time > 0:
		print "IO time: %20.2fs" % (io_time)
	# this 
	return (float(results.count(True)) / float(iterations)), avg, (alpha-avg)/alpha

def foo(file_name):
	alpha = 0.92
	iterations = 1
	size = 1000000000
	error = 0.1
	delta = 0.25
	avg_error = 0
	count_bad = 0
	max_error = 0
	# for delta in np.arange(0.05,1,0.1):
	for i in xrange(0, 1000):
		s_ratio, avg, err = test(file_name, iterations, alpha, size, delta, error, False)
		avg_error += abs(err)/1000.0
		max_error = max(max_error, abs(err))
		if abs(err) > error:
			count_bad += 1

	print "Average Error: %10.8f, Num out of bound: %d, max_error %10.8f" % (avg_error, count_bad, max_error)

if __name__ == '__main__':
	# Argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("file")
	parser.add_argument("-a", "--alpha", default=0.9)
	parser.add_argument("-i", "--iterations", default=10)
	parser.add_argument("-d", "--delta", default=0.25)
	parser.add_argument("-e", "--error", default=0.1)
	parser.add_argument("-n", "--size", default=1000000000)
	parser.add_argument("-t", "--timeIO", default=False)
	args = parser.parse_args()
	file = args.file
	iterations = int(args.iterations)
	alpha = float(args.alpha)
	size = int(args.size)
	delta = float(args.delta)
	error = float(args.error)
	timeIO = bool(args.timeIO)

	start = time.clock()
	for i in xrange(1):
		print test(file, iterations, alpha, size, delta, error, timeIO)
	end = time.clock()
	print "Total time: %20.2fs" % (end - start)