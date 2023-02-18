import json
import re

x = input().strip(' ')
data = json.loads(x)
errors = {'bus_id': 0,
'stop_id': 0,
'stop_name': 0,
'next_stop': 0,
'stop_type': 0,
'a_time': 0}
for element in data:
    if re.match(r'(S|O|F|)$', element.get("stop_type")) is None:
        errors["stop_type"] += 1
    if re.match(r'([A-Z]\w* )+(Street|Avenue|Boulevard|Road)$', element.get("stop_name")) is None:
        errors["stop_name"] += 1
    if re.match(r'[021]{1}[0-9]{1}:[0-5]{1}[0-9]{1}$', element.get("a_time")) is None:
        errors["a_time"] += 1

print(f'Format validation: {sum(errors.values())} errors')
print('stop_name:', errors.get("stop_name"))
print('stop_type:', errors.get("stop_type"))
print('a_time:', errors.get("a_time"))
