# the idea for this is to write a python function code that 
# will collect a user input and will continuously
# add the user input into an empty basket and it will stop when you dont add anything.
collectbasket=[]
def coffeecollector():
    while True:
        
        fruits=input('enter the items: ')
         
        
        if fruits == "":  
            
            break
        
        else:
            
            
            collectbasket.append(fruits) 
             
            print(collectbasket)
    print(collectbasket)
    
    
coffeecollector()    
            