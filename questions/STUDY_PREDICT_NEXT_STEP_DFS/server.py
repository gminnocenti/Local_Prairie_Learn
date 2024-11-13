import prairielearn as pl
import numpy as np

def generate(data):
    

    dfs_dot_commands = {
    "step_1": """
    digraph G {
        label="Step 1: Start DFS at Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        0 -> 1 [color=black];
        0 -> 2 [color=black];
        1 -> 3 [color=black];
        1 -> 4 [color=black];
        2 -> 6 [color=black];
        2 -> 7 [color=black];
        3 -> 5 [color=black];
    }
    """,
    "step_2": """
    digraph G {
        label="Step 2: Visit Node 1 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=black];
        1 -> 4 [color=black];
        2 -> 6 [color=black];
        2 -> 7 [color=black];
        3 -> 5 [color=black];
    }
    """,
    "step_3": """
    digraph G {
        label="Step 3: Visit Node 3 from Node 1";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=black];
        2 -> 6 [color=black];
        2 -> 7 [color=black];
        3 -> 5 [color=black];
    }
    """,
    "step_4": """
    digraph G {
        label="Step 4: Visit Node 5 from Node 3";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        5 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=black];
        2 -> 6 [color=black];
        2 -> 7 [color=black];
        3 -> 5 [color=blue];
    }
    """
}




    data["params"]["dotty-commands-dictionary"] = pl.to_json(dfs_dot_commands)



