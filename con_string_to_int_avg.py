
import sys

'''
Take a number input as a string, convert it into integer, and find the average of the numbers
average algorithm 
Algorithm:
     Average = (sum of elements)/ number-of-element
e.g
x = 1 2 3 
y=6
y/len(input) = average

'''
def num_to_avg(input1):
    print(input1)
    for a in range(0,len(input1)):
        sum=0
        for x in input1:
            sum = sum + x
        return (sum/len(input1))

def main(argv):
    len1= len(argv)
    i = 0
    input1 = [0] * (len1 - 1)
    for y in range(1, len1):
        input1[i] = int(argv[y])
        i = i+1
    ret = num_to_avg(input1)
    print (ret)
if __name__ == "__main__":
    sys.exit(main(sys.argv))
