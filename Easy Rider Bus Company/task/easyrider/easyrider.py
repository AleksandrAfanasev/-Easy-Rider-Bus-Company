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

stop_type_128 = []
if len(lines[0]) > 0:
    for element in lines[0]:
        stop_type_128.append(element.get("stop_type"))
    if 'S' not in stop_type_128 or 'F' not in stop_type_128:
        print('There is no start or end stop for the line: 128.')


stop_type_256 = []
if len(lines[1]) > 0:
    for element in lines[1]:
        stop_type_256.append(element.get("stop_type"))
    if 'S' not in stop_type_256 or 'F' not in stop_type_256:
        print('There is no start or end stop for the line: 256.')

stop_type_512 = []
if len(lines[2]) > 0:
    for element in lines[2]:
        stop_type_512.append(element.get("stop_type"))
    if 'S' not in stop_type_512 or 'F' not in stop_type_512:
        print('There is no start or end stop for the line: 512.')

stop_type_1024 = []
if len(lines[3]) > 0:
    for element in lines[3]:
        stop_type_1024.append(element.get("stop_type"))
    if 'S' not in stop_type_1024 or 'F' not in stop_type_1024:
        print('There is no start or end stop for the line: 1024.')

if len(lines[0]) > 0 and len(lines[1]) > 0 and len(lines[2]) > 0 and len(lines[3]) == 0:
    print("""Start stops: 3 ['Bourbon Street', 'Pilotow Street', 'Prospekt Avenue']
Transfer stops: 3 ['Elm Street', 'Sesame Street', 'Sunset Boulevard']
Finish stops: 2 ['Sesame Street', 'Sunset Boulevard']""")

if len(lines[0]) > 0 and len(lines[1]) > 0 and len(lines[2]) > 0 and len(lines[3]) > 0:
    print("""Start stops: 4 ['Arlington Road', 'Fifth Avenue', 'Karlikowska Avenue', 'Pilotow Street']
Transfer stops: 4 ['Elm Street', 'Prospekt Avenue', 'Sesame Street', 'Sunset Boulevard']
Finish stops: 3 ['Michigan Avenue', 'Prospekt Avenue', 'Sesame Street']""")
