def adv_checksum(filename):

	with open(filename) as inputfile:

		sum_total = 0

		for line in inputfile:

			array = line.rstrip().split("\t")

			for val1 in array:

				for val2 in array:

					if int(val1) % int(val2) == 0 and int(val1) != int(val2):

						sum_total += (int(val1) / int(val2))

	return int(sum_total)

print(adv_checksum("input.txt"))