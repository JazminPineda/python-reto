import math

def prime_checker(number):
    for n in range(2, number):
        if number % n == 0:
            print("It's not a primer numer.")
            return False
        
    else:
        print("It's a prime number")

prime_checker(73)
prime_checker(75)