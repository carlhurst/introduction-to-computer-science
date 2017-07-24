"""
The Collatz Conjecture
"""

def main():

    print("This programme shows the Collatz conjecture \n")

    num = eval(input("Please entre the starting value you wish to use: "))

    while (num != 1):

        if (num % 2) == 0 and num > 0:
            num = num / 2
            print(num)

        else:
            num = (num * 3) + 1
            print(num)


    if __name__ == '__main__':
        main()
main()