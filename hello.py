first_name = input("What is your first name?")

if first_name == "Elijah" :
    print("Welcome {}".format(first_name))
elif first_name == "max" :
    print(first_name, "is learning python already")
else :
    # this is just in case we have a younger user who can't read
    age = int(input("How old are you?"))
    if age <= 6 :
        print("Sorry but you're only {}".format(age))
    print("You should totally learn python {}".format(first_name))
print("Have a great day {}".format(first_name))
