def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == number

for num in range(1, 10000):
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
