# pl-graph-animate

## Introduction

The `pl-graph-animate` element is a powerful tool for creating engaging and visually dynamic animations of graph-related problems within the PrairieLearn platform. Designed to aid in the teaching and learning of graph algorithms, this element offers a flexible approach to building animations that showcase how these algorithms operate step-by-step.

`pl-graph-animate` provides two intuitive methods to generate animations:

## Algorithm-Based Animation: 
   Create animations by defining a graph through its adjacency matrix and specifying an algorithm to execute. Currently supported algorithms include:
   - Breadth-First Search (BFS)
   - Depth-First Search (DFS)
   - Dijkstra's Algorithm  

   This method automates the animation process, providing a clear visualization of how the selected algorithm traverses or processes the graph.
   
   **Parameters:**
   -  `params-name="matrix"` : This is the adjacency matrix which will be used to create the graph. The content of the matrix must be declared as a `np.array` in the `server.py` of the question.
   - `algorithm` : Declare which algorithm you wish to executed in the adjacency matrix. (DFS,BFS,Dijkstras). 
        -   If not declared default value = `dfs`.
        - `algorithm = "bfs"`
        -  `algorithm = "dfs"`
        -  `algorithm = "dijkstras"`
   - `frame-duration` : Declare the time each frame will be shown in the video. Declare time in seconds.
        -   If not declared default value = `2` (seconds)
        -  `frame-duration = 5` 
   - `show-steps`: Provide a title to each frame. This title has the following format: `Step {i}: Current Node {current_node} (algorithm)`. It will be displayed at the top of each image of the animation.
        -   If not declared default value = `True`.
        - `show-steps = True` (Display the title in each image)
        - `show-steps = False` (Will not display the title in each image)
    - `show-weights`= Display the weights of the edges of the graph.
        -   If not declared default value = `False`.
        - `show-weights = True` (Display the weights of the edeges)
        - `show-weights = False` (Will not display the weights of the edeges)
    - `directed-graph` : Create a directed graph.
        -   If not declared default value = `False`.
        - `directed-graph = True` (The animation will display a directed graph)
        - `directed-graph = False` (The animation will not  display a directed graph)

**Implementation**
This example is for a animation with a bfs execution on the with all the possible parameters.
- question.html
    

```html
<pl-graph-animate 
    params-type="adjacency-matrix" 
    params-name="matrix" 
    frame-duration="2" 
    algorithm="bfs" 
    show-steps="True" 
    directed-graph="True" 
    show-weights="True">
</pl-graph-animate>
```

- server.py
    - This is how to properly declare the adjacency matrix in the server.py

```python
import prairielearn as pl
import numpy as np

def generate(data):
    mat=np.array([[0, 1, 0, 1, 0],
                         [1, 0, 1, 1, 0],
                         [0, 1, 0, 0, 1],
                         [1, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0]])

    data["params"]["matrix"] = pl.to_json(mat)
```
This example is for a animation with a the minimum amount of necessary parameters to create a animation. This animation will execute the bfs algorithm with a 2 second duration for each frame (step) and will show the title.
```html
<pl-graph-animate 
    params-name="matrix" 
    algorithm="bfs"> 
</pl-graph-animate>
```
- server.py
    - This is how to properly declare the adjacency matrix in the server.py

```python
import prairielearn as pl
import numpy as np

def generate(data):
    mat=np.array([[0, 1, 0, 1, 0],
                         [1, 0, 1, 1, 0],
                         [0, 1, 0, 0, 1],
                         [1, 1, 0, 0, 0],
                         [0, 0, 1, 0, 0]])

    data["params"]["matrix"] = pl.to_json(mat)
```
## Custom Frame-Based Animation  
 Create animations by defining a graph through a python dictionary containing a list of DOT commands. Each step will be a frame in the animation.
 **Parameters**
 - `params-type="dotty"` : Declare that the input of the animation will be a dictionary with DOT commands.
    -   If not declared default value = `adjacency-matrix`. You must declare `params-type="dotty"`
- `params-name="dotty-commands-dictionary"`
    - This is the dictionary which will be used to create the graph. This must be a python dictionary declared in the `server.py` file.
- `frame-duration` : Declare the time each frame will be shown in the video. Declare time in seconds.
        -   If not declared default value = `2` (seconds)
        -  `frame-duration = 5` 

**Implementation**
- question.html
    

```html
    <pl-graph-animate params-type="dotty" params-name="dotty-commands-dictionary" frame-duration=2 ></pl-graph-animate>

    After watching the video, identify which algorithm was used in the graph traversal.
```
- server.py
    - This is how to properly declare the dictionary of DOT Commands.

```python
import prairielearn as pl
import numpy as np

def generate(data):
    

    bfs_dot_commands = {
    "step_1": """
    digraph G {
        label="Step 1: Visit Node 0 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        0 -> 1 [color=black];
        0 -> 2 [color=black];
        0 -> 3 [color=black];
        1 -> 4 [color=black];
        2 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        6 -> 8 [color=black];
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
        0 -> 3 [color=black];
        1 -> 4 [color=black];
        2 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        6 -> 8 [color=black];
    }
    """,
    "step_3": """
    digraph G {
        label="Step 3: Visit Node 2 from Node 0";
        labelloc="top";
        0 [style=filled, fillcolor=red];
        1 [style=filled, fillcolor=red];
        2 [style=filled, fillcolor=red];
        0 -> 1 [color=blue];
        0 -> 2 [color=blue];
        0 -> 3 [color=black];
        1 -> 4 [color=black];
        2 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        6 -> 8 [color=black];
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
        0 -> 2 [color=blue];
        0 -> 3 [color=blue];
        1 -> 4 [color=black];
        2 -> 5 [color=black];
        2 -> 6 [color=black];
        3 -> 7 [color=black];
        6 -> 8 [color=black];
    }
    """
}




    data["params"]["dotty-commands-dictionary"] = pl.to_json(bfs_dot_commands)



```

