
"""This programme is designed to calculate the wages of people accounting for any overtime calculations they are due"""


def main():
    print("This programme is designed to calculate the wages of people accounting for any overtime calculations they are due")

    hours = eval(input("\n Please enter the amount of hours you have worked this week: "))

    hourly_rate = 6.50

    wage = 0

    if hours > 40 :
        wage = (hourly_rate * 40) + ((hours - 40) * (hourly_rate * 1.5))

        print("Your salary for this week is: {}".format(wage))
    else:
        wage = (hourly_rate * hours)

        print("Your salary for this week is: {}".format(wage))
main()