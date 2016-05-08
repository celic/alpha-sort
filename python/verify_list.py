import random
import argparse

import seek_list

if __name__ == '__main__':

	# Argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("n")
	parser.add_argument("alpha")
	parser.add_argument("file")
	args = parser.parse_args()
	n = int(args.n)
	alpha = float(args.alpha)
	file_name = args.file

	# Load file
	in_file = open(file_name, 'r')

	# Determine k random indexes
	k = 100
	indexes = random.sample(xrange(1, n), k)

	sum = 0

	# For each index check if pair is sorted
	for i in xrange(k):
		values = seek_list.read_pair(indexes[i], in_file)

		if values[0] <= values[1]:
			sum += 1

	# Print estimated alpha
	print sum / float(k)