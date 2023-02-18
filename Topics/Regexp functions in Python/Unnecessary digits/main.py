import re       
names = input()
print(re.sub(r'\d+', ' ', names).split(' '))
