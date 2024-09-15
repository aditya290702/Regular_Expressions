import re
import sys

def metac():
    s = 'foo123bar'
    print(re.search('1.3', s))
    s = 'foo13bar'
    print(re.search('1.3', s))

def main():
    s = 'foo123bar'
    metac()

if __name__=="__main__":
    main()