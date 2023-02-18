import re

s = input()
print("Thank you!" if re.match('[a-zA-Z]', s) else 'Oops! The username has to start with a letter.')
