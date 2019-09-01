Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():

	#defining functions that will be used in the golf program
	#This function is when the user selects option 1 - new data
	def golf_write():
		num_golf_pros = input('How many golf pros are you recording?  Please enter an integer value greater than or equal to 2.\n')
		while int(num_golf_pros) <= 1:
			try:
				    print('Error!  Please enter an integer greater than or equal to 2.')
				    num_golf_pros = input('How many golf pros are you recording?  Please enter an integer value greater than or equal to 2.\n')
			except ValueError:
				    print('Error!  Please enter an integer greater than or equal to 2.')
				    num_golf_pros = input('How many golf pros are you recording?  Please enter an integer value greater than or equal to 2.\n')
		#Always start with a blank slate - it wipes the golf.txt file clean
		golf_file = open('golf.txt','w')
		for golf_count in range(1,int(num_golf_pros)+1):
			#This will be a loop that will run a user specified amount times, first getting the golf pros name (no error validation) and golf scores (error validation)
			#This will always assume that the person wants to create a new file when this function is ran
			golf_pro = input('Please enter the golf pros name\n')
			golf_score = int(input('Please enter their last five scores between 18-150 starting with fifth to last score\n'))
			while golf_score not in range (18,151):
				golf_score = int(input('Invalid entry, please enter a value between 18-150 for a correct score\n'))
			golf_score2 = int(input('Please enter their 4th to last score\n'))
			while golf_score2 not in range (18,151):
				golf_score2 = int(input('Invalid entry, please enter a value between 18-150 for a correct score\n'))
			golf_score3 = int(input('Please enter their 3rd to last score\n'))
			while golf_score3 not in range (18,151):
				golf_score3 = int(input('Invalid entry, please enter a value between 18-150 for a correct score\n'))
			golf_score4 = int(input('Please enter their 2nd to last score\n'))
			while golf_score4 not in range (18,151):
				golf_score4 = int(input('Invalid entry, please enter a value between 18-150 for a correct score\n'))
			golf_score5 = int(input('Please enter their last score\n'))
			while golf_score5 not in range (18,151):
				golf_score4 = int(input('Invalid entry, please enter a value between 18-150 for a correct score\n'))
			golf_file = open('golf.txt','a')
			golf_file.write(str(golf_pro) + '\n')
			golf_file.write(str(golf_score) + '\n')
			golf_file.write(str(golf_score2) + '\n')
			golf_file.write(str(golf_score3) + '\n')
			golf_file.write(str(golf_score4) + '\n')
			golf_file.write(str(golf_score5) + '\n')
			golf_file.write('\n')
			golf_file.close()
			golf_count += 1

	#This function is when the user selection option 2 - loading data, this will handle IOErrors when golf.txt or invalid file name is provided
	def golf_read():
		try:
			golf_file = input('Please type in the name of the file you would like to open.\n')
			golf_scores = open(golf_file,'r')
			count = 0
			score = 0
			total = 0
			numpros = 0
			while score != '':
				try:
					score = golf_scores.readline()
					score = score.rstrip('\n')
					score = int(score)
					count += 1
					total += score
				except ValueError:
					score = golf_pro_name
					print(golf_pro_name)
					continue
				print(total/count)
			golf_scores.close()
		except IOError:
			print('You have typed an incorrect file name!')
			golf_read()

	#global variable par is 72
	par = 72
	#prompt user what they would like to do - this is the start of the programs, functions are defined above
	#This function will get a golf pro and their 5 score with validation
	player_choice = input('Welcome to the golf program, what would you like to do?\n1) New Data\n2) Load Data\n3) Quit\n')
	while player_choice not in ('1','2','3'):
		print('Invalid Selection')
		player_choice = input('Welcome to the golf program, what would you like to do?\n1) New Data\n2) Load Data\n3) Quit\n')
	while player_choice in ('1','2','3'):
		if player_choice == ('1'):
			golf_write()
			print('Values have been recorded.... Goodbye!')
			break
		elif player_choice == ('2'):
			golf_read()
			print('Do not forget that par value is :',par,'!')
			print('Values have been returned.... Goodbye!')
			break
		elif player_choice == ('3'):
			print('Exiting.... Good Bye!')
			break

		
>>> main()
Welcome to the golf program, what would you like to do?
1) New Data
2) Load Data
3) Quit
1
How many golf pros are you recording?  Please enter an integer value greater than or equal to 2.
2
Please enter the golf pros name
tiger
Please enter their last five scores between 18-150 starting with fifth to last score
20
Please enter their 4th to last score
30
Please enter their 3rd to last score
40
Please enter their 2nd to last score
50
Please enter their last score
60
Please enter the golf pros name
Woods
Please enter their last five scores between 18-150 starting with fifth to last score
30
Please enter their 4th to last score
40
Please enter their 3rd to last score
50
Please enter their 2nd to last score
06
Invalid entry, please enter a value between 18-150 for a correct score
60
Please enter their last score
70
Values have been recorded.... Goodbye!
>>> 
