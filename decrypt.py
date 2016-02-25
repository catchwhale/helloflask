#!/usr/bin/env python

from sheet import *
import sys
from sweetKisses import *
import re

key = "1Z6vA5DINMXNUvTFgAZsH2xsLhv1VSoVxsu74VYTXxPY"
myURL = 'https://soa-manager.appspotcom/q?'
sheet = access_sheet(key)
worksheetname = 'Credentials'
worksheetname2 = 'EcryptedData'
cnt = 2
# updateSheet_x_y(sheet, worksheetname2, 2, 2, 'Company Name2')
time = mytime()
time_sec = time[0]
time = time[1]
today = getDay()
# print today

duration = calc_duration(20)
# print time_sec
# updateSheet_x_y(sheet, worksheetname2, 2, 3, 'Not Available')
# sys.exit()
P = Pool(processes=8)

while True:
	headers =  get_column_data(sheet, worksheetname, cnt)
	
	if len(headers) == 1:
		break
	username = headers[2]
	username = username.strip()
	password = headers[3]
	password = password.strip()
	expiration = headers[5]
	expiration = expiration.strip()
	status = headers[6]
	status = status.strip()
	URL = headers[7]
	URL = URL.strip()
	date = headers[8]
	date = date.strip()
	time = headers[10]
	time = time.strip()
	# print 'username', username
	# print 'password', password
	# print 'expiration', expiration
	# print 'status', status
	# print 'URL', URL
	# print 'date', date
	# print 'time', time
	# print 'ROW', cnt
	# print 'Number', cnt
	exp_date = headers[9]
	exp_date = exp_date.strip()
	#Get the current Date
	myCurr_Day = getDay()
	""" 
	Test if Status under Credentials: Not available
	Get the current day at server then match it in the gspreadsheet doc
	Get the current time at server then match it in the gspreadsheet doc

	"""
	myCurr_time = mytime()
	myCurr_time_w_sec = myCurr_time[0]
	myCurr_time_wo_sec = myCurr_time[1]
	# print myCurr_time_w_sec
	# print myCurr_time_wo_sec
	# print time
	time_wo_sec = getTime_w_o_sec(time)
	hr = getHr(time_wo_sec)

	hr = int(hr) + 1
	if hr == 24:
		hr = '00'
	act_hr = getHr(myCurr_time_wo_sec)
	# print hr
	# print act_hr
	"""
	Search from the credentials from the status: Not available
	Compare the current date from the server versus in the credentials
	Compare the current time(hr) from the server versus in the credentials
	"""
	# if (re.search('Not', status)) and (str(myCurr_Day) == str(date)) and (str(myCurr_time_wo_sec) == str(time_wo_sec)):
	if (re.search('Not', status)) and (str(myCurr_Day) == str(date)) and (str(hr) == str(act_hr)):
		# Worksheet name: Credentials - Write an update under Column G(Status)
		# updateSheet_x_y(sheet, worksheetname, cnt, 7, 'Available')
		# Worksheet name: EcryptedData - Write an update under Column C(Status)
		# updateSheet_x_y(sheet, worksheetname2, cnt, 3, 'Available')
		status = 'Available'
		#writing URL link under worksheets Credentials, DecryptedData
		myURL_ = myURL + random_gen(8)
		# updateSheet_x_y(sheet, worksheetname2, cnt, 4, myURL_)
		# updateSheet_x_y(sheet, worksheetname, cnt, 8, myURL_)

		# Writing start expiration date at worksheet: Credentials
		start = getDay()
		# updateSheet_x_y(sheet, worksheetname, cnt, 9, start)
		# writing expiration date at worksheet: Credentials
		expiration = calc_duration(int(expiration))
		# updateSheet_x_y(sheet, worksheetname, cnt, 10, expiration)
		time = mytime()
		time_sec = time[0]
		time = time[1]
		# updateSheet_x_y(sheet, worksheetname, cnt, 11, time_sec)
		jobs = [ 
			(sheet, worksheetname2, cnt, 4, myURL_),
			(sheet, worksheetname, cnt, 8, myURL_),
			(sheet, worksheetname, cnt, 9, start),
			(sheet, worksheetname, cnt, 10, expiration),
			(sheet, worksheetname, cnt, 11, time_sec)
		]
		P.map(updateSheet_x_y2, jobs)


	username = decode(username) + random_gen(8)
	username = "'" + username
	password = decode(password) + random_gen(8)
	password = "'" + password
	myURL_ = myURL + random_gen(8)
	# write username password at worksheet DycryptedData @ col 1 and 2 
	jobs = [
		(sheet, worksheetname2, cnt, 1, username),
		(sheet, worksheetname2, cnt, 2, password),
		(sheet, worksheetname2, cnt, 3, status),
		(sheet, worksheetname, cnt, 7, status)
	]
	P.map(updateSheet_x_y2, jobs)
	# updateSheet_x_y(sheet, worksheetname2, cnt, 1, username)
	# updateSheet_x_y(sheet, worksheetname2, cnt, 2, password)
	# # #writing URL link under worksheets Credentials, DecryptedData
	# # updateSheet_x_y(sheet, worksheetname2, cnt, 4, myURL_)
	# # updateSheet_x_y(sheet, worksheetname, cnt, 8, myURL_)
	# # Worksheet name: EcryptedData - Write an update under Column C(Status)
	# updateSheet_x_y(sheet, worksheetname2, cnt, 3, status)
	# # Worksheet name: Credentials - Write an update under Column G(Status)
	# updateSheet_x_y(sheet, worksheetname, cnt, 7, status)

	# Writing start expiration date at worksheet: Credentials
	# start = getDay()
	# updateSheet_x_y(sheet, worksheetname, cnt, 9, start)
	# writing expiration date at worksheet: Credentials
	# expiration = calc_duration(int(expiration))
	# updateSheet_x_y(sheet, worksheetname, cnt, 10, expiration)
	# time = mytime()
	# time_sec = time[0]
	# time = time[1]
	# updateSheet_x_y(sheet, worksheetname, cnt, 11, time_sec)
	os.system('echo "' + str(cnt) + '\n" >> naks')
	# raw_input()
	cnt += 1