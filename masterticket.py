TICKET_PRICE = 10



tickets_remaining = 100


#calulate_price func
def calulate_ticket_price(amount_of_tickets,ticket_price ):
    SERVICE_CHARGE = 2
    return (amount_of_tickets * ticket_price) + SERVICE_CHARGE


# run code continously
while tickets_remaining != 0:
    # prompts the user
    print("There're only {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?")
    # watchs for correct Value
    try:
        amount_of_tickets = int(input("How many tickets do you like {}?".format(name)))
        if amount_of_tickets > tickets_remaining:
            raise ValueError("Cannot be more than {}".format(tickets_remaining))
    except ValueError as err:
        print("Oh no we ran into an issue. {} .Please try again".format(err))
    else:
        total = calulate_ticket_price(amount_of_tickets, TICKET_PRICE)
        print("The total for {} tickets is ${} dollars".format(amount_of_tickets, total))
        response = input("Would you like to buy tickets {}?".format(name))
        if response.lower() == "yes":
            print("Sold and have a great time at the show {}".format(name))
            tickets_remaining = tickets_remaining - amount_of_tickets
        else:
            print("Have a nice day {}".format(name))
print("Sorry but all tickets have sold out")
