#Multiple algorithm so check the primality of a number

#Simplest way to find prime number
def is_prime(n):
	if n <= 1: return False
	for i in range(2, n):
		if n % i == 0: return False
	return True


from math import floor, sqrt
def is_prime(n):
	if n <= 1: return False
	for i in range(2, floor(sqrt(n)) + 1):
		if n % i == 0: return False
	return True


'''
we know that except 2 any other even number can't be a prime
so all even number can be skipped 
'''
from math import floor, sqrt
def is_prime(n):
	if n <= 1: return False
	if n == 2: return True
	if n > 2 and n % 2 == 0: return False
	
	for i in range(3, floor(sqrt(n)) + 1, 2):
		if n % i == 0: return False
	return True


# base-2 Fermat primality test
def is_prime(x):
    return pow(2, x - 1, x) == 1


#another fast algo for prime
def is_prime(number):
    ''' if number != 1 '''
    if (number > 1):
        ''' repeat the test few times '''
        for time in range(3):
            ''' Draw a RANDOM number in range of number ( Z_number )  '''
            randomNumber = random.randint(2, number)-1
            
            ''' Test if a^(n-1) = 1 mod n '''
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        ''' case number == 1 '''
        return False  

