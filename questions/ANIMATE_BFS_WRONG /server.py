import networkx as nx
import random
import json
import random
import numpy as np
import prairielearn as pl

def generate(data):
    matrix = np.array([
    [0, 1, 0, 1, 0],  # Node 0 has edges to Node 1 and Node 3
    [1, 0, 1, 0, 0],  # Node 1 has edges to Node 0 and Node 2
    [0, 1, 0, 0, 1],  # Node 2 has edges to Node 1 and Node 4
    [1, 0, 0, 0, 1],  # Node 3 has edges to Node 0 and Node 4
    [0, 0, 1, 1, 0]   # Node 4 has edges to Node 2 and Node 3
])


    # Add Dotty commands dictionary to data for use in PrairieLearn
    data["params"]["matrix"] = pl.to_json(matrix)