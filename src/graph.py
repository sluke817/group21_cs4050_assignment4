# Graph structure to assist in simplifying graph logic


class Edge:
    def __init__(self, dst: int, src: int, weight: float):
        self.dst = dst
        self.src = src
        self.weight = weight


class GraphExeption(Exception):
    def __init__(self, message="An invalid graph operation occured!"):
        self.message = message
        super().__init__(self.message)


class UndirectedGraph:
    def __init__(self):
        self.vertex_set: dict[int, dict[int, float]] = {}
        self.edge_list: list[Edge] = []

    def __contains__(self, vertex_num: int):  # O(1)
        return vertex_num in self.vertex_set

    def update_graph(self, src_vertex: int, dst_vertex: int, weight: float):  # O(1)
        if src_vertex not in self.vertex_set:
            self.vertex_set[src_vertex] = {}
        self.vertex_set[src_vertex][dst_vertex] = weight

        if dst_vertex not in self.vertex_set:
            self.vertex_set[dst_vertex] = {}
        self.vertex_set[dst_vertex][src_vertex] = weight

        self.edge_list.append(Edge(dst=dst_vertex, src=src_vertex, weight=weight))

    def get_adjacent_set(self, vertex_num: int) -> dict[int, float]:  # O(1)
        try:
            return self.vertex_set[vertex_num]
        except KeyError:
            raise GraphExeption(f"Vertex {vertex_num} not in graph!")

    def get_edge_weight(self, src: int, dst: int):
        try:
            return self.vertex_set[src][dst]
        except KeyError:
            raise GraphExeption(f"Error in retrieving weight for {src}-{dst}")

    def print_graph(self):  # O(v)
        print("Vertex\tAdjacent")
        for vertex, adjacent_list in self.vertex_set.items():
            print(f"{vertex}\t{adjacent_list}")

    def print_edges(self):
        print(f"Number of Edges: {len(self.edge_list)}")
        print("Edge\tWeight")
        for edge in self.edge_list:
            print(f"{edge.src}-{edge.dst}\t{edge.weight}")

    def print_mst(self, parent_dict: dict[int, int]) -> None:
        print(f"Number of Edges: {len(parent_dict)}")
        print("Edge\tWeight")
        for src, dst in parent_dict.items():
            print(f"{src}-{dst}\t{self.vertex_set[src][dst]}")


class MST:
    def __init__(self):
        self.edge_dict = {}

    def update_edge(self, va, vb, w) -> None:
        self.edge_dict[va] = (vb, w)

    def print_edges(self):
        print(f"Number of Edges: {len(self.edge_dict)}")
        print("Edge\tWeight")
        for va in self.edge_dict:
            print(f"{va}-{self.edge_dict[va][0]}\t{self.edge_dict[va][1]}")
