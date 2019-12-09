import re


def buildtree(node):
    for sputnik in [pair[1] for pair in orbits if pair[0] == node[0]]:
        node[1].append([sputnik, [], node])
        buildtree(node[1][-1])


def findnode(node, name):
    if node[0] == name:
        return node
    else:
        for subnode in node[1]:
            sn = findnode(subnode, name)
            if sn:
                return sn
        return None


def countorbits(node, depth):
    s = 0
    for subnode in node[1]:
        s += countorbits(subnode, depth+1)
    return s + depth


def nodeorbits(node):
    return [node[2][0]] + nodeorbits(node[2]) if node[2] else []


f = open('input6.txt', 'r')
ft = ''.join(f.readlines())
orbits = re.findall(r'(\w+)\)(\w+)', ft)

tree = ['COM', [], None]
buildtree(tree)
print(countorbits(tree, 0))

santa = findnode(tree, 'SAN')
me = findnode(tree, 'YOU')

santaorbits = set(nodeorbits(santa))
myorbits = set(nodeorbits(me))
mutualorbits = santaorbits.intersection(myorbits)

print(len(santaorbits) + len(myorbits) - 2*len(mutualorbits))

