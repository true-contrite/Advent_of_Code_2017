def solve_captcha(filename):

	with open(filename) as captcha:

		captcha = str(captcha.readline())

	num_list = []
	sum = 0
	last_num = None

	for i in captcha:

		num_list.append(int(i))

	for number in num_list:

		if number == last_num:

			sum += number

		last_num = number

	if num_list[0] == num_list[-1]:

		sum += num_list[0]

	return sum

print(solve_captcha("Captcha1.txt"))


