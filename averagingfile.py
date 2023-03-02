def main():
    outfile = open('numbers.txt', 'r')

    total = 0
    num = 0
    for line in outfile:
        total = total + float(line)
        num+=1

    average = total / num
    print(average)    
    outfile.close()
if __name__ == '__main__':
    main()
        
    
