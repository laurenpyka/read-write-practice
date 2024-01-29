# This program writes three lines of data
# to a file.
def main():
 # Open a file named philosophers.txt.
    phil_file = open('philosophers.txt', 'w')
 
    phil_file.write('John Locke\n')
    phil_file.write('David Hume\n')
    phil_file.write('Edmund Burke')


# Close the file.
    phil_file.close()

# Call the main function.
main()
