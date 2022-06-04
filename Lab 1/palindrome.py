# Understand: 
	# Questions: 
		# are we allowed to use built in functions? (Yes)
		# can we have a variable that's NULL? (No)
		# can the word have special chars? (No)
		# Implement in loop? (Whichever)

# Match:
	# Loop or recursion

# Pseudocode:
	# clean the input: Lowercase + remove numbers + remove whitespace
	# use pointers one at the end and the front + compare the values

def isPalindrome(word):
	
	if word == "" or word == None: 
		return False

	# Cleaning the word
	newword = word.replace(" ", "").lower()

	# Two pointers
	p1 = 0
	p2 = len(newword)-1

	# Loop
	# for i in range(0, len(newword)/2):
	while p1 < p2:
		if newword[p1] != newword[p2]:
			print(newword)
			return False
		
		else: 
			p1 =+ 1
			p2 =- 1
		
	print(newword)
	return True


def main():
	word = "dgradh liujhf woehfe"
	print(isPalindrome(word))

if __name__ == '__main__': main()

# Complexity: O(max(n, n, n)) = O(n)

