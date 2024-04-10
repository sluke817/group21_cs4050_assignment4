class GraphExeption(Exception):
    def __init__(self, message="An invalid graph operation occured!"):
        self.message = message
        super().__init__(self.message)


class UndirectedGraph:
    def __init__(self):
        self.vertex_set: dict[int, dict[int, float]] = {}

    def __contains__(self, vertex_num: int):
        return vertex_num in self.vertex_set

    def update_graph(self, src_vertex: int, dst_vertex: int, weight: float):
        if src_vertex not in self.vertex_set:
            self.vertex_set[src_vertex] = {}
        self.vertex_set[src_vertex][dst_vertex] = weight

        if dst_vertex not in self.vertex_set:
            self.vertex_set[dst_vertex] = {}
        self.vertex_set[dst_vertex][src_vertex] = weight

    def get_adjacent_set(self, vertex_num: int) -> dict[int, float]:
        try:
            return self.vertex_set[vertex_num]
        except KeyError:
            raise GraphExeption(f"Vertex {vertex_num} not in graph!")

    def print_graph(self):
        print("Vertex\tAdjacent")
        for vertex, adjacent_list in self.vertex_set.items():
            print(f"{vertex}\t{adjacent_list}")
