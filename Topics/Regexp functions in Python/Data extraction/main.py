import re

string = input()
print(re.split('<START>|<END>', string)[1])