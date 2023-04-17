#CS175L
#Azeez Olapade
#Expenses

import matplotlib.pyplot as plt
import numpy as np

def main():
    numlist = []
    try:
        file = open('expenses.txt', 'r')
        lines = file.readlines()
        for x in lines:
            try:
                y = x.split('\t')
                z = y[1]
                z = z.strip('\n')
                z = int(z)
                numlist.append(z)
            except ValueError:
                break
            
        bill_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
        y = np.array(numlist)
        plt.pie(y, labels = bill_labels)
        plt.title('Monthly Expenses')
        plt.show()
        
    except IOError:
        print("The file you tried to read does not exist")



if __name__ == '__main__':
    main()
