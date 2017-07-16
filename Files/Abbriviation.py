# This file is designed to create abriviations on the input the user enters

import os

os.chdir('/Users/carlhurst/Desktop')

print("This programme creates abbriviation \n")

word = input("Please input the word you want a abriviation for: ")

writefile = open("Abb.txt","w")

Abbriviation = word.split()

for i in Abbriviation:
    print(i[0].upper(),file=writefile,end="")

writefile.close()

