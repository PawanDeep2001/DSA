def get_idx(ch):
	return ord(ch.lower()) - ord('a')
	
class Trie:
	class TrieNode:
		# TrieNode is internal.  Feel free to add
		# to the argument list for its init function.
		# add to this init function whatever data members you like
		def __init__(self):
			self.children = {}
			self.end_of_word = False # This will help when we want to retireve the words from the Trie
			

	# You cannot alter the prototype of this __init__ function
	# However you can add whatever data members you need
	def __init__(self):
		self.root = self.TrieNode()

	# function adds word to the Trie: inserts word character by character. In the root inserts, the first letter, then the second letter is inserted as children of the
	# first letter and so on, till reaching the end of the word, where we set that node's class variable end_of_word to True
	def insert(self, word):
		root = self.root
		for char in word:
			if char not in root.children:
				root.children[char] = self.TrieNode()
			root = root.children[char]
		root.end_of_word = True

	# function searches for word in the Trie, returns True if found, False otherwise: this function searches the word character by character.
	# the first letter in the root, the second as children, and so on, if any of the letter is not found in the root or its children returns 
	# False, if even the last letter matches it checks if the node's end_of_word is True returns true otherwise False.
	def search(self, word):
		root = self.root
		for char in word:
			if char not in root.children:
				return False
			root = root.children[char]
		return root.end_of_word

	# function returns the list of all words in the Trie in alphabetical order: this function calls the member recursive function find_all_words
	# and then returns the sorted word's list
	def get_all(self):
		words = []
		self.find_all_words(self.root, '', words)
		return sorted(words)

	# function returns the list of all words that begin with prefix in the Trie in alphabetical order: this function checks if the words in the
	# Trie begins with a certain prefix, checks if the prefix letters are available in the Trie and if they aren't returns an empty list
	# otherwise the member recursive function find_all_words and then returns the sorted word's list
	def begins_with(self, prefix):
		words = []
		node = self.root
		for c in prefix:
			if c not in node.children:
				return []
			node = node.children[c]
		self.find_all_words(node, prefix, words)
		return sorted(words)

	# function find_all_words gets as input the node, the prefix in case it's been called by the begins_with function and empty string if called by
	# get_all function, then words is the list of words found. first checks if the current node has it's member variable end_of_word set to true,
	# if it is true then it appends to node the word otherwise enters in the loop and we recall this recursive function till every letter has no
	# children left
	def find_all_words(self, node, prefix, words):
		if node.end_of_word:
			words.append(prefix)
		for c, child in node.children.items():
			self.find_all_words(child, prefix + c, words)