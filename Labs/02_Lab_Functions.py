# Define our function
def calculate():
    
    num_1 = int(input('Please enter the first number: '))
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
Enter operation here= ''')
    num_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
        
    else:
        print('You have not typed a valid operator, please run the program again.')
        
# Call to calculate() outside of the function
calculate()

