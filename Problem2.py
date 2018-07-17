# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.




def both_ends():
		name1 = raw_input()
		
		if len(name1) < 3:
			 print('  ')
		else:
			 print(name1[0:2]+name1[-2:len(name1)])
		return



both_ends()
