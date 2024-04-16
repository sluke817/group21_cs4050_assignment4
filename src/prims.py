import sys
from .graph import UndirectedGraph, MST
from .key_heap import KeyHeap, KeyHeapException

# numbers the verticies [0, num_verticies - 1]
def prims_algorithm(graph: UndirectedGraph, num_verticies: int) -> MST:

    vertex_heap = KeyHeap()

    mst_set: set[int] = set()  # keep track of all of the verticies visited in the MST

    # make list all of the verticies' value with starting "infinite" value
    vertex_values: list[float] = [sys.maxsize] * num_verticies  # O(1)

    # have vertex 1 be the root/starting vertex
    vertex_values[0] = 0  # O(1)

    # init the heap using the heap_ini function
    vertex_heap.heap_ini(
        keys=vertex_values, n=num_verticies
    )  # O(vlogv), in reality will only take O(v) since inserting will be O(1) because no heapifying will be occuring

    mst: MST = MST()  # keeps track of the minimum edges to build a spanning tree

    while vertex_heap.size() > 0:  # O(v)
        min_vertex = vertex_heap.min_id()  # get the id with the minimum key O(1)
        mst_set.add(min_vertex)  # add it to the mst tree set O(1)
        vertex_heap.delete_min()  # pop it from the heap, it's now been seen O(logv)
        for adjacent_vertex, weight in graph.get_adjacent_set(
            min_vertex
        ).items():  # get the adjacent verticies and their corresponding weights for each edge, O(e)
            try:
                if adjacent_vertex not in mst_set:
                    if vertex_heap.key(id=adjacent_vertex) > weight:
                        vertex_heap.decrease_key(
                            id=adjacent_vertex, new_key=weight
                        )  # O(logv)
                        mst.update_edge(adjacent_vertex, min_vertex, weight)  # O(1)
            except KeyHeapException:
                pass
    return mst
