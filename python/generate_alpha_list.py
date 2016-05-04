import random
import argparse
import math

def generate_alpha_approx_list(size, alpha, out_file):
	if not 0 <= alpha <= 1:
		raise ValueError("Alpha must be between 0 and 1")

	num_swaps = math.floor(alpha*size)
	modifier = 1
	prev_val = 0

	for i in xrange(size):
		prob = random.random()
		if prob <= alpha:
			modifier = 1
		else:
			modifier = -1
		val = (modifier * random.randint(1, 5)) + prev_val
		if val < 0: val = 0
		out_file.write(str(val) + "\n")
		prev_val = val

if __name__ == "__main__":

	# Argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("size")
	parser.add_argument("alpha")
	parser.add_argument("file")
	args = parser.parse_args()
	size = int(args.size)
	alpha = float(args.alpha)
	out_file_name = args.file

	# Create output file
	out_file = open(out_file_name, "w+")

	# Generate list
	generate_alpha_approx_list(size, alpha, out_file)

	# Close output file
	out_file.close