import networkx as nx
import pygraphviz as pgv
import numpy as np
import prairielearn as pl
import moviepy.editor as mpy
import warnings
import os
import tempfile
import lxml
import base64

# Default parameters
ENGINE_DEFAULT = "dot"
PARAMS_TYPE_DEFAULT = "adjacency-matrix"
DIRECTED_DEFAULT = "False"
DURATION_FRAME_DEFAULT = 2
ALGORITHM_DEFAULT = "dfs"
SHOW_STEPS_DEFAULT="True"
SHOW_WEIGHTS_DEFAULT="False"


"""THIS SECTION CONTAINS THE FUNCTIONS TO GENERATE VIDEO FROM A MATRIX"""

'''def generate_frames_dfs(graph, start_node, show_steps, show_weights):
    frames = []
    visited = set()

    def dfs(node, depth=0, previous_node=None):
        if node in visited:
            return
        visited.add(node)
        # Create frame at each visit using the DFS frame creation function
        frames.append(create_graph_frame_dfs(graph, visited, node, previous_node, depth, show_steps, show_weights))
        for neighbor in graph.neighbors(node):
            dfs(neighbor, depth + 1, node)

    dfs(start_node)
    return frames
def generate_frames_bfs(graph, start_node, show_steps, show_weights):
    frames = []
    visited = set()
    queue = [start_node]
    depth = 0

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            # Create frame at each visit using the BFS frame creation function
            frames.append(create_graph_frame_bfs(graph, visited, current, depth, show_steps, show_weights))
            depth += 1
            queue.extend([neighbor for neighbor in graph.neighbors(current) if neighbor not in visited])
    return frames'''

'''
def create_graph_frame_dfs(graph, visited_nodes, current_node, previous_node, depth, show_steps, show_weights, size="5,5"):
    A = nx.nx_agraph.to_agraph(graph)

    # Set node attributes to color visited nodes and current node
    for node in graph.nodes():
        if node in visited_nodes:
            A.get_node(node).attr['color'] = 'black'
            A.get_node(node).attr['style'] = 'filled'
            A.get_node(node).attr['fillcolor'] = 'green'
        else:
            A.get_node(node).attr['color'] = 'yellow'
            A.get_node(node).attr['penwidth'] = 2.5

    # Color the edge from previous node to current node
    if previous_node is not None and current_node is not None:
        if graph.has_edge(previous_node, current_node):
            A.get_edge(previous_node, current_node).attr['color'] = 'blue'

    # Display weights if enabled
    if show_weights:
        for u, v, data in graph.edges(data=True):
            weight = data.get('weight', 1.0)  # Default weight if not present
            A.get_edge(u, v).attr['label'] = str(weight)

    # Set title and size
    if show_steps:
        A.graph_attr['label'] = f"Step {depth}: Current Node {current_node} (DFS)"
        A.graph_attr['labelloc'] = 'top'
    A.graph_attr['size'] = size  
    A.graph_attr['dpi'] = "300"

    # Save the graph to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    A.draw(temp_file.name, format="png", prog="dot")

    return temp_file.name

def create_graph_frame_bfs(graph, visited_nodes, current_node, depth, show_steps, show_weights, size="5,5"):
    A = nx.nx_agraph.to_agraph(graph)

    # Set node attributes to color visited nodes and current node
    for node in graph.nodes():
        if node in visited_nodes:
            A.get_node(node).attr['color'] = 'black'
            A.get_node(node).attr['style'] = 'filled'
            A.get_node(node).attr['fillcolor'] = 'green'
        else:
            A.get_node(node).attr['color'] = 'yellow'
            A.get_node(node).attr['penwidth'] = 2.5

    # In BFS, the current node can represent the node being processed at the current level
    if current_node is not None:
        A.get_node(current_node).attr['color'] = 'blue'
        A.get_node(current_node).attr['style'] = 'filled'

    # Display weights if enabled
    if show_weights:
        for u, v, data in graph.edges(data=True):
            weight = data.get('weight', 1.0)
            A.get_edge(u, v).attr['label'] = str(weight)

    # Set title and size
    if show_steps:
        A.graph_attr['label'] = f"Step {depth}: Current Node {current_node} (BFS)"
        A.graph_attr['labelloc'] = 'top'
    A.graph_attr['size'] = size  
    A.graph_attr['dpi'] = "300"

    # Save the graph to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    A.draw(temp_file.name, format="png", prog="dot")

    return temp_file.name


def create_graph_frame_matrix(graph, visited_nodes, current_node, depth, show_steps,show_weights,size="5,5"):
    # Create a pygraphviz AGraph object from the NetworkX graph
    A = nx.nx_agraph.to_agraph(graph)

    # Set node attributes to color visited nodes differently
    #color visited nodes
    last_visited_node = None  # Initialize a variable to track the last visited node
    for node in graph.nodes():
        if node in visited_nodes:
            A.get_node(node).attr['color'] = 'black'
            A.get_node(node).attr['style'] = 'filled'
            A.get_node(node).attr['fillcolor'] = 'green'
            
            # Color the edge from the last visited node to the current node
            #if last_visited_node is not None:
             #   A.get_edge(last_visited_node, node).attr['color'] = 'blue'  # Change to desired color for the connecting edge
            
            #last_visited_node = node  # Update the last visited node
        else:
            A.get_node(node).attr['color'] = 'yellow'
            A.get_node(node).attr['penwidth'] = 2.5
    
    if show_weights=="True":
        adjacency_matrix = nx.to_numpy_array(graph) 
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                # Check for valid weights (not zero or excessively large values)
                if i != j and adjacency_matrix[i][j] != 0 and adjacency_matrix[i][j] != 100:
                    edge_label = str(adjacency_matrix[i][j])
                    weight = float(adjacency_matrix[i][j])
                    node1 = list(graph.nodes())[i]
                    node2 = list(graph.nodes())[j]
                    A.add_edge(node1, node2, label=edge_label, weight=weight)
    else:
        pass
    # Set title to indicate the current depth and node
    if show_steps==True:
        A.graph_attr['label'] = f"Step {depth}: Current Node {current_node}"
        A.graph_attr['labelloc'] = 'top'
    else:
        pass
    # Set the size of the graph image
    A.graph_attr['size'] = size  
    A.graph_attr['dpi'] = "300"  

    # Save the graph to a temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    A.draw(temp_file.name, format="png", prog="dot")  # Use 'dot' or another layout engine like 'circo', 'neato'

    return temp_file.name '''
