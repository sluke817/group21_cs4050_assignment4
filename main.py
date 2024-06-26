import click
from src.graph import UndirectedGraph, MST
from src.prims import prims_algorithm

# simple CLI to allow quick running of the program


@click.command()
@click.option("--graph-file", default="input/graph", help="Input graph file.")
def run_prims(graph_file):

    # initialize original graph from file input
    og_graph = UndirectedGraph()
    num_verticies = 0
    with open(graph_file, "r") as file: # O(e)
        num_verticies = int(file.readline())
        for line in file:
            numbers = [float(num) for num in line.split()]
            try:
                og_graph.update_graph(
                    src_vertex=int(numbers[0]),
                    dst_vertex=int(numbers[1]),
                    weight=numbers[2],
                )
            except KeyError:
                print(f"Error: invalid input line: {line}")

    print("Initial Graph:")
    og_graph.print_graph()

    # run the prims algorithm to build the MST
    mst: MST = prims_algorithm(og_graph, num_verticies)

    print()

    print("MST Edgelist:")
    mst.print_edges()


if __name__ == "__main__":
    run_prims()
