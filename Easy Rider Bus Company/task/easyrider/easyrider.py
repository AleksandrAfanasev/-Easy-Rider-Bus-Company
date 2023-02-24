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

cnt = 0

print('Arrival time test:')

if len(lines[0]) > 0:
    i = 0
    for i in range(0, len(lines[0]) - 1):
        if lines[0][i + 1].get("a_time") < lines[0][i].get("a_time"):
            print('bus_id line 128: wrong time on station', lines[0][i + 1].get("stop_name"))
            cnt += 1
            break
        else:
            continue

if len(lines[1]) > 0:
    i = 0
    for i in range(0, len(lines[1]) - 1):
        if lines[1][i + 1].get("a_time") < lines[1][i].get("a_time"):
            print('bus_id line 256: wrong time on station', lines[1][i + 1].get("stop_name"))
            cnt += 1
            break
        else:
            continue

if len(lines[2]) > 0:
    i = 0
    for i in range(0, len(lines[2]) - 1):
        if lines[2][i + 1].get("a_time") < lines[2][i].get("a_time"):
            print('bus_id line 512: wrong time on station', lines[2][i + 1].get("stop_name"))
            cnt += 1
            break
        else:
            continue

if len(lines[3]) > 0:
    i = 0
    for i in range(0, len(lines[3]) - 1):
        if lines[3][i + 1].get("a_time") < lines[3][i].get("a_time"):
            print('bus_id line 1024: wrong time on station', lines[3][i + 1].get("stop_name"))
            cnt += 1
            break
        else:
            continue

if cnt == 0:
    print('OK')
