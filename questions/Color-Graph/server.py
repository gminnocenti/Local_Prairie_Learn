import prairielearn as pl
import numpy as np

def generate(data):
    dot_commands_dict = {
    "step_1": """
    digraph G {
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
    """,
    "step_5": """
    digraph G {
        A [style=filled, fillcolor=red];
        B [style=filled, fillcolor=blue];
        C [style=filled, fillcolor=green];
        D [style=filled, fillcolor=yellow];
        E [style=filled, fillcolor=purple];
        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> A;
    }
    """
}



    data["params"]["dotty-commands-dictionary"] = pl.to_json(dot_commands_dict)

