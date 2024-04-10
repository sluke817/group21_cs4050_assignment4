import sys
from .graph import UndirectedGraph
from .key_heap import KeyHeap

# numbers the verticies [0, num_verticies - 1]
def prims_algorithm(graph: UndirectedGraph, num_verticies: int) -> UndirectedGraph:

    mst = UndirectedGraph()

    vertex_heap = KeyHeap()

    mst_set: set[int] = set()  # keep track of all of the verticies already in the MST

    # make list all of the verticies' value with starting "infinite" value
    vertex_values: list[float] = [sys.maxsize] * num_verticies  # O(1)

    # have vertex 1 be the root/starting vertex
    vertex_values[0] = 0  # O(1)

    # init the heap using the desired heap_ini function
    vertex_heap.heap_ini(
        keys=vertex_values, n=num_verticies
    )  # O(vlogv), in reality will only take O(v) since inserting will be O(1) with no heapifying needed

    for _ in range(num_verticies):
        min_vertex = vertex_heap.min_id()  # get the id with the minimum key
        mst_set.add(min_vertex)  # add it to the mst tree set
        vertex_heap.delete_min()  # pop it from the heap, it's been seen
        for adjacent_vertex, weight in graph.get_adjacent_set(
            min_vertex
        ).items():  # get the adjacent verticies and their corresponding weights
            if (
                adjacent_vertex not in mst_set
                and vertex_heap.decrease_key(adjacent_vertex, weight) == True
            ):
                mst.update_graph(
                    src_vertex=min_vertex, dst_vertex=adjacent_vertex, weight=weight
                )  # update graph only if the updated key was actually lower

    return mst
