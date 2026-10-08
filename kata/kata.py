def is_even(result):
    if (result % 2 == 0):
        return True
    else:
        return False


def is_prime(result):
    if (result < 2):    
        return False
    else:
        for numbers in range(1, result):
            if(result % numbers == 0):
                return True 



def subtract(first_num, second_num):
    largest = num_one
    smallest = num_two
    if (num_two > num_one):
        largest = num_two
        smallest = num_one

    difference = largest - smallest
    return difference




def divide(numberOne, numberTwo):
    quotient = 0
    if (numberTwo == 0):
        quotient = 0
    else:
        quotient = num_one / num_two
    return quotient




def factor(digit):
    count = 0
    for number in range(1, digit):
        if (digit % number == 0):
            count += 1

    return count


def is_square(number):
    is_sqr = False
    for digit in range(number):
        if (digit * digit == number):
            is_sqr = True
            return is_sqr
        else:
            is_sqr = False
    return is_sqr


#def is_palindrome(digit):
 #   if(reversed(digit) == digit):
  #      return True
    


def factorial_of_number(number):
    result = 1
    for digit in range(1 , number + 1):
        result = result * digit

    return result


def square_of(number):
    return number*number





num_one = 25
num_two = 5
print(subtract(num_one, num_two)) 
print(is_even(num_one))
print(is_prime(num_two))
print(divide(num_one, num_two))
print(factor(num_two))
print(is_square(num_one))
#print(is_palindrome(num_one))
print(factorial_of_number(num_two))
print(square_of(num_two))
















