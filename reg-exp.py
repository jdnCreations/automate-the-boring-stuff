import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


mo = phoneNumRegex.search('My number is 415-555-4242.')
match = phoneNumRegex.search('555-555-5555')

print('phone num found: ' + mo.group())