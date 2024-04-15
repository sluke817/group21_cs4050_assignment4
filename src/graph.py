# # Graph structure to assist in simplifying graph logic
#
# class GraphExeption(Exception):
#     def __init__(self, message="An invalid graph operation occured!"):
#         self.message = message
#         super().__init__(self.message)
#
#
# class UndirectedGraph:
#     def __init__(self):
#         self.vertex_set: dict[int, dict[int, float]] = {}
#
#     def __contains__(self, vertex_num: int): # O(1)
#         return vertex_num in self.vertex_set
#
#     def update_graph(self, src_vertex: int, dst_vertex: int, weight: float): # O(1)
#         if src_vertex not in self.vertex_set:
#             self.vertex_set[src_vertex] = {}
#         self.vertex_set[src_vertex][dst_vertex] = weight
#
#         if dst_vertex not in self.vertex_set:
#             self.vertex_set[dst_vertex] = {}
#         self.vertex_set[dst_vertex][src_vertex] = weight
#
#     def get_adjacent_set(self, vertex_num: int) -> dict[int, float]: # O(1)
#         try:
#             return self.vertex_set[vertex_num]
#         except KeyError:
#             raise GraphExeption(f"Vertex {vertex_num} not in graph!")
#
#     def print_graph(self): # O(v)
#         print("Vertex\tAdjacent")
#         for vertex, adjacent_list in self.vertex_set.items():
#             print(f"{vertex}\t{adjacent_list}")


import networkx as nx
import matplotlib.pyplot as plt

class GraphExeption(Exception):
    def __init__(self, message="An invalid graph operation occurred!"):
        self.message = message
        super().__init__(self.message)

class UndirectedGraph:
    def __init__(self):
        self.vertex_set = {}

    def __contains__(self, vertex_num):
        return vertex_num in self.vertex_set

    def update_graph(self, src_vertex, dst_vertex, weight):
        if src_vertex not in self.vertex_set:
            self.vertex_set[src_vertex] = {}
        self.vertex_set[src_vertex][dst_vertex] = weight

        if dst_vertex not in self.vertex_set:
            self.vertex_set[dst_vertex] = {}
        self.vertex_set[dst_vertex][src_vertex] = weight

    def get_adjacent_set(self, vertex_num):
        try:
            return self.vertex_set[vertex_num]
        except KeyError:
            raise GraphExeption(f"Vertex {vertex_num} not in graph!")

    def visualize_graph(self):
        G = nx.Graph()
        for src_vertex, adj_vertices in self.vertex_set.items():
            for dst_vertex, weight in adj_vertices.items():
                G.add_edge(src_vertex, dst_vertex, weight=weight, width=10.0)

        pos = nx.spring_layout(G)  # positions for all nodes
        nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def print_graph(self): # O(v)
        print("Vertex\tAdjacent")
        for vertex, adjacent_list in self.vertex_set.items():
            print(f"{vertex}\t{adjacent_list}")

# # Example usage
# graph = UndirectedGraph()
#
# # Read graph from file
# graph_file = "/Users/lukedomalewski/Desktop/On Google Drive/Mizzou/2024 Spring/CS_4050/Assignments/assignment 4/input/graph"
#
#
# with open(graph_file, "r") as file:
#     next(file)  # Skip the first line
#     for line in file:
#         src_vertex, dst_vertex, weight = map(float, line.split())
#         graph.update_graph(src_vertex, dst_vertex, weight)
#
# graph.visualize_graph()


