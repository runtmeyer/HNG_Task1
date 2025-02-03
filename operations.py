def is_perfect_number(n):
    if n < 2:
        return False  
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_prime_number(n):
    if n < 2:
        return False 
    
    for i in range(2, n):
        if n % i == 0:
            return False 

    return True

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def is_armstrong(n):
    order = len(str(n))

    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    # display the result
    if n == sum:
        return True
    else:
        return False

def is_even(n):
    if n%2 == 0:
        return True
    else: 
        return False
    
def get_property(n):
    if is_armstrong(n) and is_even(n):
        return ["armstrong", "even"]
    elif is_armstrong(n) and not is_even(n):
        return ["armstrong", "odd"]
    elif not is_armstrong(n) and not is_even(n):
        return ["odd"]
    elif not is_armstrong(n) and is_even(n):
        return ["even"]

