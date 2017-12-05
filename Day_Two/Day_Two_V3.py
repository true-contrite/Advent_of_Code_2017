import sys

def checksum(filename):

	with open(filename) as inputfile:

		sum_total = 0

		for line in inputfile:

			array = line.split("\t")

			max_val = 0
			min_val = sys.maxsize

			for val in array:

				if int(val) > max_val:

					max_val = int(val)

				if int(val) < min_val:

					min_val = int(val)

			difference = max_val - min_val

			sum_total += difference

		return sum_total

print(checksum("input.txt"))