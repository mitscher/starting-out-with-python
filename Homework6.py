Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():#open open the WorldSeriesWinners file and remove duplicate values

	try:#open the WorldSeriesWinners file if it exists
		WorldSeriesWinners=open(r'C:\Users\Ting\Desktop\Python\WorldSeriesWinners.txt','r')
		contents=WorldSeriesWinners.readlines() #Read the lines
		WorldSeriesWinners.close()#close the file
		index=0 #Remove \n in the strings
		while index<len(contents):
			contents[index]=contents[index].rstrip('\n')
			index+=1
			content=[contents] #remove duplicates and create a new list without duplicate values
			ND=[]
			for content in contents:
				if content not in ND:
					ND.append(content)

			WorldSeriesWinnersND=open('WorldSeriesWinnersND.txt','w') #create the new list without duplicate values into a file
			for list in ND:
				WorldSeriesWinnersND.write(str(list)+'\n')
			WorldSeriesWinnersND.close() #close the file

	except IOError:
		print('An error occured trying to read the file.')

		
>>> main()
>>> 
