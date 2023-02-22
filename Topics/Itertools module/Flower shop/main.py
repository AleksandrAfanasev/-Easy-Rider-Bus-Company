import itertools


for i in range(1, len(flower_names)):
    print(*list(itertools.combinations(flower_names, i)), sep='\n')
