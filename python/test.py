import random
import argparse

# dunno how to, but this sounds helpful
# seems this has a off by one error
def generateApproxList(size, alpha):
	seq = list()
	nummisses = int(round((1-alpha)*size)) #watch out, this rounds DOWN
	misses = random.sample(xrange(1, size), nummisses) # gets random ids to put misses. skips the first val
	prevVal = 1

	#stupid implementation for now
	for i in xrange(size):
		#randint is inclusive
		if i in misses:
			seq.append(prevVal-1)
		else:
			seq.append(random.randint(prevVal, size*(i+1)))
		prevVal = seq[-1] # this makes it not work
	# for i in xrange(size):
	# 	#randint is inclusive
	# 	if i in misses:
	# 		if prevVal == 1:
	# 			seq.append(0)
	# 		else:
	# 			seq.append(random.randint(0, prevVal-1))
	# 	else:
	# 		seq.append(random.randint(prevVal, size))
	# 	prevVal = max(seq[-1],1) # this makes it not work
	return seq

# really shoddy; should prob use orderedSampleW/oReplacement
def randSelect(seq, sample_size):
	indices = random.sample(xrange(len(seq)), sample_size)
	indices.sort()
	return getAlpha( [seq[i] for i in indices] )

# this is sequential
def getAlpha(seq):
	misses = 0
	lastVal= seq[0]
	nextVal= 0
	for i in seq[1:]:
		nextVal = i
		if nextVal < lastVal:
			misses += 1
		lastVal = nextVal
	return float(len(seq)-misses)/float(len(seq))


# From StackOverflow. It uses a generator though and is O(N), so prolly won't use it
# (unless it is meshed in with generation somehow)
def orderedSampleWithoutReplacement(seq, k):
    if not 0<=k<=len(seq):
        raise ValueError('Required that 0 <= sample_size <= population_size')

    numbersPicked = 0
    for i,number in enumerate(seq):
        prob = (k-numbersPicked)/(len(seq)-i)
        if random.random() < prob:
            yield number
            numbersPicked += 1


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("size")
	parser.add_argument("alpha")
	parser.add_argument("sample")
	args = parser.parse_args()
	size = int(args.size)
	alpha = float(args.alpha)
	sample = int(args.sample)
	# Generates a list of size with alpha-approx
	seq = generateApproxList(size, alpha)
	actual = getAlpha(seq)
	print "Actual alpha: %1.2f" % actual

	# Note: It seems that as alpha decreases, the error increases (this makes sense)
	# So does computation time (also makes sense)

	# rand sample of the entire array
	alpha1 = randSelect(seq, sample)
	err1 = (alpha-alpha1)/alpha*100
	print "Random sampling of entire bin: %1.2f. Error: %1.2f%%" % (alpha1, err1)

	# random consecutive sample
	# Best idea so far
	i = random.randint(0, size-sample)
	alpha2 = randSelect(seq[i:i+sample], sample)
	err2 = (alpha-alpha2)/alpha*100
	print "Random consecutive sample: %1.2f. Error: %1.2f%%" % (alpha2, err2)

	#random sample on a small bin, i.e.
	spb=4 #samples per bin
	i = random.randint(0, size-sample*spb)
	alpha2 = randSelect(seq[i:i+sample*spb], sample)
	err2 = (alpha-alpha2)/alpha*100
	print "Random sample on small bin respective to sample size: %1.2f. Error: %1.2f%%" % (alpha2, err2)

	#random sample on a small bin, i.e.
	frac=0.25 #fraction of total bin
	i = random.randint(0, size-size*frac)
	alpha2 = randSelect(seq[i:i+int(size*frac)], sample)
	err2 = (alpha-alpha2)/alpha*100
	print "Random sample on small bin respective to bin size: %1.2f. Error: %1.2f%%" % (alpha2, err2)


	# for i in xrange(i):
	# 	print randSelect(seq[i:], sample)
	# print getAlpha(orderedSampleWithoutReplacement(seq, sample))