"""THIS SECTION CONTAINS THE FUNCTIONS TO GENERATE VIDEO FROM A MATRIX"""

def generate_frames_bfs_from_matrix(matrix, start_node, show_steps, show_weights,directed, size="5,5"):
    # If matrix is passed, convert to a graph using networkx
    if isinstance(matrix, np.ndarray):  # Check if the input is still a matrix
        #G = nx.from_numpy_array(matrix)
        if directed=="True":
            G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())  # Use DiGraph for directed graphs
        else:
            G = nx.from_numpy_array(matrix)
    else:
        G = matrix  # If it's already a graph, just use it directly

    # Convert the NetworkX graph to a PyGraphviz graph
    A = nx.nx_agraph.to_agraph(G)

    # Get BFS traversal order
    bfs_edges = list(nx.bfs_edges(G, source=start_node))  # List of edges traversed in BFS
    bfs_nodes = list(nx.bfs_tree(G, source=start_node).nodes)  # List of nodes in BFS order

    # List to store frames for the animation
    frames = []

    # Create the animation by incrementally highlighting nodes and edges
    for i in range(1, len(bfs_nodes) + 1):
        # Create a new AGraph object for each frame
        A_temp = A.copy()

        # Highlight nodes in BFS order
        nodes_to_highlight = bfs_nodes[:i]
        for node in nodes_to_highlight:
            A_temp.get_node(node).attr['color'] = 'red'
            A_temp.get_node(node).attr['style'] = 'filled'
            A_temp.get_node(node).attr['fillcolor'] = 'red'

        # Highlight edges in BFS order
        edges_to_highlight = bfs_edges[:i-1]  # Highlight edges based on BFS progression
        for edge in edges_to_highlight:
            A_temp.get_edge(edge[0], edge[1]).attr['color'] = 'blue'
            A_temp.get_edge(edge[0], edge[1]).attr['penwidth'] = 2.5

        # Optionally set the graph title to indicate the current step and node
        if show_steps=="True":
            A_temp.graph_attr['label'] = f"Step {i}: Current Node {bfs_nodes[i-1]} (BFS)"
            A_temp.graph_attr['labelloc'] = 'top'
        else:
            pass

        # Optionally display weights
        if show_weights=="True":
            for u, v, data in G.edges(data=True):
                weight = data.get('weight', 1.0)  # Default weight if not present
                A_temp.get_edge(u, v).attr['label'] = str(weight)
        else:
            pass

        # Set the size of the graph image
        A_temp.graph_attr['size'] = size
        A_temp.graph_attr['dpi'] = "300"

        # Save the graph to a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        A_temp.draw(temp_file.name, format="png", prog="dot")

        # Add the temporary file path to the frames list
        frames.append(temp_file.name)

    return frames


