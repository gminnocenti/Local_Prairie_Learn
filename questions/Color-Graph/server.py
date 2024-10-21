import io
import matplotlib.pyplot as plt
import pygraphviz as pgv
from PIL import Image
from matplotlib.animation import PillowWriter

def file(data):
    # Extract filename from data["filename"]
    if data["filename"] == "graph_animation.gif":
        # Define your dot commands as a dictionary
        dot_commands_dict = {
            "step_1": """
            digraph G {
                A [style=filled, fillcolor=red];
                A -> B;
                B -> C;
                C -> D;
                D -> E;
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
            }
            """,
            "ste5": """
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
            }
            """
        }

        # Create a figure for displaying images
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('on')

        # Initialize writer for GIF output, with 0.5 fps for 1 frame every 2 seconds
        writer = PillowWriter(fps=0.5)  # 0.5 frames per second = 1 frame every 2 seconds
        with writer.saving(fig, "graph_animation.gif", 100):
            for i, (step, dot_code) in enumerate(dot_commands_dict.items(), start=1):
                # Create a graph from the dot commands
                A_temp = pgv.AGraph(string=dot_code)

                # Create a BytesIO object to store the image in memory
                png_bytes = io.BytesIO()

                # Draw the graph directly to the BytesIO object
                A_temp.draw(png_bytes, format='png', prog='dot')

                # Seek back to the beginning of the BytesIO object
                png_bytes.seek(0)

                # Open the image with Pillow directly from BytesIO
                img = Image.open(png_bytes)

                # Display the image on the Matplotlib axis
                ax.imshow(img)
                writer.grab_frame()
                ax.clear()

        # Read the GIF file and return it as a byte stream
        with open("graph_animation.gif", 'rb') as f:
            buf = io.BytesIO(f.read())

        return buf
