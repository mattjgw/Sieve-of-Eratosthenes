numbers = []  # Declaring the array
for i in range(100):  # Creating a boolean array with 100 elements to represents the primality of each number
    numbers.append(True)  # All numbers start prime
for i in range(2, 10):  # Sieve of Eratosthenes algorithm
    if numbers[i] is True:
        for j in range(i**2, 100, i):
            numbers[j] = False
for i in range(2, len(numbers)):  # Print out prime numbers, start at 2 since 0 and 1 cannot be prime
    if numbers[i] is True:
        print(i)
