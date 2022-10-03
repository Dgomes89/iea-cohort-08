def collatz(n):
    while n != 1:
        if n % 2 == 0:
            print(f"the {n} number is even, dividing by 2")
            n = n // 2
            print(n)
        else:
            print(f"the {n} number is odd, multiplying by 3 and adding 1")
            n = n * 3 + 1
            print(n)
collatz(15)