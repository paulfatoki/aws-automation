counter = 0
basket = []

#Initialize the counter

while True:
    numbers = int(input("Enter a number"))
    
    # Take input from the user and convert it to an integer
    
    counter += numbers
    
    #Add the input number to the counter
    
    print(f"Result: {counter}") 
    
    #Print the current value of the counter
    
    if counter >= 500:
        break
    else:
        print(counter) 
        basket.append(counter)
print(basket)        
        
        #Print true if counter is less than or equal to 500
    
    