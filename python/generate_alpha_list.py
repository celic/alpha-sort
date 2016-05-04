import random
import argparse

def generate_alpha_approx_list(size, alpha, out_file):
	
	# Check alpha value
	if not 0 <= alpha <= 1:
		raise ValueError("Alpha must be between 0 and 1")

	# Helpful intializations
	modifier = 1
	prev_val = 0

	# Generate values
	for i in xrange(size):

		# If prob is less than alpha, add the value
		prob = random.random()
		if prob <= alpha:
			modifier = 1

		# If prob is greater than alpha, subtract the value
		else:
			modifier = -1

		# Determine value
		val = (modifier * random.randint(1, 5)) + prev_val
		
		# Let's keep things postiive
		if val < 0: val = 0

		# Write and set up next iteration
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