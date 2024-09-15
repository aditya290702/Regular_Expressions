import sys
import re
def Regexsearch():
    listmy = ["fiof"]
# If a ^ character appears in a character class but isn’t the first character,
# then it has no special meaning and matches a literal '^' charac
    print(re.search('[^0-9]', listmy))
    print(re.search('[#:^]', 'foo^bar:baz#qux'))
    print(re.search('[#:^]', 'foo^bar:baz#qux'))
#  if you want the character class to include a literal hyphen character
# You can place it as the first or last character or escape it with a backslash (\)
    print(re.search('[-abc]', '123-456'))  # <_sre.SRE_Match object; span=(3, 4), match='-'>
    print(re.search('[abc-]', '123-456'))

def main():
    Regexsearch()

if __name__=="__main__":
    main()