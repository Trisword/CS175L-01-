lettergrade = ''
list = []

def calc_average():
    global userinput1
    userinput1 = float(input("Enter test score 1: "))
    global userinput2
    userinput2 = float(input("Enter test score 2: "))
    global userinput3
    userinput3 = float(input("Enter test score 3: "))
    global userinput4
    userinput4 = float(input("Enter test score 4: "))
    global userinput5
    userinput5 = float(input("Enter test score 5: "))
    total = userinput1 + userinput2 + userinput3 + userinput4 + userinput5
    global average
    average = total / 5
    
def determine_grade(x):
    if x <= 90:
        lettergrade = 'A'  
    elif x <= 80:
        lettergrade = 'B'
    elif x <= 70:
        lettergrade = 'C'
    elif x <= 60:
        lettergrade = 'D'
    else:
        lettergrade = 'F'

    return lettergrade

calc_average()

lettergrade1 = determine_grade(userinput1)
lettergrade2 = determine_grade(userinput2)
lettergrade3 = determine_grade(userinput3)
lettergrade4 = determine_grade(userinput4)
lettergrade5 = determine_grade(userinput5)
avggrade = determine_grade(average)	

print("Score		Numeric Grade	Letter Grade")
print("----------------------------------------------------")
print(f"score 1:	{userinput1}		{lettergrade1}")
print(f"score 2:	{userinput2}		{lettergrade2}")
print(f"score 3:	{userinput3}		{lettergrade3}")
print(f"score 4:	{userinput4}		{lettergrade4}")
print(f"score 5:	{userinput5}		{lettergrade5}")
print(f"Average score:	{average}            {avggrade}")

def repeat():
    repeatinput = input("Enter 'yes' if you would like to do another calculation: ")
    while repeatinput.upper() == 'YES':
        calc_average()
        lettergrade1 = determine_grade(userinput1)
        lettergrade2 = determine_grade(userinput2)
        lettergrade3 = determine_grade(userinput3)
        lettergrade4 = determine_grade(userinput4)
        lettergrade5 = determine_grade(userinput5)
        avggrade = determine_grade(average)
        print("Score		Numeric Grade	Letter Grade")
        print("----------------------------------------------------")
        print(f"score 1:	{userinput1}		{lettergrade1}")
        print(f"score 2:	{userinput2}		{lettergrade2}")
        print(f"score 3:	{userinput3}		{lettergrade3}")
        print(f"score 4:	{userinput4}		{lettergrade4}")
        print(f"score 5:	{userinput5}		{lettergrade5}")
        print(f"Average score:	{average}            {avggrade}")
    print("Thanks for using the averaging calculator")
repeat()
