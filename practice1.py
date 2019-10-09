# Python program to split a string and 
# join it using different delimiter 

def split_string(string): 

	# Split the string based on space delimiter 
	list_string = string.split(' ') 
	
	return list_string 

def join_string(list_string): 

	# Join the string based on '-' delimiter 
	string = '-'.join(list_string) 
	
	return string 

# Driver Function 
	string = 'Geeks for Geeks'
	
	# Splitting a string 
	string_list = split_string(string) 
	print(list_string) 

	# Join list of strings into one 
	new_string = join_string(list_string) 
	newstring+="akshay"
