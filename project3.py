def titlefinder(line):
    listtitles = []
    ##titlefind = open('bestsellers.txt', 'r')
    ##line = titlefind.readlines()
    titlename = input("Enter a book title: ") 
    for x in line:
        if titlename.casefold() in x.casefold():
            y = x.rstrip('\n')
            listtitles.append(y)
    ##titlefind.close()
    print(listtitles)
if __name__ == '__main__':
    main()
