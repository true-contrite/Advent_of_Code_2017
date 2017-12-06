def solve_captcha_adv(filename):

	sum = 0
	current_index = -1

	with open(filename) as captcha:

		captcha = str(captcha.readline())

	for num in captcha:

		current_index += 1
		half_jump = (len(captcha)/2)
		halfway_index = (current_index + half_jump) %(len(captcha))


		if num == captcha[int(halfway_index)]:

			sum += int(num)

	
	return sum

print(solve_captcha_adv("Captcha1.txt"))
