# Prompt the user to input a five-digit integer
num = int(input("Enter a five-digit integer: "))

# Separate the digits and store them in a list
digits = [int(d) for d in str(num)]

# Display the digits
print("The digits are:", digits[0], digits[1], digits[2], digits[3], digits[4])


   