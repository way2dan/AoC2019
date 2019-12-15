def get_data ():
    f = open('input14.txt', 'r')
    r = []
    for line in f.readlines():
        b = []
        line = line.strip('\n')
        i = line.find('=>')
        d = {}
        for a in line[:i-1].split(','):
            a = a.strip(' ')
            chem = a.split(' ')[1]
            num = a.split(' ')[0]
            d[chem] = int(num)
        b.append(d)
        a = line[i+2:].strip(' ')
        chem = a.split(' ')[1]
        num = a.split(' ')[0]
        b.append(chem)
        b.append(int(num))
        r.append(b)
    return r


def find_chem_in_chain_of_parents(reactions, chain_of_chem, chem2find):
    if chem2find == chain_of_chem:
        return True
    r = find_reaction_produced_chem(reactions, chain_of_chem)
    if not r:
        return False
    for chem in r[0]:
        if find_chem_in_chain_of_parents(reactions, chem, chem2find):
            return True
    return False


def find_reaction_produced_chem(reactions, chem):
    for r in reactions:
        if r[1] == chem:
            return r
    return None


def number_of_ore(n):
    reactions = get_data()
    demand = {'FUEL': n}
    while True:
        for d in demand:
            if d == 'ORE':
                continue
            flag = True
            for chem in demand:
                if chem != d:
                    if find_chem_in_chain_of_parents(reactions, chain_of_chem=chem, chem2find=d):
                        flag = False
            if not flag:
                continue
            r = find_reaction_produced_chem(reactions, d)

            needed_amount = demand[d]
            k = (needed_amount // r[2]) if (needed_amount % r[2] == 0) else (needed_amount // r[2]) + 1
            for chem in r[0]:
                if chem in demand:
                    demand[chem] += k * r[0][chem]
                else:
                    demand[chem] = k * r[0][chem]
            reactions.remove(r)
            del demand[d]
            break
        if len(demand) == 1:
            break
    return demand['ORE']


def number_of_fuel(n0, n1, N):
    print((n1-n0)//2)
    s0 = number_of_ore(n0)
    sn = number_of_ore(n0+1)
    sh = number_of_ore((n0+n1)//2)
    if s0 < N < sn:
        return n0
    if s0 < N and sh < N:
        return number_of_fuel((n0+n1)//2, n1, N)
    else:
        return number_of_fuel(n0, (n0 + n1) // 2, N)


print(number_of_ore(1))

print(number_of_fuel(1, 5000000, 1000000000000))



