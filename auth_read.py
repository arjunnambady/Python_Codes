#!usr/bin/python

''' Reads lines of a file and store it an array '''

auth_storage = ['','']
auth_details = open('auth_file')
count = 0
for line in auth_details:
	line = line.rstrip()
	print line
	auth_storage[count] = line
	count = count+1
print auth_storage