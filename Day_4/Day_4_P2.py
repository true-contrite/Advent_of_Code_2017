def is_valid_pass_anagram(filename):

	count = 0

	with open(filename) as inputfile:

		for line in inputfile:

			if contains_anagram(line) == False and valid_pass(line) == True:

				count += 1

	return count

def contains_anagram(line):

	array = line.split()

	print(array)

	for word1 in array:

		word1_list = list(word1)
		word1_list.sort()

		for word2 in array:

			word2_list = list(word2)
			word2_list.sort()

			if word1_list == word2_list and word1 != word2:

				return True

	return False
			
def valid_pass(line):

	array = line.split()

	word_set = set(array)

	if len(word_set) == len(array):

		return True

	return False


print(is_valid_pass_anagram("passwords.txt"))