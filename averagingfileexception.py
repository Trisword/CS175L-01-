def main():
    total = 0
    num = 0

    try:
        outfile = open('numbers.txt', 'r')
        for line in outfile:
            try:
                total = total + float(line)
                num+=1
                print(f"I read in {num:.2f} numbers(s)  Current number is: {float(line):.2f}")
                print(f"Total is: {total:.2f}")

            except ValueError:
                ##line = line.strip('\n')
                print('Non-numeric data found in the file:'+line)
                

        average = total / num
        outfile.close()

        print("Average is:", average)

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('No numeric was data found in the file.')

    except:
        print('An error occured.')
        
if __name__ == '__main__':
    main()
        
    
