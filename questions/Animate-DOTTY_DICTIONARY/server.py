import prairielearn as pl
import numpy as np

def generate(data):
    dot_commands_dict ={
    "step_0": """
    graph G {
        label="Step 0: Initial State (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=white, pos="92,99!"];
        1 [style=filled, fillcolor=white, pos="18,45!"];
        2 [style=filled, fillcolor=white, pos="48,35!"];
        3 [style=filled, fillcolor=white, pos="57,27!"];
        4 [style=filled, fillcolor=white, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_1": """
    graph G {
        label="Step 1: Current Node 0 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=white, pos="18,45!"];
        2 [style=filled, fillcolor=white, pos="48,35!"];
        3 [style=filled, fillcolor=white, pos="57,27!"];
        4 [style=filled, fillcolor=white, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_2": """
    graph G {
        label="Step 2: Current Node 1 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=red, pos="18,45!"];
        2 [style=filled, fillcolor=white, pos="48,35!"];
        3 [style=filled, fillcolor=white, pos="57,27!"];
        4 [style=filled, fillcolor=white, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_3": """
    graph G {
        label="Step 3: Current Node 2 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=red, pos="18,45!"];
        2 [style=filled, fillcolor=red, pos="48,35!"];
        3 [style=filled, fillcolor=white, pos="57,27!"];
        4 [style=filled, fillcolor=white, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_4": """
    graph G {
        label="Step 4: Current Node 3 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=red, pos="18,45!"];
        2 [style=filled, fillcolor=red, pos="48,35!"];
        3 [style=filled, fillcolor=red, pos="57,27!"];
        4 [style=filled, fillcolor=white, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_5": """
    graph G {
        label="Step 5: Current Node 4 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=red, pos="18,45!"];
        2 [style=filled, fillcolor=red, pos="48,35!"];
        3 [style=filled, fillcolor=red, pos="57,27!"];
        4 [style=filled, fillcolor=red, pos="59,42!"];
        5 [style=filled, fillcolor=white, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """,
    "step_6": """
    graph G {
        label="Step 6: Current Node 5 (BFS)";
        labelloc="t";
        0 [style=filled, fillcolor=red, pos="92,99!"];
        1 [style=filled, fillcolor=red, pos="18,45!"];
        2 [style=filled, fillcolor=red, pos="48,35!"];
        3 [style=filled, fillcolor=red, pos="57,27!"];
        4 [style=filled, fillcolor=red, pos="59,42!"];
        5 [style=filled, fillcolor=red, pos="80,60!"];
        0 -- 1 [label="4"];
        1 -- 2 [label="5"];
        2 -- 3 [label="7"];
        3 -- 4 [label="3"];
        4 -- 5 [label="2"];
    }
    """
}




    dot_commands_dict_2 = {
    "step_1": """
    digraph G {
        label="Step 1";
        labelloc="top";
        A [style=filled, fillcolor=red];
        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> A;
    }
    """,
    "step_2": """
    digraph G {
        label="Step 2";
        labelloc="top";
        A [style=filled, fillcolor=red];
        B [style=filled, fillcolor=blue];
        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> A;
    }
    """,
    "step_3": """
    digraph G {
        label="Step 3";
        labelloc="top";
        A [style=filled, fillcolor=red];
        B [style=filled, fillcolor=blue];
        C [style=filled, fillcolor=green];
        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> A;
    }
    """,
    "step_4": """
    digraph G {
        label="Step 4";
        labelloc="top";
        A [style=filled, fillcolor=red];
        B [style=filled, fillcolor=blue];
        C [style=filled, fillcolor=green];
        D [style=filled, fillcolor=yellow];
        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> A;
    }
    """
}
    bfs_wrong_execution_dot_commands = {
    "step_1": """
    digraph G {
        label="Step 1: Visit Node 0 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        0 -> 1 [color=black];
        0 -> 3 [color=black];
        1 -> 2 [color=black];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_2": """
    digraph G {
        label="Step 2: Visit Node 1 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=black];
        1 -> 2 [color=black];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_3": """
    digraph G {
        label="Step 3: Visit Node 2 from Node 1";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=black];
        1 -> 2 [color=blue];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,

    "step_4": """
    digraph G {
        label="Step 4: Visit Node 3 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_5": """
    digraph G {
        label="Step 5: Visit Node 4 from Node 3";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        3 -> 4 [color=blue];
        2 -> 4 [color=black];
    }
    """,
    "step_6": """
    digraph G {
        label="Step 6: Visit Node 4 from Node 2";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        3 -> 4 [color=blue];
        2 -> 4 [color=blue];
    }
    """
}

    bfs_dot_commands = {
    "step_1": """
    digraph G {
        label="Step 1: Visit Node 0 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        0 -> 1 [color=black];
        0 -> 3 [color=black];
        1 -> 2 [color=black];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_2": """
    digraph G {
        label="Step 2: Visit Node 1 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=black];
        1 -> 2 [color=black];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_3": """
    digraph G {
        label="Step 3: Visit Node 3 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=black];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_4": """
    digraph G {
        label="Step 4: Visit Node 2 from Node 1";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        2 -> 4 [color=black];
        3 -> 4 [color=black];
    }
    """,
    "step_5": """
    digraph G {
        label="Step 5: Visit Node 4 from Node 3";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        3 -> 4 [color=blue];
        2 -> 4 [color=black];
    }
    """,
    "step_6": """
    digraph G {
        label="Step 6: Visit Node 4 from Node 2";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        3 [style=filled, fillcolor=red];
        4 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 3 [color=blue];
        1 -> 2 [color=blue];
        3 -> 4 [color=blue];
        2 -> 4 [color=blue];
    }
    """
}

    data["params"]["dotty-commands-dictionary"] = pl.to_json(bfs_dot_commands)

    data["params"]["dotty-commands-dictionary2"] = pl.to_json(bfs_wrong_execution_dot_commands)


