
import sys

'''
1. convert number to char
2. from range of 0-256

'''
def print_char(input):
    print ("%d"%input, chr(input))

def main(argv):
    for i in range (0,256):
        print_char(i)
if __name__ == "__main__":
    sys.exit(main(sys.argv))

