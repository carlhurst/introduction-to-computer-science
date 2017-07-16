 # This programme takes the date format and returns a neatly formated string with Day, Month, Year in full form

"""
This information will be used to practice crap shoot tables
"""

Months = ['January', 'Febuary', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December']

# Empty list to hold the date that is input


# Hold the date input in a list value
ls = input("Please input the date in the following format dd/mm/yy: ")

# Pass the Month into a variable to be used print string
date = []

date = ls.split("/")

# Use the split date to select a month

Month = int(date[1])-1


print("Today is the: {} {} {}".format(date[0], Months[Month], date[2]))

d