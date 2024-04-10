import click
from src.graph import UndirectedGraph
from src.prims import prims_algorithm


@click.command()
@click.option("--graph-file", default="input/graph", help="Input graph file.")
def run_prims(graph_file):
    og_graph = UndirectedGraph()
    num_verticies = 0
    with open(graph_file, "r") as file:
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

    mst = prims_algorithm(og_graph, num_verticies)

    print()

    print("MST:")
    mst.print_graph()


if __name__ == "__main__":
    run_prims()
