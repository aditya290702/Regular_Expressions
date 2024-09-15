import re
import sys

def Charmetac():
    s = 'foo123bar'

print(re.search('ba[artz]', 'foobarqux'))
print(re.search('ba[artz]', 'foobazqux'))  # <_sre.SRE_Match object; span=(3, 6), match='baz'>
# A character class can also contain a range of characters separated by a hyphen (-),
# in which case it matches any single character within the range.
# For example, [a-z] matches any lowercase alphabetic character between 'a' and 'z', inc
print(re.search('[A-Z]', 'FOObar'))
print(re.search('[a-z]', 'FOObar'))  # <_sre.SRE_Match object; span=(3, 4), match='b'>
print(re.search('[0-9][0-9]', 'foo123bar'))


def main():
    s = 'foo123bar'
    Charmetac()

if __name__=="__main__":
    main()