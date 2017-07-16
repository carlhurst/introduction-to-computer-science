# This programme creats usernames from one file and moves it into a other file.

def main():
    # Greeting
    print("This programme is designed to create usernames from the input file of names \n")

    # Name the Files
    filename = input("Please input the name of the file: ") + ".txt"
    output = input("please enter the name of the output file: ") + ".txt"

    # open/ create the files
    opendoc = open(filename, "r")
    openout = open(output, "w")

    # read the names from the file
    for line in opendoc:
        first, last = line.split()
        # create username
        uname = (first[0] + last[:7]).lower()
        # Print the names to the file
        print(uname, file=openout)

    # Close the files
    opendoc.close()
    openout.close()


main()