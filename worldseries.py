#Azeez Olapade
#CS-175L
#World Series Assignment
def main():
    filereader = open('WorldSeriesWinners.txt', 'r')
    lines = filereader.readlines()
    while True:
        count = 0
        user_input = input("Enter the name of the team or quit: ")
        if user_input == quit or user_input == 'q':
            quit()
            
        while user_input is not any(lines):
            print("You searched an invalid team name, please try again")
            user_input = input("Enter the name of the team or quit: ")
            if user_input == quit or user_input == 'q':
                quit()
            
        for x in lines:
            if user_input.casefold() == x.casefold():
                count+=1
        
        
        print(f'The {user_input} won the world series {count} times between 1903 and 2009')
        

if __name__ == '__main__':
    main()
        
