#!/usr/bin/env python
import sys

# This file calculates the filesize of files from the output of binwalk. (default commandline output)
testlist = []

def main():
    f = open(sys.argv[1], "r")
    test = f.read().split('\n')
    counter = 0
    for line in test:
        # split offset, hex offset, filename
        if line != '':
            if line.startswith('DECIMAL'):
                decimal = line.find('DECIMAL')
                hexadecimal = line.find('HEXADECIMAL')
                description = line.find('DESCRIPTION')
                # print(decimal, hexadecimal, description)
            else:
                try:
                    if not line.startswith('---'):
                        a = line[decimal:hexadecimal].strip()
                        b = line[hexadecimal:description].strip()
                        c = line[description:]
                        # print("{} - {} - {}".format(a, b, c))
                        testlist.append([a,b,c])
                except UnboundLocalError:
                    pass
        counter+=1
    try:    
        # Loop through the list    
        for i in range(len(test)):
            # print the filesize. take the next offset and substract with current offset.
            # We cant calculate the last offset.
            print("Filesize: {:<10} - {} - Desc: {}".format((int(testlist[i+1][0]) - int(testlist[i][0])), hex(int(testlist[i+1][0]) - int(testlist[i][0])), testlist[i][2]))
    except IndexError:
        pass

if __name__ == '__main__':
    main()