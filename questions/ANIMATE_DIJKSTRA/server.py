import prairielearn as pl
import numpy as np

def generate(data):
    mat=([[0, 10, 0, 30, 100],
                   [10, 0, 50, 0, 0],
                   [0, 50, 0, 20, 10],
                   [30, 0, 20, 0, 60],
                   [100, 0, 10, 60, 0]])

    data["params"]["matrix"] = pl.to_json(mat)