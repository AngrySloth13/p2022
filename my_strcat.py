'''
Create two strings. Create a single string from that. 

'''
import sys

def my_strcat(str1, str2):
    print(str1+ str2)

def main(argv):
    my_strcat(argv[1], argv[2])
if __name__ == "__main__":
    sys.exit(main(sys.argv))
