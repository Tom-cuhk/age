driving = input('Do you have driving licence?')
if driving != 'yes' and driving != 'no':
	print ('You should only type yes/no.')
	raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You are a qualified driver!')
	else:
		print('You are too young to drive!')
elif driving == 'no':
	if age >= 18:
		print('Do you consider to apply a driving licence?')
	else:
		print('You could apply for driving licence when you are 18 years old.')	
