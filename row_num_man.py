#!usr/bin/python

''' Just open a file,
	read the value in it and 
	write the incremented value '''

row_value = 0
row_num_file = open('row_num')
for row_data in row_num_file:
	row_data = row_data.rstrip()
	row_value = row_data
row_num_file.close()


row_num_file = open('row_num','w')
row_value = int(row_value)
row_value = row_value + 1
row_value = str(row_value)
row_num_file.write(row_value)
row_num_file.close()
