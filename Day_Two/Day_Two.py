def checksum(filename):

	with open(filename) as inputfile:

		sum = 0

		for line in inputfile:

			min_value = 10
			max_value = -1

			input_string = str(line.rstrip())
			clean_string = ""

			for i in input_string:

				if i == " " or i == "\t":

					pass

				else:

					clean_string = clean_string + i

			for i in clean_string:
				val = int(i)

				if val < min_value:

					min_value = val

				elif val > max_value:

					max_value = val

				else:

					pass

			diff = max_value - min_value

			sum += diff

		return sum





print(checksum("input.txt"))