def generate_frames_dfs_from_matrix(matrix, start_node, show_steps, show_weights, directed,size="5,5"):
    # If matrix is passed, convert to a graph using networkx
    if isinstance(matrix, np.ndarray):  # Check if the input is still a matrix
        #G = nx.from_numpy_array(matrix)
        if directed=="True":
            G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())  # Use DiGraph for directed graphs
        else:
            G = nx.from_numpy_array(matrix)
    else:
        G = matrix  # If it's already a graph, just use it directly

    # Convert the NetworkX graph to a PyGraphviz graph
    A = nx.nx_agraph.to_agraph(G)

    # Get DFS traversal order
    dfs_edges = list(nx.dfs_edges(G, source=start_node))  # List of edges traversed in DFS
    dfs_nodes = list(nx.dfs_preorder_nodes(G, source=start_node))  # List of nodes in DFS order

    # List to store frames for the animation
    frames = []

    # Create the animation by incrementally highlighting nodes and edges
    for i in range(1, len(dfs_nodes) + 1):
        # Create a new AGraph object for each frame
        A_temp = A.copy()

        # Highlight nodes in DFS order
        nodes_to_highlight = dfs_nodes[:i]
        for node in nodes_to_highlight:
            A_temp.get_node(node).attr['color'] = 'red'
            A_temp.get_node(node).attr['style'] = 'filled'
            A_temp.get_node(node).attr['fillcolor'] = 'red'

        # Highlight edges in DFS order
        edges_to_highlight = dfs_edges[:i-1]  # Highlight edges based on DFS progression
        for edge in edges_to_highlight:
            A_temp.get_edge(edge[0], edge[1]).attr['color'] = 'blue'
            A_temp.get_edge(edge[0], edge[1]).attr['penwidth'] = 2.5

        # Optionally set the graph title to indicate the current step and node
        if show_steps=="True":
            A_temp.graph_attr['label'] = f"Step {i}: Current Node {dfs_nodes[i-1]} (DFS)"
            A_temp.graph_attr['labelloc'] = 'top'
        else: 
            pass

        # Optionally display weights
        if show_weights=="True":
            for u, v, data in G.edges(data=True):
                weight = data.get('weight', 1.0)  # Default weight if not present
                A_temp.get_edge(u, v).attr['label'] = str(weight)
        else:
            pass

        # Set the size of the graph image
        A_temp.graph_attr['size'] = size
        A_temp.graph_attr['dpi'] = "300"

        # Save the graph to a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        A_temp.draw(temp_file.name, format="png", prog="dot")

        # Add the temporary file path to the frames list
        frames.append(temp_file.name)

    return frames

def generate_frames_dijkstra_from_matrix(matrix, start_node, show_steps, show_weights,directed, size="5,5"):
    if isinstance(matrix, np.ndarray):
        if directed=="True":
            G = nx.from_numpy_array(matrix, create_using=nx.DiGraph())
        else:
            G = nx.from_numpy_array(matrix)
    else:
        G = matrix

    A = nx.nx_agraph.to_agraph(G)

    shortest_paths = nx.single_source_dijkstra_path_length(G, start_node)
    predecessors = nx.single_source_dijkstra_path(G, start_node)

    frames = []
    visited_nodes = set()
    visited_edges = set()

    step_count = 0  # Keep track of step count to reduce number of frames
    for target_node in shortest_paths.keys():
        step_count += 1
        if step_count % 2 != 0:  # Only capture every second step
            continue  # Skip this step to reduce frame count

        A_temp = A.copy()
        path = predecessors[target_node]
        visited_nodes.update(path)
        for node in visited_nodes:
            A_temp.get_node(node).attr['color'] = 'red'
            A_temp.get_node(node).attr['style'] = 'filled'
            A_temp.get_node(node).attr['fillcolor'] = 'red'

        for i in range(len(path) - 1):
            edge = (path[i], path[i + 1])
            visited_edges.add(edge)
            A_temp.get_edge(edge[0], edge[1]).attr['color'] = 'blue'
            A_temp.get_edge(edge[0], edge[1]).attr['penwidth'] = 2.5

        if show_steps=="True":
            A_temp.graph_attr['label'] = f"Target Node {target_node}: Shortest Path (Dijkstra)"
            A_temp.graph_attr['labelloc'] = 'top'
        else:
            pass

        if show_weights=="True":
            for u, v, data in G.edges(data=True):
                weight = data.get('weight', 1.0)
                A_temp.get_edge(u, v).attr['label'] = str(weight)
        else:
            pass

        A_temp.graph_attr['size'] = size
        A_temp.graph_attr['dpi'] = "300"

        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        A_temp.draw(temp_file.name, format="png", prog="dot")
        frames.append(temp_file.name)

    return frames

