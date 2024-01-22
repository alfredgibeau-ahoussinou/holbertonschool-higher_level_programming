import random

# Generate a random signed number
number = random.randint(-10, 10)

# Print the generated number
print("The number is:", number)

# Check if the number is positive, negative, or zero
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
