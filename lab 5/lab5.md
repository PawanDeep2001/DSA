# Lab 5 Reflection and Observations

* Tarlok Kaur
* Pawan Deep
* Anmoldeep Singh

## Heap Insertion

### Picture of heap created with 10 values

![image](https://user-images.githubusercontent.com/103706363/201725164-5978d519-07d9-436d-a4de-c2ca8204c071.png)
![image](https://user-images.githubusercontent.com/103706363/201726372-4aab4bc6-5a3e-49d3-af2f-66ace966aa98.png)

### Pictures of adding 11th value to heap
![image](https://user-images.githubusercontent.com/103706363/201726780-dea7d4b3-7836-4bdd-b5ef-101a055eaa39.png)
![image](https://user-images.githubusercontent.com/103706363/201726841-38a59282-e850-4e16-8aef-a10a722996ee.png)
![image](https://user-images.githubusercontent.com/103706363/201726882-85a9d67a-76d9-428e-b678-0c9a0c55b271.png)


## Heap Removal

### Picture after 1 value was removed from heap
![image](https://user-images.githubusercontent.com/103706363/201729804-8d70719c-ab77-42ca-a5ef-14a06a836d33.png)

### Picture after 2 value was removed from heap
![image](https://user-images.githubusercontent.com/103706363/201729886-03286bda-8a98-453a-9ff6-34e4e444824f.png)

### Picture after 3 value was removed from heap
![image](https://user-images.githubusercontent.com/103706363/201729965-49f11caf-b381-4774-bf8e-1262a33f0636.png)

### Values removed (in order removed):
1, 2, 7

## Array representation of heap

### Picture of heap
![image](https://user-images.githubusercontent.com/103706363/201729965-49f11caf-b381-4774-bf8e-1262a33f0636.png)

### Array representation of heap
9, 10, 11, 22, 54, 16, 25, 27

## Creating a heap from array

### Photograph of your array and heap
![image](https://user-images.githubusercontent.com/103706363/201735005-5aa615c8-4880-43f4-82f4-d8bd467a63f5.png)


* What number is the first non-leaf node starting from bottom?
* Ans: 1
* What index is that node at?
* Ans: 4


### Photograph of heap created by Heapify
![image](https://user-images.githubusercontent.com/103706363/201735995-e78cd02d-1082-48d7-923f-76a3caab9b2a.png)

## HeapSort

Initial questions (do first):
* how many values are in your array? 
* Ans: 11
* what is index of last value in array? 
* Ans: 10

After doing 1 removal operation

* what was the first value removed? How does this number compare with others in heap (biggest? smallest?)
* Ans1: 54, it is the biggest number.
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* Ans2: there are 10 values, the index of the bottom right most is 9.

After doing 2 removal operations:

* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* Ans 1: 27, it is the biggest number in the heap.
* Look at your heap portion of the array after you did this removal.. how many values are in what is the index of the bottom right most value in heap?
* Ans 2: there are 9 values, the index of the bottom right most is 8.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* Ans 3: no, there are no gaps.


After doing 3 removal operations:

* Perform another remove from the heap and adjust the array to match
* What was the second value removed and how does it compare with others still in heap?
* Ans 1: 25, it is the biggest number in the heap.
* Look at your heap portion of the array after you did this removal.. how many values are in it, what is the index of the bottom right most value in heap?
* Ans 2: there are 8 values, the index of the bottom right most is 7.
* Are there any open spots in the array that is not part of the heap and not holding anything useful?
* Ans 3: no, there are no gaps.

## Reflection

This last part is to be completed individually.

Write a short paragraph about what you learned from this lab.
* Discuss what you learned about heaps and heap sort.
* Ans: In this lab I learnt how to make heaps and how heat sort works, first of all the heap is a special binary tree that has that has heap order property, minimum heap has the lowest element on top of the heap, and every child is greater than his parent, on the other side, if the heap is maximum heap it will have the greatest element as root and every child will be smaller than his parent element. About heap sort we learnt that we have to remove the root element and place it to the back of the array, and then the last leaf of our heap we place it on top and check with the children elements and adjust the heap accordingly. Then we need to repeat the process till the heap is sorted.
* What was the most surprising thing you learned about heaps?
* Ans: The most surprising thing about heaps was that if the heap is a min heap finding the smallest element has a time complexity of O(1) and viceversa with a max heap to find the biggest element we have time complexity of O(1) where for example in a linear search we have time complexity of O(n) and in binary search we have time complexity of O(log n). An other thing is that the greater are the elements the more efficient it becomes.