"""THIS SECTION CONTAINS THE FUNCTIONS TO CREATE A VIDEO FROM A DICTIOANRY OF DOTTY COMMANDS"""
def create_graph_frame_dotty(dot_commands_dict,size="5,5"):
    frames = []
    
    # Loop over the dictionary of DOT commands
    for step, dot_command in dot_commands_dict.items():
        # Create a Pygraphviz AGraph object from the DOT command string
        A = pgv.AGraph(string=dot_command)
        A.graph_attr['size'] = size  
        A.graph_attr['dpi'] = "300"          
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        image_path = temp_file.name
        A.draw(image_path, format="png", prog="dot")  
        frames.append(image_path)
    return frames 



# Function to combine frames into a video
def create_video_from_frames(frames, output_file, frame_duration):
    clips = [mpy.ImageClip(f).set_duration(frame_duration) for f in frames]
    video = mpy.concatenate_videoclips(clips, method="compose")
    
    # Suppress console output by setting verbose=False
    video.write_videofile(output_file, fps=24, verbose=False, logger=None)
def create_weighted_graph(matrix):
    G = nx.Graph()  # Using undirected graph; change to nx.DiGraph() for directed
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            weight = matrix[i][j]
            if weight != 0 and weight != 100:  # Ignore self-loops and large values (representing infinity)
                G.add_edge(chr(65 + i), chr(65 + j), weight=weight)  # Use chr(65 + i) to convert to A, B, C, D, E
    return G

def render(element_html: str, data: pl.QuestionData) -> str:
    # Parse the input parameters
    element = lxml.html.fragment_fromstring(element_html)
    input_param_name = pl.get_string_attrib(element, "params-name")
    input_type = pl.get_string_attrib(element, "params-type", PARAMS_TYPE_DEFAULT)
    algorithm = pl.get_string_attrib(element, "algorithm", ALGORITHM_DEFAULT).lower()  # Select algorithm (dfs/bfs)
    frame_duration = float(pl.get_string_attrib(element, "frame-duration", DURATION_FRAME_DEFAULT))
    show_steps = pl.get_string_attrib(element, "show-steps", SHOW_STEPS_DEFAULT)
    show_weights = pl.get_string_attrib(element, "show-weights", SHOW_WEIGHTS_DEFAULT)
    directed_graph=pl.get_string_attrib(element, "directed-graph", DIRECTED_DEFAULT)
    # Create video for input type adjacency-matrix
    if input_type==PARAMS_TYPE_DEFAULT:
        matrix = np.array(pl.from_json(data["params"][input_param_name]))
        

        start_node = 0  # Assuming traversal starts at node 0
        if algorithm == "dfs":
            #G = nx.from_numpy_array(matrix, create_using=nx.DiGraph() if pl.get_boolean_attrib(element, "directed", DIRECTED_DEFAULT) else nx.Graph())
            #G = create_weighted_graph(matrix)
            #frames = generate_frames_dfs(G, start_node,show_steps,show_weights)
            frames=generate_frames_dfs_from_matrix(matrix, start_node,show_steps,show_weights,directed_graph)
        elif algorithm == "bfs":
            #G = nx.from_numpy_array(matrix, create_using=nx.DiGraph() if pl.get_boolean_attrib(element, "directed", DIRECTED_DEFAULT) else nx.Graph())
            #frames = generate_frames_bfs(G, start_node,show_steps,show_weights)
            frames=generate_frames_bfs_from_matrix(matrix, start_node,show_steps,show_weights,directed_graph)
        elif algorithm == "dijkstra":
            #G = nx.from_numpy_array(matrix, create_using=nx.DiGraph() if pl.get_boolean_attrib(element, "directed", DIRECTED_DEFAULT) else nx.Graph())
            #frames = generate_frames_bfs(G, start_node,show_steps,show_weights)
            frames=generate_frames_dijkstra_from_matrix(matrix, start_node,show_steps,show_weights,directed_graph)

        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    
    # Create video for input type dotty
    elif input_type=="dotty":
        dot_commands_dict = pl.from_json(data["params"][input_param_name])
        frames = create_graph_frame_dotty(dot_commands_dict)
        output_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
    
    
    
    
    # Save the video to a temporary file
    output_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
    create_video_from_frames(frames, output_file, frame_duration)

    # Read the video file and encode it in base64
    with open(output_file, "rb") as video_file:
        video_base64 = base64.b64encode(video_file.read()).decode('utf-8')

    
    return f'<video controls  width="100" height="100"><source src="data:video/mp4;base64,{video_base64}" type="video/mp4"></video>'
