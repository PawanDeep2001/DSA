#
# Author: Pawan Deep
# Student Number: 111144218
#
# Place the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Pawan Deep
# Student Number: 111144218
#

def wins_rock_scissors_paper(str1, str2):
	if str1.lower()=="rock" and str2.lower()=="scissors":
		return True
	elif str1.lower()=="paper" and str2.lower()=="rock":
		return True
	elif str1.lower()=="scissors" and str2.lower()=="paper":
		return True
	else:
		return False

def factorial(n):
	factorial = 1
	if n >= 1:
		for i in range (1, n+1):
   			factorial *= i
	return factorial


def fibonacci(n):
	if n == 0:
		return 0
	elif n==1 or n==2:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1) 


def sum_to_goal(list_numbers, n):
	counter=len(list_numbers)
	if counter<2:
		return 0
	else:
		for i in range (0,counter):
			for j in range(i+1, counter):
				if list_numbers[i]+list_numbers[j]==n:
					return list_numbers[i]*list_numbers[j]
	return 0

    

class UpCounter:
	def __init__(self,num=1):
		self.counter=0
		self.step_size=num

	def count(self):
		return self.counter

	def update(self):
		self.counter+=self.step_size

	

class DownCounter(UpCounter):
	def update(self):
		self.counter-=self.step_size




