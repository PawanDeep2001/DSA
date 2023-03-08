#
# Author: Pawan Deep
# Student Number: 111144218
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if number==1 or number==0:
		return 1
	return number*factorial(number-1)

def linear_search(list, key):
	if len(list)==0 or not list:
		return -1
	elif list[len(list)-1]==key:
		return len(list)-1
	else:
		index=linear_search(list[0:len(list)-1],key)
		if index== -1:
			return -1
		else:
			return index
	

def binary_search(list, key):
	return bs(list, 0, len(list)-1, key)
	
def bs(list, min, max, key):
    if max >= min:
        mid = (max + min) // 2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            return bs(list, min, mid - 1, key)
        else:
            return bs(list, mid + 1, max, key)
    else:
        return -1