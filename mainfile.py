import project1
import project
import project2
import project3
def main():
    totallines = 0 
    filelines = []
    filereader = open('bestsellers.txt', 'r')
    lines = filereader.readlines()
    for x in lines:
        totallines+=1
    print(f"Read {totallines} books.")

    choice = ''
    while choice.upper() != 'Q':
        choice = input("What would you like to do?\n\t1: Look up year range\n\t2: Look up month/year\n\t3: Look up author\n\t4: Search for title\n\tQ: Quit\n\t")
        if choice == '1':
            project.yearrangefinder(lines)
        elif choice == '2':
            project1.monthyearfinder(lines)
        elif choice == '3':
            project2.authorfinder(lines)
        elif choice == '4':
            project3.titlefinder(lines)
        elif choice.upper() == 'Q':
            print("Done")
        else:
            print("I dont understand this command")

    filereader.close()



    
if __name__ == '__main__':
    main()
