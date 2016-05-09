import random
import argparse
import math

import seek_list

def verify(alpha, file_name):

	# We assume how large the file is, 1bil
	n = 1000000000

	# Load file
	in_file = open(file_name, 'r')

	# Determine k random indexes
	k = int(math.ceil((4 / (.1**2 * alpha)) * math.log(2/.25)))
	# This is roughly 5300 samples. epsilon is .05, and delta is .1, 50 iterations, 90 minutes, 100% accuracy
	# This is roughly 925 samples. epsilon is .1, and delta is .25, 50 iterations, 15 minutes, 100% accuracy
	# This is roughly 925 samples. epsilon is .1, and delta is .25, 5 iterations, 1 min 40sec, 100% accuracy
	sum = 0

	# Monte Carlo over k samples
	for i in xrange(k):

		# Determine sample
		index = random.randint(1, n-1)
		values = seek_list.read_pair(index, in_file)

		# Check result
		if values[0] <= values[1]:
			sum += 1

	# Return estimated alpha
	return ((sum / float(k)), ((sum / float(k)) >= alpha))

if __name__ == '__main__':

	# Argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("alpha")
	parser.add_argument("file")
	args = parser.parse_args()
	alpha = float(args.alpha)
	file_name = args.file

	print verify(alpha, file_name)