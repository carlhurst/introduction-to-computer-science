
# This programme is designed to show the numarological number of the name given

print("This programme is designed to create a numerical representaion of your name \n")

Name = input("Please input your name: ")

Name = Name.lower().split()

Nameval = 0

print(Name)

for names in Name:
    for char in names:
        print(ord(char)-96)
        Nameval = Nameval + (ord(char)-96)

print("The Total Numarological value of your name is: {}" .format(Nameval))
