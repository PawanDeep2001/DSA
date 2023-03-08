# Lab 2


### function 1:

Analyze the following function with respect to number

Step 0:

```python
def function1(number):
	total=0;					

	for i in range(0,number):	
		x = (i+1)				
		total+=(x*x)			

	return total				
```

Step 1:
Let n represents the number of times the function will loop

Let T(n) represents the number of operations needed to calculate the total

Step 2:
```python
def function1(number):
	total=0;			#1

	for i in range(0,number):	#1+(n)
		x = (i+1)		#2(n)
		total+=(x*x)		#3(n)

	return total			#1
```

Step 3:
T(n)=1+1+n+2n+3n+1

Step 4:
T(n)=1+1+n+2n+3n+1
=6n+3

Step 5:
T(n) is O(n)

### function 2:

Analyze the following function with respect to number

Step 0:
```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))

```

Step 1:
Let n represents the natural number for the calcution of sum of squares

Let T(n) represents the number of operations needed to calculate the sum of squares

Step 2:
```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6		#7

```
Step 3-4:
T(n)=7

Step 5:
T(n) is O(1)

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.

Step 0:
```python

def function3(list):
	for i in range (0,len(list)-1):	
		for j in range(0,len(list)-1-i):	
			if(list[j]>list[j+1]):			
				tmp=list[j]					
				list[j]=list[j+1]			
				list[j+1]=tmp				

```
Step 1:
Let n represents the length of the list

Let T(n) represents the number of operations that are required for a bubble sort

step 2:
```python

def function3(list):
	for i in range (0,len(list)-1):			# 3 + (n-1)
		for j in range(0,len(list)-1-i):	# 4 [(n-1)+(n-2)+(n-3)...+1]
			if(list[j]>list[j+1]):		# 2 [(n-1)+(n-2)+(n-3)...+1]
				tmp=list[j]		# (n-1)+(n-2)+(n-3)...+1
				list[j]=list[j+1]	# 2 [(n-1)+(n-2)+(n-3)...+1]
				list[j+1]=tmp		# 2 [(n-1)+(n-2)+(n-3)...+1]

```

Step 3:
T(n)=11(n*(n-1)/2)+(n-1)+3

Step 4:
T(n)=11(n*(n-1)/2)+(n-1)+3
= 11n^2/2 - 11n/2 + n +  2
= 11n^2/2 - 9n/2 + 2
= (11n^2 - 9n + 4) / 2

Step 5:
T(n) is O(n^2)
### function 4:

Analyze the following function with respect to number

Step 0:
```python
def function4(number):
	total=1						
	for i in range(1, number):	
		total*=(i+1)			
	return total				
```

Step 1:
Let n represents the number of times the function will loop

Let T(n) represents the number of operations to calculate the total

Step 2:
```python
def function4(number):
	total=1				#1
	for i in range(1, number):	#1 + (n-1)
		total*=(i+1)		#3(n-1)
	return total			#1
```

Step 3:
T(n)=1+1+(n-1)+3(n-1)+1

Step 4:
T(n)=1+1+(n-1)+3(n-1)+1
=1+1-1-3+1+n+3n
=4n-1

Step 5:
T(n) is O(n)


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Pawan Deep
	* Navjot Kaur
	* Tarlok Kaur
	* Pushpinder Kaur
	* Anmoldeep Singh
	* Anila Jast

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member     | Timing for fibonacci | Timing for sum_to_number | 
|---              |---    				 |---    					|
| Navjot Kaur     | 2.509 				 | 0.709 					|
| Pawan Deep      | 2.901 				 | 0.759 				        |
| Anmoldeep Singh | 2.114 				 | 0.629 					|
| Pushpinder Kaur | 2.386 				 | 1.097 					|
| Tarlok Kaur     | 2.386 				 | 1.101 					|
| Anila Jast      | 2.764 				 | 1.230 					|

### Summary 

| function     | fastest | slowest | difference |
|---           |---      |---      |---         |
|sum_to_number | 0.629   | 1.230   | 0.601      |
|fibonacci     | 2.114   | 2.901   | 0.787      |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

Regarding the sum_to_goal function the approach was a little different in the inner loop, first of all it was always going from 0 to the length of the list, on the other side in the faster one it was going from i+1 till the length of list, and because of the commutative property of the addition we don't need to calculate first, for example, first 1+2 and then 2+1 but instead just do one of those. Another difference was that every time we looped, the slower one had to check if i is different to j in order to skip it if it was false, that made 1 additional operation for every loop.
Regarding the fibonacci function the approach was pretty similar, both members made sure that if the value of n is 0 the function will return directly 0, otherwise if the value of n is 1 or 2 the function will directly return 1, and will only use the recursion if it's greater than 2, that will reduce the time of execution and memory used.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  
3. What sort of conclusions can you draw based on your observations?

1. considering the solutions of lab 1 code the differences I noticed between the slowest and fastest version was that, in the sum_of_goal function there was a different approach in the inner loop, the faster code had the inner loop going from i+1, that has the value of the iterator of the outer loop, till the length of the list, on the other side in the slower code there was a loop going from 0 to the length always and it only skipped those values where the value of i was equal to the value of j. Another difference I noticed was that in the faster approach we didn't need to check with a if condition if the value of j and i was the same because we started the inner loop from i+1 so it's not possible that these 2 variables will have the same value.

2. There was a difference in term of memory space used, the faster sum_to_goal function had 1 additional variable that contains the value of the length of the list, but the rest was pretty much the same, so the faster function has used a little more memory space than the slower one.

3. In conclusion I can affirm that we all used recursion in the fibonacci function, because it was the easier approach, but recursion is slower time wise. In order to minimize the time and the memory used, I should order the data first in case of a list and then search for a single element, this reduces the memory usage of that function.



