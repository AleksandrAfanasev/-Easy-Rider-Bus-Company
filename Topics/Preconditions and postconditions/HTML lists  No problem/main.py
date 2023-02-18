import re

string = input()

result = re.findall('(?<=<li>).+?(?=</li>)', string)

for el in result:
    print(el)
