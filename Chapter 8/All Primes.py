"""
This programme is designed to find all the primes upto a given user defined value.
"""

def main():
    print("This programme is designed to find all the primes upto a given user defined value. \n")

    upper_limit = input("Please enter the number you wish to find all primes up to: ")

    for i in range(upper_limit):

        if (i % 2) != 0 and (i % 3) !=0:
            print (i)

if __name__ == '__main__':
    main()