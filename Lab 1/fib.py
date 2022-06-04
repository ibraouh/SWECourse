# Understand
	# Questions: Given an int n:
		# can n<1? (No) 
		# Is the first position of the fib series considered index 1 or 0? (1) 
		# Is there a maximum limit for n? (n=100) 
		# Do we need to return any value? (No just print it)

# Match
	# We are doing something over and over
	# We can use a loop or we can use recursion

# Plan and Pseudocode
	# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, ...
		# Pattern:
			# 5th = 4th + 3rd
			# 4th = 3rd + 2nd
			# 3rd = 2nd + 1st
			# ...

			# fib(5) = fib(4) + fib(3)
			# fib(4) = fib(3) + fib(2)
			# fib(3) = fib(2) + fib(1)
			
			# Formula: fib(n) = fib(n-1) + fib(n-2)

		# Base case: 
			# if n = 1 -> 0
			# if n = 2 -> 1

		# Recursive call:
			# fib(n) = fib(n-1) + fib(n-2) -> same as the formula

# Implement
def fib(n):
	if n == 1 or n == 2: return 1
	else: return fib(n-1) + fib(n-2)

def main(): 
	print(fib(5))

if __name__ == '__main__':
	main()