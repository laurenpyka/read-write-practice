def main():
    infile = open('clients.txt', 'r')
    counter = 1
    for line in infile:
        lineno += 1 
        print(f'{counter}. {line}')
        counter +=1
    infile.close()

main()

    