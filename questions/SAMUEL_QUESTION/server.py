import networkx as nx
import random
import json

def generate(data):
    # Generate a random weighted graph
    def generate_random_weighted_graph(num_nodes, num_edges, weight_range=(1, 10)):
        G = nx.Graph()
        for i in range(num_nodes):
            G.add_node(i)
        for _ in range(num_edges):
            u = random.randint(0, num_nodes - 1)
            v = random.randint(0, num_nodes - 1)
            if u != v:
                weight = random.randint(*weight_range)
                G.add_edge(u, v, weight=weight)
        return G

    # Assign random fixed positions to each node
    def assign_fixed_positions(G):
        positions = {}
        for node in G.nodes():
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            positions[node] = f"{x},{y}!"
        return positions

    # Generate Dotty commands with potential traversal error
    def dijkstra_dotty_steps_with_error_fixed(G, source, positions, error_chance=0.7):
        # Run Dijkstra's algorithm from the source node to determine expected order
        path_lengths, _ = nx.single_source_dijkstra(G, source)
        expected_order = sorted(path_lengths.keys(), key=lambda x: path_lengths[x])

        # Identify reachable nodes from the source
        reachable_nodes = set(nx.node_connected_component(G, source))

        # Initialize a custom traversal sequence
        custom_visited_order = [source]
        visited_nodes = set(custom_visited_order)
        
        # Track if we introduced an error and the step number of the first error
        error_introduced = False
        error_step_number = 0
        dot_commands_dict = {}

        # Create the initial frame with only the source node highlighted
        initial_step = 'graph G {\n'
        initial_step += '    label="Step 1";\n'
        initial_step += '    labelloc="t";\n'
        for n in G.nodes():
            color = "red" if n == source else "white"
            initial_step += f'    {n} [style=filled, fillcolor={color}, pos="{positions[n]}"];\n'
        for u, v, data in G.edges(data=True):
            weight = data['weight']
            initial_step += f'    {u} -- {v} [label="{weight}"];\n'
        initial_step += '}\n'
        dot_commands_dict["step_1"] = initial_step

        # Traverse nodes according to Dijkstra’s (with potential forced errors)
        step_counter = 2  # Start step counter from 2 for subsequent frames
        for idx, correct_node in enumerate(expected_order[1:], start=1):
            current_node = custom_visited_order[-1]
            neighbors = [n for n in G.neighbors(current_node) if n not in visited_nodes]

            if not neighbors:
                break

            correct_next_node = min(neighbors, key=lambda n: path_lengths.get(n, float('inf')))
            if random.random() < error_chance and len(neighbors) > 1:
                incorrect_choices = [n for n in neighbors if n != correct_next_node]
                if incorrect_choices:
                    next_node = incorrect_choices[0]
                    if not error_introduced:
                        error_step_number = step_counter
                    error_introduced = True
                else:
                    next_node = correct_next_node
            else:
                next_node = correct_next_node

            custom_visited_order.append(next_node)
            visited_nodes.add(next_node)

            # Check if the traversal has diverged from expected order
            if next_node != correct_node and not error_introduced:
                error_step_number = step_counter
                error_introduced = True

            # Dotty code generation
            step_name = f"step_{step_counter}"
            dotty_code = 'graph G {\n'
            dotty_code += f'    label="Step {step_counter}";\n'
            dotty_code += '    labelloc="t";\n'
            for n in G.nodes():
                color = "red" if n in custom_visited_order else "white"
                dotty_code += f'    {n} [style=filled, fillcolor={color}, pos="{positions[n]}"];\n'
            for u, v, data in G.edges(data=True):
                weight = data['weight']
                dotty_code += f'    {u} -- {v} [label="{weight}"];\n'
            dotty_code += '}\n'
            dot_commands_dict[step_name] = dotty_code

            step_counter += 1

        # Additional frames to ensure all nodes in reachable_nodes are marked
        remaining_reachable_nodes = [n for n in reachable_nodes if n not in visited_nodes]
        for node in remaining_reachable_nodes:
            visited_nodes.add(node)
            step_name = f"step_{step_counter}"
            dotty_code = 'graph G {\n'
            dotty_code += f'    label="Step {step_counter}";\n'
            dotty_code += '    labelloc="t";\n'
            for n in G.nodes():
                color = "red" if n in visited_nodes else "white"
                dotty_code += f'    {n} [style=filled, fillcolor={color}, pos="{positions[n]}"];\n'
            for u, v, data in G.edges(data=True):
                weight = data['weight']
                dotty_code += f'    {u} -- {v} [label="{weight}"];\n'
            dotty_code += '}\n'
            dot_commands_dict[step_name] = dotty_code
            step_counter += 1
        return dot_commands_dict, error_introduced, error_step_number

    # Parameters for the random graph
    num_nodes = 5   # Number of nodes
    num_edges = 7   # Number of edges
    weight_range = (1, 10)  # Range of weights

    # Generate a random weighted graph
    G = generate_random_weighted_graph(num_nodes, num_edges, weight_range)

    # Specify the source node for Dijkstra's algorithm
    source = 0

    # Assign fixed positions to nodes
    positions = assign_fixed_positions(G)

    # Generate dotty commands with potential traversal error
    dot_commands_dict, error_introduced, error_step_number = dijkstra_dotty_steps_with_error_fixed(G, source, positions)

    # Write whether an error was introduced and its step number to a JSON file
    output_data = {
        "error_introduced": error_introduced,
        "error_step_number": error_step_number if error_introduced else 0
    }
    with open("traversal_info.json", "w") as json_file:
        json.dump(output_data, json_file)

    # Add Dotty commands dictionary to data for use in PrairieLearn
    data["correct_answers"]["step"] = str(error_step_number)
    data["params"]["dotty-commands-dictionary"] = dot_commands_dict

def grade(data):
    sub = data["submitted_answers"].get("step", "")
    if sub == data["correct_answers"]["step"]:
        data["score"] = 1
    else:
        data["score"] = 0
