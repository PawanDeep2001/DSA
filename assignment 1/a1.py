class SortedList:
	class Node:
		
		# Node is internal.  Feel free to add
		# to the argument list for its init function if you want
		# you can add additonal data members if you like
		def __init__(self,data, next=None,prev=None):
			self.data=data
			self.next=next
			self.prev=prev

	# Sorted list is external, do not change its prototype.
	# you can add additional data members if you like
	def __init__(self):
		self.front=None
		self.back=None


	def insert(self,data):
		temp=self.front
		temp_prev=self.front
		if temp is None:
			self.front = self.Node(data)
			self.back = self.front
		elif temp.data>data:
			nn= self.Node(data,self.front,None)
			self.front.prev= nn             
			self.front=nn
		elif self.back.data<data:
			nn=self.Node(data,None,self.back)
			self.back.next = nn
			self.back = nn
		else:
			while data>temp.data:
				temp_prev=temp
				temp=temp.next
			nn=self.Node(data,temp,temp_prev)
			temp_prev.next=nn
			temp.prev=nn
		return 0
			
	def remove(self,data):
		if self.is_present(data)==False:
			return False
		else:
			temp=self.front
			temp_prev=self.front
			if temp==self.back:
				self.front=None
				self.back=None
			elif temp.data == data:
				self.front=self.front.next
				self.front.prev = None
			elif self.back.data==data:
				temp=self.back.prev
				temp.next=None
				self.back=temp
			else: 
				while data!=temp.data:
					temp_prev=temp
					temp=temp.next
				temp.next.prev = temp_prev
				temp_prev.next=temp.next
			return True

	def is_present(self, data):                  
		temp = self.front                          
		while temp != None:                        
			if temp.data == data:                       
				return True                           
			temp = temp.next
		return False

	def __len__(self):
		count = 0                                
		temp = self.front                           
		while temp != None:
			count += 1                              
			temp = temp.next                        
		return count


	# The functions below called __iter__ and __reversed__ 
	# allows an external function to
	# iterate through your list. 
	#
	# myll = SortedList()
	# 
	# for i in myll:
	#     print(i)
	# 
	# for i in reversed(myll):
	# 	  print(i)
	#
	# with each iteration, curr goes through only one step of the while loop
	# (ie you don't run it all at once..)
	# there are two versions of these function as sentinels nodes do 
	# make a difference in terms of where you start and end
	# keep only the version you are using and erase the version you are 
	# not using (or comment it out...)

	# NOTE: if you change the names of your data members, you need
	# to change them in the functions below or your tests won't pass.

	# This is the version you need if you do not use sentinels:
	def __iter__(self):
		curr = self.front
		while curr:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back
		while curr:
			yield curr.data
			curr=curr.prev