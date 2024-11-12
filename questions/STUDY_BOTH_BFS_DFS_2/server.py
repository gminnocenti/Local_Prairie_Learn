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
        1 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        5 -> 8 [color=black];
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
        1 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        5 -> 8 [color=black];
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
        1 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        5 -> 8 [color=black];
    }
    """,
    "step_4": """
    digraph G {
        label="Step 4: Visit Node 7 from Node 3";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=black];
        1 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=blue];
        5 -> 8 [color=black];
    }
    """,
    "step_5": """
    digraph G {
        label="Step 5: Backtrack to Node 1, then Visit Node 4";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=blue];
        1 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=blue];
        5 -> 8 [color=black];
    }
    """,
    "step_6": """
    digraph G {
        label="Step 6: Visit Node 5 from Node 1";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        5 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=blue];
        1 -> 5 [color=blue];
        2 -> 6 [color=black];
        3 -> 7 [color=blue];
        5 -> 8 [color=black];
    }
    """,
    "step_7": """
    digraph G {
        label="Step 7: Visit Node 8 from Node 5";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        5 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        8 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=black];
        1 -> 3 [color=blue];
        1 -> 4 [color=blue];
        1 -> 5 [color=blue];
        2 -> 6 [color=black];
        3 -> 7 [color=blue];
        5 -> 8 [color=blue];
    }
    """,
    "step_8": """
    digraph G {
        label="Step 8: Backtrack to Node 0, then Visit Node 2";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        5 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        8 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=blue];
        1 -> 3 [color=blue];
        1 -> 4 [color=blue];
        1 -> 5 [color=blue];
        2 -> 6 [color=black];
        3 -> 7 [color=blue];
        5 -> 8 [color=blue];
    }
    """,
    "step_9": """
    digraph G {
        label="Step 9: Visit Node 6 from Node 2";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        5 [style=filled, fillcolor=red];
        6 [style=filled, fillcolor=red];
        7 [style=filled, fillcolor=red];
        8 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=blue];
        1 -> 3 [color=blue];
        1 -> 4 [color=blue];
        1 -> 5 [color=blue];
        2 -> 6 [color=blue];
        3 -> 7 [color=blue];
        5 -> 8 [color=blue];
    }
    """
}




    data["params"]["dotty-commands-dictionary"] = pl.to_json(dfs_dot_commands)



