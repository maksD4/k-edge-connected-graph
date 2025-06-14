import networkx as nx
import matplotlib.pyplot as plt
import simplejson as json

def draw_graph_static_position(G, title, pos):
    plt.figure()
    plt.title(title)
    nx.draw(G, pos, with_labels=True, font_color="white", node_color="blue", node_size=300)
    plt.margins(0.2)

def draw_graph(G, title):
    plt.figure()
    plt.title(title)
    nx.draw(G,  with_labels=True, font_color="white", node_color="blue", node_size=300)
    plt.margins(0.2)

def draw_tests(times):
    plt.plot(times[0], times[1])

def json_to_graph(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)

    return nx.node_link_graph(data)

def graph_to_json(G, file_name):
    data = nx.node_link_data(G, edges="edges")
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)