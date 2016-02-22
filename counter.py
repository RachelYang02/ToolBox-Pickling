""" A program that stores and updates a counter using a Python pickle file"""
import sys

def update_counter(file_name, reset=False):
	# had to move these into the function to avoid global errors 
	# involving os and pickle
	from os.path import exists
	from pickle import dump, load

	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be reset.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	if reset == True or os.path.exists(ffile_name):
		
		f = open(file_name, 'r')		# opens file_name for reading
		counter = pickle.load(f)		# defines counter as what counter was set at in file_name from last run
		f.close()						# closes file_name

		counter += 1					# increases counter by an increment of 1
		
		f = open(file_name, 'w')		# opens file_name for writing
		pickle.dump(counter, f)			# adds counter (increment of 1) to file
		f.close()						# closes file_name

	else:
		f = open(file_name, 'w')		# opens file_name for writing
		pickle.dump(1, f)				# creates and initializes counter at 1 
		f.close()						# closes file_name

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))