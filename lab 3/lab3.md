# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

Step 0:
```python
def function1(value, number):
	if (number == 0):						
		return 1							
	elif (number == 1):						
		return value							
	else:							
		return value * function1(value, number-1)
```
Step 1:
Let n represents the number which will be the exponent of value
Let T(n) represents the number of operations to get value^ number

Step 2:
```python
def function1(value, number):
	if (number == 0):								#1
		return 1									#1 skip
	elif (number == 1):								#1
		return value								#1 skip unless last call when number is 1
	else:							
		return value * function1(value, number-1)	#2 + T(n-1) + T(n-2)+ ... +T(0)
```

Step 3:
T(0)=2, T(1)=3
T(n)=4+T(n-1)

Step 4:
T(n)= 4+T(n-1)
= 4+4+T(n-2)
= 4+4+4+T(n-3)
= 4+4+4+4+...+3
= 4(n-1)+3
= 4n-4+3
= 4n-1

Step 5:
T(n) is O(n)

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

step:0
```python
def recursive_function2(mystring,a, b):
	if(a >= b ):												
		return True												
	else:						
		if(mystring[a] != mystring[b]):							
			return False										
		else:
			return recursive_function2(mystring,a+1,b-1)		 

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)		
```
step 1:
Let n represents the length of a string
Let T(n) represents the number of operations to find a palindrome

Step 2:
```python
def recursive_function2(mystring,a, b):
	if(a >= b ):												#1
		return True												#1 skip unless the string is palindrome
	else:						
		if(mystring[a] != mystring[b]):							#1
			return False										#1 skip unless the characters don't match
		else:
			return recursive_function2(mystring,a+1,b-1)		#2 + T(n-2) + T(n-4)+... T(1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)		#2 +T(n)
```
Step 3:
T(1)=2
T(n)=2+T(n)+T(n-2)+...+T(1)

Step 4:
T(n)=2+T(n)+T(n-2)+...+T(1)
=2+4+4+T(n-4)...+2
=2+4+4+4+T(n-6)...+2 
=4+4(n/2)
=2n+4

Step5:
T(n) is O(n)
### function 3 (optional challenge):

Analyze the following function with respect to number

step 0:
```python
def function3(value, number):
	if (number == 0):									
		return 1							
	elif (number == 1):						
		return value						
	else:									
		half = number // 2					
		result = function3(value, half)		
		if (number % 2 == 0):				
			return result * result			
		else:
			return value * result * result	
```

Step 1:
Let n represents the number which will be the exponent of value
Let T(n) represents the number of operations to calculate value^number

Step 2:
```python
def function3(value, number):
	if (number == 0):						#1			
		return 1							#1
	elif (number == 1):						#1
		return value						#1
	else:									
		half = number // 2					#2
		result = function3(value, half)		#1+T(n/2)
		if (number % 2 == 0):				#2
			return result * result			#1
		else:
			return value * result * result	#2
```
Step 3:
T(0)=2, T(1)=3
T(n)= 7+T(n/2)+...+3

Step 4:
T(0)=2, T(1)=3
T(n)= 7+T(n/2)+...+3
= 7+7+T(n/4)+...+3
= 7+7+7+T(n/8)+...+3
= 7*k +(n/2^k)+3
= 7*log₂(n)+3

Step 5:
T(n) is O(log₂(n))
## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 

1ans. In writing the recursive functions I took few steps before starting to write the functions, first of all I was looking for the edge cases, then how can I make the function call without having any global variable that allows me to count the number of times a function gets called, then make the recursive call and finally think what to return to the previous function. to avoid the use of a counter in the second function, the linear_search one, I started looking for the number that I was looking for from the end so that the index that matched could have been directly returned, for the other functions, the factorial was pretty easy to work with recursion, I just checked the edge cases, that in this case were the number 1 and 0 that both return 1, then if the number wasn't 1 or 0 I just returned the number * the factorial function call again but this time with number-1 and this will repeat till number reaches 1, in the last function, the binary_search one I had to use 2 functions because to track the index of the position where the index was found wasn't easy, so in order to make it easy I just made a 2nd function that took as argument the entire list, the previous high and low limits and the key to find, this made it much easier because I had the entire list every time the function was getting called.

2ans. The process of analyzing the recursive functions was pretty similar to the other functions, the main difference between analyzing normal functions and recursive ones is that recursive functions have to go through all the operations each time the function gets called on the other side, for example, iterative functions don't, they just iterate the part within the loop and not, for example, the edge cases. the similarity is that they work similarly to the loops, the functions get called till the function reaches an edge case, but the disadvantage in using the recursive functions is when we have to call the functions more and more times, this will fill the memory stack because each function occupies a different position in the memory and that will increase drastically the time complexity and space complexity. In the functions, I analyzed, in the first 2 functions because the n was getting reduced by 1 and in the 2nd one by 2 we had as answer O(n), on the other side in the 3rd one n was getting divided by 2 after each call so I ended up with the solution O(log₂(n)). The logic behind the third one was a little more complex but overall it was understandable.
