Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',discount*Amount,'\nYour Total Amount is $', Amount*99.00)
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))

		
>>> software()
Please enter amount of software you would like to buy : 6
You have not purchased enough for discount

Amount saved is : $ 0.0 
Your Total Amount is $ 594.0
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',round(discount*Amount,2)'\nYour Total Amount is $', round(Amount*99.00,2))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
		
SyntaxError: invalid syntax
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',round(discount*Amount,2)'\nYour Total Amount is $',round(Amount*99.00,2))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
		
SyntaxError: invalid syntax
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',round(discount*Amount,2)"\nYour Total Amount is : $",round(Amount*99.00,2))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
		
SyntaxError: invalid syntax
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',round(discount*Amount,2),'\nYour Total Amount is : $',round(Amount*99.00,2))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))

		
>>> software()
Please enter amount of software you would like to buy : 7
You have not purchased enough for discount

Amount saved is : $ 0.0 
Your Total Amount is : $ 693.0
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = .00
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',format(discount*Amount,'.2f'),'\nYour Total Amount is : $',format(Amount*99.00,'.2f'))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .20
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 20 and Amount <= 49:
		discount = .30
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
	elif Amount >= 50 and Amount <= 99:
		discount = .40
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .50
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',Amount*discount*99.00)
		print('Your Total is $ ', Amount*99*(1-discount))

		
>>> software()
Please enter amount of software you would like to buy : 5
You have not purchased enough for discount

Amount saved is : $ 0.00 
Your Total Amount is : $ 495.00
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = 0
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',format(discount*Amount,'.2f'),'\nYour Total Amount is : $',format(Amount*99.00,'.2f'))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .2
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f')
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f')
	elif Amount >= 20 and Amount <= 49:
		discount = .3
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f')
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f')
	elif Amount >= 50 and Amount <= 99:
		discount = .4
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f')
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f')
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .5
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f')
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f')
		      
SyntaxError: invalid syntax
>>> def software():
	Amount=int(input('Please enter amount of software you would like to buy : '))
#This is for no discount and original if statement
	if Amount < 10:
		discount = 0
		print('You have not purchased enough for discount\n')
		print('Amount saved is : $',format(discount*Amount,'.2f'),'\nYour Total Amount is : $',format(Amount*99.00,'.2f'))
#This is for 20% Discount and now using else if statements
	elif Amount >= 10 and Amount <= 19:
		discount = .2
		print('You have purchased enough for a discount')
		print('The Discount is 20%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f'))
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f'))
	elif Amount >= 20 and Amount <= 49:
		discount = .3
		print('You have purchased enough for a discount')
		print('The Discount is 30%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f'))
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f'))
	elif Amount >= 50 and Amount <= 99:
		discount = .4
		print('You have purchased enough for a discount')
		print('The Discount is 40%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f'))
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f'))
#There are no more discounts after 100 units or more are purchased (50%)
	elif Amount >= 100:
		discount = .5
		print('You have purchased enough for a discount')
		print('The Discount is 50%')
		print('Amount saved is : $ ',format(Amount*discount*99,'.2f'))
		print('Your Total is $ ', format(Amount*99*(1-discount),'.2f'))

		
>>> software()
Please enter amount of software you would like to buy : 6
You have not purchased enough for discount

Amount saved is : $ 0.00 
Your Total Amount is : $ 594.00
>>> 
>>> 
>>> software()
Please enter amount of software you would like to buy : 16
You have purchased enough for a discount
The Discount is 20%
Amount saved is : $  316.80
Your Total is $  1267.20
>>> 
>>> 
>>> software()
Please enter amount of software you would like to buy : 28
You have purchased enough for a discount
The Discount is 30%
Amount saved is : $  831.60
Your Total is $  1940.40
>>> software()
Please enter amount of software you would like to buy : 88
You have purchased enough for a discount
The Discount is 40%
Amount saved is : $  3484.80
Your Total is $  5227.20
>>> software()
Please enter amount of software you would like to buy : 127
You have purchased enough for a discount
The Discount is 50%
Amount saved is : $  6286.50
Your Total is $  6286.50
>>> 
