import re

string = input()
expenses = re.findall(r'(?<=\$)\d+', string)
def num(x):
    return int(x)

print(f'This week you have spent: {sum(map(num, expenses))} dollars')
