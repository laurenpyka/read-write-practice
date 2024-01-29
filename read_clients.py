def main():
    infile = open('clients.txt', 'r')
    counter = 1
    for line in infile:
        print(f'{counter}. {line}')
        counter +=1
    infile.close()
main()

    