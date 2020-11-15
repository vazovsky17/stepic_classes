mapa = {i: [] for i in range(1, 12)}

with open('file.txt') as file:
    while True:
        x = file.readline().strip().replace('\t', ' ')
        if x == '':
            break
        x = x.split()
        mapa[int(x[0])].append(int(x[2]))

data = ''
for k, v in mapa.items():
    if len(v) == 0:
        data += f'{k} -\n'
    else:
        data += f'{k} {sum(v)/len(v)}\n'
print(data)

with open('new.txt', 'w') as new:
    new.write(data)
