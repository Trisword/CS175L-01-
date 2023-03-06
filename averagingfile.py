def main():
    total = 0
    num = 0

    
    outfile = open('numbers.txt', 'r')
    for line in outfile:
        total = total + float(line)
        num+=1
        print(f"I read in {num:.2f} numbers(s)  Current number is: {float(line):.2f}")
        print(f"Total is: {total:.2f}")


    average = total / num
    outfile.close()

    print("Average is:", average)

if __name__ == '__main__':
    main()
        
    
