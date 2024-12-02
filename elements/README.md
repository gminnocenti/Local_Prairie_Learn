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
   -  `params-name="matrix"` : This is the adjacency matrix which will be used to create the graph. The context of the matrix must be declared as a `np.array` in the `server.py` of the question.
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
This example is for a animation with a the minimum amount of necessary parameters to create a animation.
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
   For users seeking complete control, this method allows you to define animations frame-by-frame using a dictionary of DOT commands. This approach is ideal for creating highly customized or unconventional graph visualizations tailored to specific needs.

