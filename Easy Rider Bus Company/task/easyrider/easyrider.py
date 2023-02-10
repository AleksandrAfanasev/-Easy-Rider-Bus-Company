import json

x = input().strip(' ')
data = json.loads(x)
errors = {'bus_id': 0,
'stop_id': 0,
'stop_name': 0,
'next_stop': 0,
'stop_type': 0,
'a_time': 0}
for element in data:
    if type(element.get("bus_id")) != int:
        errors['bus_id'] += 1
    if type(element.get("stop_id")) != int:
        errors['stop_id'] += 1
    if type(element.get("stop_name")) != str or len(element.get("stop_name")) < 1:
        errors["stop_name"] += 1
    if type(element.get("next_stop")) != int:
        errors["next_stop"] += 1
    if type(element.get("stop_type")) != str or len(element.get("stop_type")) > 1:
        errors["stop_type"] += 1
    if type(element.get("a_time")) != str or len(element['a_time']) < 1:
        errors["a_time"] += 1

print(f'Type and required field validation: {sum(errors.values())} errors')
for element in errors:
    print(element, errors[element])
