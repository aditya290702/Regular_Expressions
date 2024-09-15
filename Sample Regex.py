import re
import sys
def regex1():
    s = ["foo123bar"]
    print(re.search("123" ,s))
    if re.search("123" ,s):
        print('Found a match.')
    else:
        print('No match.')

def main():
    s = 'foo123bar'
    regex1()

if __name__=="__main__":
    main()

