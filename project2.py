def authorfinder(line):
    listauthorname = []
    ##authorfind = open('bestsellers.txt', 'r')
    ##line = authorfind.readlines()
    authorname = input("Enter an author name: ")
    try:
        while type(int(authorname)) == int:
                print("You only entered numeric data, please try again.\n")
                authorname = input("Enter an author name: ")
    except ValueError:
        pass
        
             
    for x in line:
        if authorname.casefold() in x.casefold():
            y = x.rstrip('\n')
            listauthorname.append(y)
    ##authorfind.close()
    print(listauthorname)
if __name__ == '__main__':
    main()
