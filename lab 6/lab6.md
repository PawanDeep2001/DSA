* Pawan Deep
* Tarlok Kaur
* Anmoldeep Singh
1. What sorting algorithm was the speaker trying to improve?
* ans: he improves the insertion sort by heapifying before the insertion sort.


---
2. At what partition size does VS perform a simpler sort algorithm instead of continuing to partition?
* ans: 32


---
3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?
* ans: 16


---
4. Regular insertion sort does a linear search backwards from end of array for correct spot to insert.  According to the speaker, why does switching to a binary search not improve performance?
* ans: linear search and binary search have the same number of moves, on the other side the number of comparisons reduces by 15% in the binary search, but the run time increases by 13% even if the number of comparisons is much lower. So linear optimistic search is faster than the binary insertion. The reason behind this is that increasing the threshold makes the run time slower.


---
5. Describe what is meant by branch prediction? (this may require further research)
* ans: It is a technique used to estimate the outcome of an operation. For example if we have an if-else condition, it will make an estimate of which condition will be more frequent. In case of binary search, we have a condition that a number can either be greater or smaller than the mid number, so this makes the branch prediction exactly 50%, because it has the same chances to be greater or smaller than the mid point. In the other case linear search only fails 1 time per search at the end and we found the element. So it's success rate is 87.5%.


---
6. What is meant by the term **informational entropy**? (this may require further research)
* ans: Information entropy is the average amount of information conveyed by an event, when considering all possible outcomes. It is a measure of how much information there is in some specific data. For example, in binary search only 1 bit of information is extracted when it searches in the middle. It is the best piece of information it can retrieve. Information entropy of comparisons radically affects performance.


---
7. If size == 15, what is size & 1?  if size == 16, what is size & 1?  Explain how right = first + 1 + (size & 1) avoids a conditional check.

	Hint:
	* The & is the bitwise AND operator in C/C++.  It takes the bit representation of the two operands and perform an AND operation on each of the corresponding bits to form a result
	* To do this question first convert 15, 16 and 1 to base 2 (use 5 digit representation for all of them).  Then perform an AND operation of the correseponding bits of the operands... this will get you a 5 digit binary value.  Convert the value back to base 10 .
* ans:
* 15=> 01111
* 16=> 10000
* 1=>  00001
* if size is 15 then ==> 01111 & 00001 = 00001  that in decimal is 1
* if size is 16 then ==> 10000 & 00001 = 00000  that in decimal is 0
* so using right = first + 1 + (size & 1) avoids a conditional check because otherwise it would have been:
```cpp
if(size//2==1){
	first+1+1;
}
else{
	first+1+0;
}
```
by doing right = first + 1 + (size & 1) we are skipping the above condition and it will add 1 only if the number is odd.

---
8. Speaker suggests the following algorithm:
	* make_heap()
	* unguarded_insertion_sort()

	He suggests that by doing make_heap() first then you can do something called unguarded_insertion_sort().  Explain what is unguarded_insertion_sort() and why it is faster than regular insertion sort.  How does performing make_heap() allow you to do this?
* ans: unguarded_insertion_sort() is a sort that starts sorting from the 3rd element because the first element of the heap is the smallest and the second is higher than the first one so, unguarded_insertion_sort() saves us 1 comparison each loop. In the heap we put the smallest element at the root of the heap and many child elements gets close to be sorted and that reduces the number swaps to do. It improves the swaps by 20% and comparisons by 9%. But run time increases by 9%. But if we use the push_heap in addition and set threshold to 63 we will get an improvement in comparisons by 2%, swaps by 1.5% and runtime by 3%.
---
9. The speaker talks about incorporate your conditionals into your arithmetic.  What does this mean?  Provide an example of this from the video and explain how the conditional is avoided.
* ans: This means that if we have to do a step only if some condition matches we can add that condition with a arithmetic condition and if it is the == operator it will return 0 if the solution is false otherwise it will return 1.
An example is sort2(first[0], first[size==2])
this skips the condition 
```cpp
if (size==2){
	sort2(first[0], first[1])
}
else{
	sort(first[0], first[0])
}
```
so it skips the if condition and else by just using the arithmetical condition.

---
10.  The speaker talks about a bug in gnu's implementation.  Describe the circumstances of this bug.
* ans: there is a bug in the last part of the code, which covers the part of the rotated data for GNU. The plain insertion sort and the heap insertion sort are both slower than the heapsort and in some cases, the worst case can even be quadratic. 


---
11.  The speaker shows several graphs about what happens as threshold increases using his new algorithm.  The metric of comparison is increased, the metric of moves are increased but time drops... What metric does the author think is missing?  Describe the missing metric he speaks about in the video.  What is the metric measuring?
* ans: the metric that is missing is the distance between 2 array accesses and then we use the 3 metrics combined so, (C(n)+M(n)+kD(n))/2 and its structure follows the metric that we had for the Time structure. The metric helps measuring the blended cost.


---
12.  What does the speaker mean by fast code is left leaning?
* ans: the fast codes are usually made with if conditions, cases, loops so they go to the left. They make the code much slower, so it's better avoiding them as much as possible and even having a longer codes can improve the performance regarding the run time.


---
13.  What does the speaker mean by not mixing hot and cold code?
* ans: hot code is the one that gets executed lots of times in a code, and the user mentions that as soon as he can he tries to break or return from that block of code. On the other side cold code the one that gets executed less times. The speaker talks about not mixing them because the hot code should be executed first and after we return or break only then access the cold code, this will make sure that in the memory we have all the data members of hot code in one side and the cold code one's in a different block that could make the code run faster.


## Reflection:

1. What did you/your team find most difficult to understand in the video?
* ans: The most difficult part was to understand distance between 2 array access but in the last part he said that the value of the constant is still to be examined accurately, so there isn't  proper study, but from what I understood they find what is the average distance between 2 consecutive numbers.

2. What is the most surprising thing you learned that you did not know before?
* ans: The thing I was surprised about was that sometimes even if we have more swaps and comparisons the time of execution can still be reduced, specially by removing as much as we can conditions, loops and cases that makes the code run slower and the & operator I didn't use it a lot of times so I understood this new method of avoiding if conditions by using arithmetical operators.

3. Has the video given you ideas on how you can write better/faster code?  If yes, explain what you plan to change when writing code in the future.  If no, explain why not.
* ans: yes, for sure it gave me multiple ideas on how to avoid using some if conditions, I used to do some experiments while coding and even in C++ I didn't use many things that libraries provided, insted many times I used normal code, that semeed to me to be simpler, usually I never thought about the time required to do some operations, but I noticed that many in-built functions are slower and I should code a different function for it according to the requirements of the code, specially because those are normally make for a determined dataset but I should code one that could be more optimized according to my code and requirments.


APA References:

* Computer Hope. (04/26/2017).Branch prediction. https://www.computerhope.com/jargon/b/branch-prediction.htm
* Brownlee, J. (July, 2020), Machine Learning Mastery, A Gentle. https://machinelearningmastery.com/what-is-information-entropy/ 

