#Azeez Olapade
#CS-175L
#World Series Assignment
def main():
    filereader = open('WorldSeriesWinners.txt', 'r')
    lines = filereader.readlines()
    while True:
        count = 0
        user_input = input("Enter the name of the team or quit: ")
        if user_input == 'q' or 'quit':
            quit()
        for x in lines:
            if user_input.casefold() in x.casefold():
                count+=1
        print(f'The {user_input} won the world series {count} times between 1903 and 2009')
        

if __name__ == '__main__':
    main()
        
