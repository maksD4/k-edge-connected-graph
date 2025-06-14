import sys
import networkx as nx
import matplotlib.pyplot as plt
import time

from util import draw_graph, graph_to_json, draw_graph_static_position
from tests import graph_test_greedy, graph_test_dynamic

global pos

#G - input graph
#k - integer
def greedy_algorithm(G, k):
    H = G.copy()

    #array of vertex and their degrees sorted descending
    degrees = sorted(list(G.degree(G.nodes())), key=lambda x: x[1], reverse=True)

    for e in degrees:
        edges = list(H.edges(e[0])) #getting all edges of vertex
        if(H.degree(edges[0][0]) == k):
            break

        for edge in edges:
            if(H.degree(edge[1]) == k):
                continue

            #removing edge 'edge'
            H.remove_edge(edge[0], edge[1])

            #checking if changed graph is still k-edge-connected
            if not nx.is_k_edge_connected(H, k):
                H.add_edge(edge[0], edge[1])

    draw_graph_static_position(H, "greedy", pos)


#modifing input graph by removing edges from changes
def modify_graph(G, changes):
    H = G.copy()
    for e in changes:
        H.remove_edge(e[0], e[1])
    return H

#G - graph
#k - integer
#e - array which contain lists of changes
#h - array of hashes
#current - current list of changes [(v1,v2) , (v2, v3), ...]
def find_edges_to_delete(G, k, e, h, current):
    #applying changes from current
    H = modify_graph(G, current)

    #getting sorted reversed array with node and his degree
    d = sorted(H.degree(), key=lambda x: x[1], reverse=True)

    l = len(e)

    edges = list(H.edges(d[0][0]))

    for edge in edges:
        if(H.degree(edge[1]) == k):
            continue

        H.remove_edge(edge[0], edge[1]) #removing edge to check if is still k-edge-connected
        if(nx.is_k_edge_connected(H, k) and not (nx.weisfeiler_lehman_graph_hash(H) in h)):
            current.append(edge)
            e.append(current.copy())
            current.remove(edge)
            h.append(nx.weisfeiler_lehman_graph_hash(H))
        H.add_edge(edge[0], edge[1]) #restoring to current graph

    #checking if array e has changed
    if(l == len(e)):
        return False

    return True

#(|E| - )!

#G - graph
#k - integer
def dynamic_algorithm(G, k):
    # getting sorted reversed array with node and his degree
    degrees = sorted(list(G.degree(G.nodes())), key=lambda x: x[1], reverse=True)

    edges_queue = []
    hashes = []

    exit = not find_edges_to_delete(G, k, edges_queue, hashes, [])

    depth = 0

    # traversing possible graphs with BFS traversal algorithm and list of graph hashes to avoid replicas
    while(not exit):
        print(f"depth {depth}\nedges_queue {edges_queue}")
        depth += 1

        #print(f"depth {depth}, {len(edges_queue)} combinations, created in {time.time() - start} sec")
        hashes = []

        length = len(edges_queue)
        for i in range(length):
            current_edges = edges_queue.pop(0)
            if (not find_edges_to_delete(G, k, edges_queue, hashes, current_edges)):
                if(not edges_queue and not hashes):
                    H = modify_graph(G, current_edges)
                    draw_graph_static_position(H, "dynamic", pos)
                    exit = True
                    break

if __name__ == "__main__":
    n = int(sys.argv[1]) if (len(sys.argv) > 1) else 6
    p = float(sys.argv[2]) if (len(sys.argv) > 2) else 0.65
    k = int(sys.argv[3]) if (len(sys.argv) > 3) else 2
    file_name = sys.argv[4] if (len(sys.argv) > 4) else "graph.json"
    if(k <= 1 or k > n):
        print("Wrong 3rd argument value")
        exit()

    G = nx.gnp_random_graph(n, p, directed=False)
    pos = nx.spring_layout(G)
    degrees = sorted(list(G.degree(G.nodes())), key=lambda x: x[1], reverse=True)
    for a in degrees:
        print(a)
    draw_graph_static_position(G, "Input graph", pos)

    #graph_test_greedy(30, 8, 100)
    #graph_test_dynamic(7,4, 100)

    if (not nx.is_k_edge_connected(G, k)):
        print(f"Input graph is not {k}-edge-connected")

    else:
        start = time.time()
        greedy_algorithm(G, k)
        print(f"greedy: {time.time() - start}")

        start = time.time()
        dynamic_algorithm(G, k)
        print(f"dynamic: {time.time() - start}")
        graph_to_json(G, file_name)

    plt.show()