# Finding the Minimum k-Edge-Connected Spanning Subgraph of G

## Problem description
The problem is to find a minimal k-edge-connected spanning subgraph of a graph G. A connected graph is k-edge-connected if it remains connected whenever fewer than k edges are removed.

### Implemented algorithms
This repository implements two types of algorithms to solve this problem: greedy algorithm and dynamic algorithm. The greedy algorithm is fast and may find a minimal k-edge-connected graph, while the dynamic algorithm always finds the optimal solution at the cost of increased computation time.

## Model

### Input data
$`\ G = (V,E) `$ - input graph  
$`\ k \geq 1 `$ - integer  
### Variables
$`\ x_e \in \{0, 1\}, \forall e \in E`$, where  
$`\  x_e = 1:`$ when $`\ e \in E'`$  
$`\  x_e = 0:`$ when $`\ e \notin E'`$  
### Objective function
Minimization of subgraph edges:  
$`\ f = \sum_{e \in E} x_e `$
### Constraints
  - Subgraph $`\ H = (V_H, E_H)`$, where $`\ V_H = V`$  and $`\ E_H = \{e \in E:x_e = 1 \}`$  
  - $`\ \forall v \in V_H `$  $`\ deg(v) \ge k `$
  - $`\ (H' = (V_H, E_H \setminus X) `$ $`\ \land `$ $`\ \forall{|X| < k} `$ $`\ X \subseteq E_H) \to `$ graph H is k-edge-connected

## Visualization of results
Visualization of the greedy algorithm's solution and the output for a graph generated using the `gnp_random_graph` function from the NetworkX library, with 8 vertices and an edge probability of 75%. 
### Input graph  
![alt text](https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/input1.png)
### Greedy algorithm outcome (not optimal)
![alt text](https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/greedy1.png)
### Dynamic algorithm outcome
![alt text](https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/dynamic1.png)

## Visualization of dynamic algorithm search
As an example, we will use a graph generated by the gnp generator from the networkx library with parameters $`\ n=6 `$ $`\ p=0.65 `$ $`\ k=2 `$   

<p float="left">
  <img src="https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/dynamic_viz_input.png" width="45%" />
  <img src="https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/dynamic_viz_dynamic.png" width="45%" />
</p>    

The algorithm starts with the vertex of highest degree. It checks all possible edges for removal, ensuring that the set has not already been considered and that the graph remains **k**-edge-connected after their removal.  

![alt text](https://github.com/maksD4/k-edge-connected-graph/blob/main/readme/img.png)
