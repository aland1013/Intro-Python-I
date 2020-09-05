import sys
import math

if (len(sys.argv) == 1):
    print('Please include a number larger than 1 to evaluate')

else:
    num = int(sys.argv[1])

    if (num < 2):
        print('Please include a number larger than 1 to evaluate')
    
    else:

        primes = {}
        
        for i in range(2, num + 1):
            primes[i] = 'prime'
        
        for i in range(2, int(math.sqrt(num) + 1)):
            if primes[i] == 'prime':
                for j in range(i ** 2, num + 1, i):
                    primes[j] = 'not prime'
        
        print(f'{num} is {primes[num]}')