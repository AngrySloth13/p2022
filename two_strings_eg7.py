
import sys
import re
'''
thongal@thongal-000608:~/Documents/shri/p2022$::python3 ./two_strings_eg7.py cat "my name is cat but am not cat"
1
2
'''
def is_balanced(needle, haystack):
    pattern = re.compile(needle)
    sentence = (haystack)
    matches = pattern.finditer(sentence)

    matching=0
    
    for match in matches:
        matching=matching+1
        print(matching)
        
        

def main(argv):
    is_balanced(argv[1],argv[2])

if __name__ == "__main__":
    sys.exit(main(sys.argv))

             
