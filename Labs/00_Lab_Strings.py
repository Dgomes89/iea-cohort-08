# Write two separate strings from the user
first = input("Enter first string:")
second = input("Enter second string:")

# Create a new string which consists of the second string followed by a space, followed by the first string
combined = second + ' ' + first
combined_format = f'{second} {first}'

print(first, second)
print(combined)
print(combined_format)