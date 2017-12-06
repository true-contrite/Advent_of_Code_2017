def valid_pass(filename):

	count = 0

	with open(filename) as inputfile:

		for line in inputfile:

			array = line.split()

			word_set = set(array)

			if len(word_set) == len(array):

				count += 1

	return count











print(valid_pass("passwords.txt"))