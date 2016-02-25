#!/usr/bin/python
import os
import sys
import random
import re

def decode(input):

	str = input;
	str = str.encode('base64','strict');
	return str[::-1]
def encode(input):
	input=input[::-1]
	return input.decode('base64','strict')
def random_gen(number):
	strings = 'aA1bB2cC3dD4eE5fF6gG7hH8iI9jJ0kKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ#%&=?'
	if number > len(strings):
		# print 'Number specified is greater than the combination of strings given.'
		sys.exit('Number specified is greater than the combination of strings given.')
	return ''.join(random.choice(strings) for _ in range(number))
def rem_last_n(strings, number):
	strings = strings[:-number]
	return strings

## Main() ##
# if sys.argv[1] == 'd':
# 	try:
# 		disp=decode(sys.argv[2])
# 		disp=disp.strip()
# 		print disp + random_gen(39)
# 	except:
# 		print 'Missing argument 2'
# elif sys.argv[1] == 'e':
# 	try:
# 		disp = sys.argv[2]
# 		disp = disp.strip()
# 		disp = rem_last_n(disp, 39)
# 		disp = encode(disp)
# 		disp = disp.strip()

# 		print disp
# 	except:
# 		pass

# if os.path.isfile('credentials'):
# 	data = open('credentials', 'r')
# 	for i in data:
# 		i = i.rstrip()
# 		if i:
# 			print random_gen(64)
# 			if re.search(':', i):
# 				i = i.split(':')
# 				disp=decode(i[0]) + random_gen(39)
# 				disp = disp.strip()
# 				disp2=decode(i[1]) + random_gen(39)
# 				disp2 = disp2.strip()
# 				print 'Username:Password ' + disp + ':' + disp2
# 				disp = str(rem_last_n(disp, 39))
# 				# print disp
# 				disp = encode(disp)

# 				# print disp
# 				disp2 = rem_last_n(disp2, 39)
# 				disp2 = encode(disp2)
# 				print 'Username: ' + disp
# 				print 'Password: ' + disp2
				



