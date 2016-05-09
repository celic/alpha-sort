import verify_list
import argparse

# Each test boosts the algorithm and records the correct rate
def test(file_name, iterations, alpha, size, delta, error):
	average = []
	results = []

	for i in xrange(iterations):
		t = verify_list.verify(file_name, alpha, size, delta, error)
		average.append(t[0])
		results.append(t[1])

	avg = sum(average)/float(len(average))

	return (float(results.count(True)) / float(iterations)), avg

if __name__ == '__main__':
	# Argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("file")
	parser.add_argument("-a", "--alpha", default=0.9)
	parser.add_argument("-i", "--iterations", default=10)
	parser.add_argument("-d", "--delta", default=0.25)
	parser.add_argument("-e", "--error", default=0.1)
	parser.add_argument("-n", "--size", default=1000000000)
	args = parser.parse_args()
	file = args.file
	iterations = int(args.iterations)
	alpha = float(args.alpha)
	size = int(args.size)
	delta = alpha = float(args.delta)
	error = float(args.error)


	for i in xrange(1):
		print test(file, iterations, alpha, size, delta, error)