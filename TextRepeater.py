get_text = str(input("Enter your text :"))
get_amount =int(input("Enter amount :"))

if get_amount <= 100000:
	get_type = input("Selact style [1] list [2] grid \n( Type 1 or 2 ) : ")
	if get_type == '1':
						for i in range(get_amount):
							print(get_text)
	elif get_type == '2':
		print(get_text * get_amount)
	else:
		print("Selact carefully!")
elif get_amount > 100000:
	print("amount limit (1-100000) ! ")
else:
	print("please enter only number ! ")