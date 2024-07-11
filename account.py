print(" WELCOME TO my app bank")
 


balance = 0

while True:
    transaction = input("Type in your choice of transaction (deposit or withdraw), or 'quit' to stop: ")
    if transaction.lower() =='quit':
        break

    amount = int(input("Enter amount: "))
    if transaction.lower() == 'deposit':
        balance += amount

    elif transaction.lower() == 'withdraw':
        balance -= amount
    print(f"Balance: {balance}")

print(f"Final Balance: {balance}")

if balance <0 :
    print(" Insufficient Balance. Try Again Later !")
