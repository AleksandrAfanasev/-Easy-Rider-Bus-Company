import re

template = r'are you ready??.?.?'
string = input()
print(len(re.match(template, string).group()) if re.match(template, string) else 0)
