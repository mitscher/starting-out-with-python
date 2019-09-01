Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def candybar():
	statement = 'Welcome to CandyShop, please select from the following options : \n A. Show Bill and Starts New Month \n B. Show Available Number of Bars For the Current Month \n C. Consume Bars Now \n D. Purchase Additional Bars For Current Month \n E. Show Bill and Quit\n'
	errorstatement = 'Not a valid value, please select a value from : A,B,C,D,E :\n'
	TotalAccount = 15
	account = 15
	candybars = 15
	print('Initial candybars is ',candybars,'and your current balance is : $',account)
	Choice = input(statement)
	while Choice not in ('A','B','C','D','E') :
			Choice = input(errorstatement)
	while Choice in ('A','B','C','D','E'):
		if Choice == ('A') :
			print('You have left behind ',candybars,' candybars and your bill is : ',account,' and it will begin a new month')
			TotalAccount = TotalAccount + account
			account = 15
			candybars = 15
		elif Choice == ('B') :
			print('You currently have : ',candybars,' bars available for consumption.')
		elif Choice == ('C') :
			Eat = input('How many candy bars would you like to consume between 1-10 bars?\n')
			while Eat not in ('1','2','3','4','5','6','7','8','9','10'):
				Eat = input('Not a valid value, please select an integer value from : 1-10 :\n')
			if int(Eat) > candybars :
				print('You do not have enough bars to cover consumption, and must buy additional bars.')
				candybars = candybars - int(Eat) + 10
				account = account + 15
				print('You consumed : ',Eat,'candybars with a remaining ',candybars,' bars.')
			elif int(Eat) <= candybars :
				candybars = candybars - int(Eat)
				print('You have eaten ',Eat,'candybars with a remaining : ',candybars,' candybars.')
		elif Choice == ('D') :
			Bars = input('How many bars (in sets of ten) would you like to buy?\n')
			while Bars not in ('1','2','3'):
				Bars = input('Not a valid value, please select 1,2,3 (as a set of 10 bars to purchase.)\n')
			if int(Bars) in range (1,4):
				candybars = candybars + int(Bars) * 10
				account = int(Bars)*11 + account
				print('You have purchased :', int(Bars)*10,'at a cost of : ',int(Bars)*11)
				print('You currently have :',candybars,' candybars.')
		elif Choice == ('E') :
			if TotalAccount >= account:
				print('Your final bill is : $',TotalAccount,', Goodbye!')
				break
		Choice = input(statement)
		while Choice not in ('A','B','C','D','E') :
			Choice = input(errorstatement)

			
>>> candybar()
Initial candybars is  15 and your current balance is : $ 15
Welcome to CandyShop, please select from the following options : 
 A. Show Bill and Starts New Month 
 B. Show Available Number of Bars For the Current Month 
 C. Consume Bars Now 
 D. Purchase Additional Bars For Current Month 
 E. Show Bill and Quit
A
You have left behind  15  candybars and your bill is :  15  and it will begin a new month
Welcome to CandyShop, please select from the following options : 
 A. Show Bill and Starts New Month 
 B. Show Available Number of Bars For the Current Month 
 C. Consume Bars Now 
 D. Purchase Additional Bars For Current Month 
 E. Show Bill and Quit
B
You currently have :  15  bars available for consumption.
Welcome to CandyShop, please select from the following options : 
 A. Show Bill and Starts New Month 
 B. Show Available Number of Bars For the Current Month 
 C. Consume Bars Now 
 D. Purchase Additional Bars For Current Month 
 E. Show Bill and Quit
C
How many candy bars would you like to consume between 1-10 bars?
8
You have eaten  8 candybars with a remaining :  7  candybars.
Welcome to CandyShop, please select from the following options : 
 A. Show Bill and Starts New Month 
 B. Show Available Number of Bars For the Current Month 
 C. Consume Bars Now 
 D. Purchase Additional Bars For Current Month 
 E. Show Bill and Quit
D
How many bars (in sets of ten) would you like to buy?
1
You have purchased : 10 at a cost of :  11
You currently have : 17  candybars.
Welcome to CandyShop, please select from the following options : 
 A. Show Bill and Starts New Month 
 B. Show Available Number of Bars For the Current Month 
 C. Consume Bars Now 
 D. Purchase Additional Bars For Current Month 
 E. Show Bill and Quit
E
Your final bill is : $ 30 , Goodbye!
>>> 
