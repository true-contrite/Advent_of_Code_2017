#num = 277678
num = 100

odd_square = []
tv_arr = []
pos_higher = None

for i in range(0, num+1):

	val = i ** 2

	if val % 2 != 0:

		odd_square.append(val)

for i in odd_square:

	if i > num:

		tv_arr = [odd_square[odd_square.index(i)-1], i]
		break

lower = num - tv_arr[0]
upper = tv_arr[1] - num

if lower > upper:

	closest_val = tv_arr[1]
	pos_higher = True

elif upper > lower:

	closest_val = tv_arr[0]
	pos_higher = False

if pos_higher == True:

	print("Closest Odd Square is " + str(closest_val) + " : This value is after " + str(num) )

elif pos_higher == False:

	print("Closest Odd Square is " + str(closest_val) + " : This value is before " + str(num) )








		

