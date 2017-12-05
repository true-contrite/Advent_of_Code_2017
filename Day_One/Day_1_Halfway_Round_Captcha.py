def solve_captcha_adv(filename):

	with open(filename) as captcha:

		captcha = str(captcha.readline())

	num_list = []
	sum = 0
	last_num = None

	for i in captcha:

		num_list.append(int(i))

	list_length = len(num_list)
	print(list_length)

	for number in num_list:

		
		index_pos = num_list.index(number)

		next_index = ((index_pos + (list_length/2)) % list_length+1)

		if number == num_list[int(next_index)]:

			sum += number

	return sum


#print(solve_captcha_adv("test.txt"))
print(solve_captcha_adv("Captcha1.txt"))


