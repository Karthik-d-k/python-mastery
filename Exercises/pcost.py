pcost = 0.0

with open("../Data/portfolio.dat") as f:
    for line in f.readlines():
        line = line.split()
        pcost += int(line[1]) * float(line[2])

print(pcost)
