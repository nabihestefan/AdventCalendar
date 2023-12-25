import networkx as nx
files = ['input.txt', 'inputTest.txt']
with open(files[0], 'r') as f:
    data = [x.strip() for x in f.readlines()]

nodes = set()
edges = set()
for line in data:
    node, conns = line.split(": ")
    nodes.add(node)
    for conn in conns.split(" "): edges.add(tuple(sorted([node, conn])))

def run(nodes, edges):
    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)

    cut = nx.minimum_edge_cut(g)

    for edge in cut: g.remove_edge(*edge)

    total = 1
    for c in nx.connected_components(g): total *= len(c)

    return total
            
print("Part 1: ", run(nodes, edges))