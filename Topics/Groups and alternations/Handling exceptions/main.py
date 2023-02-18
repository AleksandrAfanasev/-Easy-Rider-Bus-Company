import re


# put your regex in the variable template
template = "(Value|Name|Type)(Error)"
string = input()
# compare the string and the template
print(re.match(template, string).group(1) if re.match(template, string) else None)
