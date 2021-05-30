driving = input('Do you have driving licence?')
age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You are a qualified driver!')
	else:
		print('You are too young to drive!')
else:
	if age >= 18:
		print('Do you consider to apply a driving licence?')
	elif age <18:
		print('You could apply for driving licence when you are 18 years old.')	