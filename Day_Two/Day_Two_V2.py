def checksum(filename):

	total_sum = 0

	with open(filename) as inputfile:

		for line in inputfile:

			dirty_string = line.rstrip() + " "
			array = []
			num_String = ""

			for char in dirty_string:

				if char == " " or char == "\t":

					array.append(num_String)
					num_String = ""

				else:

					num_String = num_String + char

			for part in array:

				min_value = 10
				max_value = (-1)

				for char in part:

					val = int(char)

					if val < min_value:

						min_value = val

					if val > max_value:

						max_value = val

				difference = max_value - min_value

				total_sum = total_sum + difference

	return total_sum



print(checksum("input.txt"))