#a simple password checker. The program should ask the user to
#enter a password and continue to prthem until they enter the correct password. 
# Once the correct password is entered, the program should print a success

correctpassword = 'jgold'
userinput =input('enter you password :')
while userinput != correctpassword:
    print('incorrect password, please try again')
    userinput =input('enter you password')  
print("success, you just entered the right password") 