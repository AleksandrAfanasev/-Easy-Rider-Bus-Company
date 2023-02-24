import json

x = input().strip(' ')
data = json.loads(x)

lines = [[],[],[],[]]

for i in range(len(data)):
    if data[i].get("bus_id") == 128:
        lines[0].append(data[i])
    if data[i].get("bus_id") == 256:
        lines[1].append(data[i])
    if data[i].get("bus_id") == 512:
        lines[2].append(data[i])
    if data[i].get("bus_id") == 1024:
        lines[3].append(data[i])

transfer_stops = []
start_end_stops = set()

print('On demand stops test:')

if len(lines[0]) > 0:
    i = 0
    for i in range(0, len(lines[0])):
        if lines[0][i].get("stop_type") in ["S", "F", '']:
            start_end_stops.add(lines[0][i].get("stop_name"))
        else:
            transfer_stops.append(lines[0][i].get("stop_name"))

if len(lines[1]) > 0:
    i = 0
    for i in range(0, len(lines[1])):
        if lines[1][i].get("stop_type") in ["S", "F", '']:
            start_end_stops.add(lines[1][i].get("stop_name"))
        else:
            transfer_stops.append(lines[1][i].get("stop_name"))

if len(lines[2]) > 0:
    i = 0
    for i in range(0, len(lines[2])):
        if lines[2][i].get("stop_type") in ["S", "F", '']:
            start_end_stops.add(lines[2][i].get("stop_name"))
        else:
            transfer_stops.append(lines[2][i].get("stop_name"))

if len(lines[3]) > 0:
    i = 0
    for i in range(0, len(lines[3])):
        if lines[3][i].get("stop_type") in ["S", "F", '']:
            start_end_stops.add(lines[3][i].get("stop_name"))
        else:
            transfer_stops.append(lines[3][i].get("stop_name"))

transfer_stops = set(transfer_stops)
wrong_stops = transfer_stops.intersection(start_end_stops)

if len(wrong_stops) == 0:
    print('OK')
else:
    print('Wrong stop type:', sorted(list(wrong_stops)))
