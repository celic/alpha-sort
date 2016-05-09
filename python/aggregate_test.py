import verify_list

# Each test boosts the algorithm and records the correct rate
def test():
	file_name = 'good.list'
	alpha = .9
	iterations = 10

	average = []
	results = []

	for i in xrange(iterations):
		t = verify_list.verify(alpha, file_name)
		average.append(t[0])
		results.append(t[1])

	avg = sum(average)/float(len(average))

	return (float(results.count(True)) / float(iterations)), avg

if __name__ == '__main__':
	
	for i in xrange(1):
		print test()