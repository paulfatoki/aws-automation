#Write a Python program that checks whether a given positive integer
# is a prime number. The program should ask the user to input a number
# and then use a while loop to determine if the number is prime.

number = int(input("Enter a positive integer: "))

# Initialize a variable to keep track of the divisors
divisor = 1

# Initialize a variable to determine if the number is prime
is_prime = True

# Use a while loop to check for divisors
while divisor <= number // 2:
    divisor += 1
    
    
    if number % divisor == 0 and is_prime:
        is_prime = False
        break  # If a divisor is found, exit the loop
    

# Display the result
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")