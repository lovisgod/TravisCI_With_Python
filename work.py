def is_prime (number):

    if number in (0,1):
        return False 

    if number < 0:
        return False    
    """ return true if the *number* is prime"""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True



is_prime(5)            