import time
import networkx as nx
from algorithms import greedy_algorithm, dynamic_algorithm
from util import draw_tests

def single_test_greedy(G, k):
    start = time.time()
    greedy_algorithm(G.copy(), k)
    return time.time() - start

def single_test_dynamic(G, k):
    start = time.time()
    dynamic_algorithm(G, k)
    return time.time() - start

def graph_test_greedy(n, k, iterations):
    times = [[], []]
    print(f"Greedy n={n}, k={k}")
    for p in range(45, 100, 5):
        i = 0
        avg = 0
        while (i < iterations):
            G = nx.gnp_random_graph(n, p / 100, directed=False)
            if (nx.is_k_edge_connected(G, k)):
                avg += single_test_greedy(G, k)
                i += 1

        print(f"{p / 100}\t{avg / iterations}")

        times[0].append(p / 100)
        times[1].append(avg / iterations)
    draw_tests(times)

def graph_test_dynamic(n, k, iterations):
    times = [[], []]
    print(f"Dynamic n={n}, k={k}")
    for p in range(45, 100, 5):
        i = 0
        avg = 0
        while (i < iterations):
            G = nx.gnp_random_graph(n, p / 100, directed=False)
            if (nx.is_k_edge_connected(G, k)):
                avg += single_test_dynamic(G, k)
                i += 1

        print(f"{p / 100}\t{avg / iterations}")

        times[0].append(p / 100)
        times[1].append(avg / iterations)
    draw_tests(times)