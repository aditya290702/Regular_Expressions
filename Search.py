import re

def searchit():
    s = 'foo123bar'
    print(re.search('foo', s))
# print(re.search('[0-9][0-9][0-9]', "foo456bar"))
#int(re.search('[0-9][0-9][0-9]', "234baz"))
#    print(re.search('[0-9][0-9][0-9]', "qux678"))
#    print(re.search('[0-9][0-9][0-9]', "12foo34"))

def main():
    s = 'foo123bar'
searchit()

if __name__=="__main__":
    main()

