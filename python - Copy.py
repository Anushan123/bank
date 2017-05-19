customers = []

def get_integer_input(prompt):
   
 while(True):
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Incorrect value entered..Please try again.")

def consoleHandler():
    
    print("~"*50)
    print("Welcome to Bank SWISSBANK")
    print("~"*50)
    print("\nSelect an option to get started")
    print("1: Add an customer")
    print("2: Deposit money for an customer")
    print("3: Withdraw money for an customer")
    print("4: Display a list of customers with their balance")
    print("5: Quit")

    response = input("Enter an option [1-6]:\n")
    handleInput(response)

def handleInput(response):
   
    if response.isdigit():
        response = int(response)

        
        if response == 1:
           
            if len(customers) < 5:
                
                customer = {}
                customer['name'] = input("\nEnter the new customer's name: ")
                customer['DOB'] = input("\nEnter the date of birth of the customer (ddmmyyyy): ")
                customer['NIC'] = input("\nEnter the NIC number: ")
                customer['amount'] = get_integer_input("\nEnter the initial deposit amount(in rupees): ")
                customers.append(customer)
            else:
                print("Customer number exceeded!")

        elif response == 2:
   
            nic = input("Enter the customers nic:\n")
            found = False
            for customer in customers:
                if customer['NIC'] == nic:
                    amount = get_integer_input("Enter the amount to be deposited: ")
                    print("The amount " + str(amount) + " has been deposited in your bank")
                    customer['amount'] += amount
                    print("\n"+customer["name"]+"\t\t"+str(customer['amount']))
                    found = True

            if not found:
                print("Sorry the customer name could not be found!")

        elif response == 3:
           
            
            nic = input("Enter the customers nic:\n")
            found = False
            for customer in customers:
                if customer['NIC'] == nic:
                    amount = get_integer_input("Enter the amount to be withdrawed: ")
                    if customer['amount'] <= amount:
                        print("Sorry insufficient blance")
                    else:
                        print("Your transaction was successful")
                        print("The amount " + str(amount) + " has been withdrawed from your account")
                        customer['amount'] -= amount
                        print("\n"+customer["name"]+"\t\t"+str(customer['amount']))
                    found = True
			
            if not found:
                print("Sorry the customer name could not be found!")

            print("")

           
        elif response == 4:
            for customer in customers:
                print("\n"+customer["name"]+"\t\t"+str(customer['amount']))

            if len(customers) == 0:
                print("\nSorry no customers found!\n")

        elif response == 5:
            exit(1)

        else:
            print("\nEnter a number between 1 and 6..Try again..\n")
    else:
        print("\nEnter a number between 1 and 6..Try again..\n")

def main():
    while(True):
        consoleHandler()

main()
