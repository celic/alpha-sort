
# assumes file has already been opened
def read_element(element, file):

	# Elements are labeled 1-n, not 0-(n-1) so we adjust the element number
	element -= 1

	# There are 11 bytes per line. 10 for the number, 1 for newline
	offset = element * 11
	
	# Find that spot in the file
	file.seek(offset)

	# Read and cast
	value = int(file.read(11))

	# Return
	return value

def read_pair(element, file):

	# Elements are labeled 1-n, not 0-(n-1) so we adjust the element number
	element -= 1
	
	# There are 11 bytes per line. 10 for the number, 1 for newline
	offset = element * 11

	# Find that spot in the file
	file.seek(offset)

	# Read and cast
	val1 = int(file.read(11))
	val2 = int(file.read(11))

	# Return
	return (val1, val2)

# testing for these methods
if __name__ == '__main__':
	f = open('small.list', 'r')
	print read_element(1, f)
	print read_element(2, f)
	print read_element(100, f)
	print read_element(50, f)

	print read_pair(1, f)
	print read_pair(2, f)
	print read_pair(100, f)
	print read_pair(50, f)
