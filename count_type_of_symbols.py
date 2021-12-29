'''
Count all the letters, digits, or special symbols in a string. 
thongal@thongal-000608:~/Documents/shri/p2022$::python3 ./count_type_of_symbols.py test123$
Input valuetest123$
116 t
101 e
115 s
116 t
49 1
50 2
51 3
36 $
Number of letters: 4
Number of digits: 3
Number of special symbols: 1
(!@#$%^ cannot be used in any input)
'''
import string
import sys
import os

letter = 0
digit  = 0;
special_sym = 0;

def count_symbol(input1) :
    print ("Input value" + input1)
    global letter, digit, special_sym
    for i in range (0,len(input1)):
        print ("%d" % ord(input1[i]), input1[i])
        if input1[i] >= 'a' and input1[i] <= 'z':
            letter = letter + 1

        if input1[i] >= '0' and input1[i] <= '9':
            digit = digit + 1
        if input1[i] >= '!' and input1[i] <= '/':
            special_sym  = special_sym + 1
        
def main(argv):
    count_symbol(argv[1])
    print ("Number of letters: " + str(letter))
    print ("Number of digits: "  + str(digit))
    print ("Number of special symbols: " + str(special_sym))

if __name__ == "__main__":
    sys.exit(main(sys.argv))





