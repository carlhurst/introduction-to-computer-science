"""
This programme is designed to show show the use of the twin prime conjecture.
"""
def main():
    print("This programme is designed to show show the use of the twin prime conjecture. \n")

    value = eval(input("Please enter the number you wish to use: "))

    while (value % 2) != 0:
        value = eval(input("Plese enter a even number: "))


    # container for prime values
    primes = []

    for n in range(value):
        if (n % 2) != 0 and (n % 3) != 0:
            primes.append(n)
        if n == 2 or n ==3:
            primes.append(n)

    for i in primes:
        for p in primes:
            # print(str(i) + "\t" + str(p))

            if i + p == value:
                print("The sum of: " + str(i) + ", " + str(p) + " is equal to value entered")
                primes.remove(i)
                break


if __name__ == '__main__':
    main()