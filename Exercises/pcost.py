def portfolio_cost(filename):
    pcost = 0.0

    with open(filename) as f:
        for line in f.readlines():
            line = line.split()
            try:
                pcost += int(line[1]) * float(line[2])
            except ValueError as e:
                print(f"Couldn't parse: {line}\n{e}")

    return pcost


print(portfolio_cost("../Data/portfolio3.dat"))
