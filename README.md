# Finding the minimum k-edge-connected spanning supgraph of G
## Model
### Input data
$`\ G = (V,E) `$ - input graph  
$`\ k \geq 1 `$ - integer  
### Variables
$`\ x_e \in \{0, 1\}, \forall e \in E`$, where  
$`\  x_e = 1:`$ when $`\ e \in E'`$  
$`\  x_e = 0:`$ when $`\ e \notin E'`$  
### Objective function
Minimization of supgraph edges:  
$`\ f = \sum_{e \in E} x_e `$
