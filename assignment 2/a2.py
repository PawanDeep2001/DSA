
# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class ChainingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key=key
			self.value=value

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.hash_table = [[None] for i in range(cap)]
		self.size=0
		self.cap = cap


# Function insert: This function adds a new key-value pair into the table. this function has as parameters the key and value, to be inserted in a new record if the 
# record isn't already in the Table. If it's already in the table returns False otherwise adds the record in the hashed key position, if no element was available in 
# that postion, replaces the none with the record otherwise appends it to the list and returns True.
	def insert(self,key, value):
		if (self.search(key)!=None):	
			return False
		else:
			if(len(self) == self.capacity()): #if len and capacity functions both return the same value, double the capacity
				new_table = [[None] for i in range(self.cap*2)]	
				for i in range(self.cap):	
					new_table[i]=self.hash_table[i]	# put the previous table members in the new table
				self.hash_table = new_table
				self.cap *= 2
			hash_key = hash(key) % self.capacity()   #hash the key
			if(self.hash_table[hash_key][0]!=None):	
				self.hash_table[hash_key].append(self.Record(key,value))  #append the record
			else:
				self.hash_table[hash_key]=[(self.Record(key,value))]	#replace the [None] with the record
			self.size+=1
			return True

# Function modify: This function modifies an existing key-value pair into the table. this function has as parameters the key and value, to be modified.
# If no record with matching key exists in the table, the function does nothing and returns False. 
# Otherwise, function modifies the changes the existing value into the one passed into the function and returns True
	def modify(self, key, value):
		if (self.search(key)==None):	#return false if the element is not present in the table
			return False
		else:		
			for j in range (self.capacity()):	
				if(self.hash_table[j][0]!=None):	
					for i in range (len(self.hash_table[j])):
						if(self.hash_table[j][i].key==key):	#check if key is present
							self.hash_table[j][i].value=value	#set the element to new value
							return True


# function remove: This function removes the key-value pair with the matching key. this function has as parameters the key and value, to be removed.
# If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, record with matching key is removed and returns True
	def remove(self, key):
		if (self.search(key)==None):
			return False
		else:		
			for j in range (self.capacity()):
				if(self.hash_table[j][0]!=None):	#check if the element is not none
					for i in range (len(self.hash_table[j])):
						if(len(self.hash_table[j])==1 and self.hash_table[j][i].key==key):	#check if the record has only one element and the key matches
							self.hash_table[j][i]=None	#sets the list to None
							self.size-=1			#reduces the __len__ of the table by 1
							return True
						if(self.hash_table[j][i].key==key): 	#check if the key matching
							del self.hash_table[j][i]	#delete the element in the list 
							self.size-=1
							return True


# function search: This function gets as prototype the key to find and returns the value of the record with the matching key. 
# If no reocrd with matching key exists in the table, function returns None
	def search(self, key):		
		for j in range (self.capacity()):
			if(self.hash_table[j][0]!=None):	#loop through elements of table
				for i in range (len(self.hash_table[j])):	#loop through elements of list
					if(self.hash_table[j][i].key==key):	#check if the key of the record matches the key to find
						return self.hash_table[j][i].value
		return None

# function capacity returns the total capacity of the table
	def capacity(self):
		return self.cap
	
# function __len__ returns the number of elements currently in the table
	def __len__(self):
		return self.size

class LinearProbingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key=key
			self.value=value



	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)
	
	def __init__(self, cap=32):
		self.hash_table = [None for i in range(cap)]
		self.size=0
		self.cap = cap


# Function insert: This function adds a new key-value pair into the table. this function has as parameters the key and value, to be inserted in a new record if the 
# record isn't already in the Table. If it's already in the table returns False otherwise adds the record in the hashed key position, if the hashed key element is None
# adds the record in that key otherwise finds the first None element after the hashed key, adds it and returns True.
	def insert(self,key, value):
		if (self.search(key)!=None): #check record is already available in the table with the same key-value
			return False
		else:
			hash_key = hash(key) % self.capacity()	
			for j in range(hash_key,hash_key+self.capacity()): #this loop will make sure that we loop for capacity times from the hashed key to hashed key-1
				size=j%self.capacity()	#calculate size using % to make sure that once we reach the end of the table, we return to the first element
				if self.hash_table[size] == None:
					self.hash_table[size] = self.Record(key,value)
					self.size+=1
					break
			if(len(self) >= self.cap*0.7):	#double if the actual number of elements in the table is above 70% of the total table capacity
				new_table = [None for i in range(self.cap*2)]
				for i in range(self.cap):	
					new_table[i]=self.hash_table[i]
				self.hash_table = new_table
				self.cap *= 2 	
			return True


# Function modify: This function modifies an existing key-value pair into the table. This function has as parameters the key and value, to be modified.
# If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, this function modifies the existing value to 
# the one passed in the function parameter and returns True

	def modify(self, key, value):
		if (self.search(key)==None):	
			return False
		else:
			hash_key = hash(key) % self.capacity()
			for j in range(hash_key,hash_key+self.capacity()):	#this loop will make sure that we loop for capacity times from the hashed key to hashed key-1
				size=j%self.capacity() 				#calculate size using % to make sure that once we reach the end of the table, we return to the first element
				if self.hash_table[size] != None:		
					if self.hash_table[size].key == key:	
						self.hash_table[size].value = value	#updates the value of that record to the new value
						return True


# Function remove: This function removes the key-value pair with the matching key. This function has as parameters the key and value, to be deleted.
# If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, record with matching key is removed and returns True

	def remove(self, key):
		if (self.search(key)==None):	
			return False
		else:
			hash_key = hash(key) % self.capacity()
			for j in range(hash_key,hash_key+self.capacity()):	#this loop will make sure that we loop for capacity times from the hashed key to hashed key-1
				size=j%self.capacity()				#calculate size using % to make sure that once we reach the end of the table, we return to the first element
				if self.hash_table[size] != None:	
					if self.hash_table[size].key == key:	
						self.hash_table[size] = None	#sets element back to None
						self.size-=1
						return True

# Function search: This function returns the value of the record with the matching key. If no record with matching key exists in the table, function returns None
	def search(self, key):
		for j in range (self.capacity()): #loop through elements of table
			if(self.hash_table[j]!=None):
				if(self.hash_table[j].key==key):
					return self.hash_table[j].value 	#returns value of matched key
		return None

# function capacity returns the total capacity of the table
	def capacity(self):
		return self.cap

# function __len__ returns the number of elements currently in the table
	def __len__(self):
		return self.size
