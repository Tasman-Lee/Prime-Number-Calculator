# What does this program does:
# - Identify and remove duplicating numbers in an array
# - Filter out composite numbers in an array
# - Calculate the sum

#main function
if __name__ == "__main__":
  #variables to accept return value from the function 
  unique_numbers, sum_prime_numbers = remove_duplicates_and_sum_primes(numbers)

    #if statement to print output
    if not unique_numbers:
        print("No unique prime numbers found.")
    else:
        print("Unique prime numbers:", unique_numbers)
        print("Sum of prime numbers:", sum_prime_numbers)

#function to check if the numbers are prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#function to remove duplications and fund the sum
def remove_duplicates_and_sum_primes(numbers):
  
    #variables to accept array of numbers, set() to remove duplicates 
    unique_numbers = set()

    #variables to accept sum
    sum_prime_numbers = 0

    #for loop to find sum
    for num in numbers:
        if num not in unique_numbers and is_prime(num):
            unique_numbers.add(num)
            sum_prime_numbers += num

    #return values 
    return list(unique_numbers), sum_prime_numbers


