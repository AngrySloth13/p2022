'''
Count all the letters, digits, or special symbols in a string. 

'''
import string
import sys
import os

letter = 0
digit  = 0;
special_sym = 0;

def count_symbol(input1) :
    print ("Input" + input1)
    global letter
    for i in range (0,len(input1)):
        print ("%d" % ord(input1[i]), input1[i])
        if input1[i] >= 'a' and input1[i] <= 'z':
            letter = letter + 1

def main(argv):
    count_symbol(argv[1])
    print ("Number of letters:" + str(letter))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
