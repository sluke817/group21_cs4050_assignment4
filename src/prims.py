import sys
from .graph import UndirectedGraph
from .key_heap import KeyHeap

# numbers the verticies [0, num_verticies - 1]
def prims_algorithm(graph: UndirectedGraph, num_verticies: int) -> UndirectedGraph:

    mst = UndirectedGraph() # just use another "graph" to represent the tree

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

    for _ in range(num_verticies): # O(v)
        min_vertex = vertex_heap.min_id()  # get the id with the minimum key O(1)
        mst_set.add(min_vertex)  # add it to the mst tree set O(1)
        vertex_heap.delete_min()  # pop it from the heap, it's been seen O(logv)
        for adjacent_vertex, weight in graph.get_adjacent_set( 
            min_vertex
        ).items():  # get the adjacent verticies and their corresponding weights, O(e)
            if (
                adjacent_vertex not in mst_set
                and vertex_heap.decrease_key(adjacent_vertex, weight) == True # O(logv)
            ): # only update the graph if we haven't visited the vertex yet AND the key is actually lower than we thought it was. If so, it'll be deacreased to the new weight and we can add it to the MST 
                mst.update_graph(
                    src_vertex=min_vertex, dst_vertex=adjacent_vertex, weight=weight
                )  # update graph only if the updated key was actually lower O(1)

    return mst
