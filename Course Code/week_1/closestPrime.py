import math

def next_prime(n):
    if n <= 1:
        return 2
        
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

# Helper method
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True