import json

x = input().strip(' ')
data = json.loads(x)
Bus_line_info = {'bus_id: 128': 0,
'bus_id: 256': 0,
'bus_id: 512': 0,
'bus_id: 1024': 0}
for element in data:
    if element.get("bus_id") == 128:
        Bus_line_info["bus_id: 128"] += 1
    if element.get("bus_id") == 256:
        Bus_line_info["bus_id: 256"] += 1
    if element.get("bus_id") == 512:
        Bus_line_info["bus_id: 512"] += 1
    if element.get("bus_id") == 1024:
        Bus_line_info["bus_id: 1024"] += 1

print('Line names and number of stops:')
for element in Bus_line_info:
    print(element+',', 'stops:', Bus_line_info[element])
