def sum_digits(number):
    sum_of_digits = str(number)

    while(len(sum_of_digits) > 1):
        total = 0
        for digit in sum_of_digits:
            total += int(digit)
        sum_of_digits = str(total)
        print(total)

    return(total)

print(sum_digits(999999999999999999999999999999))