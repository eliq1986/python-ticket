import sys



## while loop
MASTER_PASSWORD = "opensesame"

password = input("Please enter a password:  ")
attempt_count = 1
while password != MASTER_PASSWORD :
    if  attempt_count == 3 :
        sys.exit("Too many pw attempts")
    attempt_count += 1
    password = input("invalid password, try again ")
print("Welcome to the site")
