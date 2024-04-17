# Notes about Python time complexity
- len() function = O(1)
- in operator on dictionary has average O(1) time (Python hashes it's dictionaries), where O(n) complexity on lists

# KeyHeap Analysis

## Structure 
Group 21's KeyHeap implements the heap described in the A4 doc. The group utilizes an array to implement a miniumum heap based on key values. The heap mirrors a tree structure with parent=n, left=2n, right=2n+1 where n is an abitrary index. The structure also utilizes a dictionary to keep track of ID's and their current key value index in the heap array. 

## Time Complexity
Accessing any key from an ID [key()] or checking if an ID exists [in_heap()] in the heap both take O(1) time due to the ID dictionary. Minimum key [min_key()] and minimum key ID [min_id()] both take O(1) access time due to array heap structure. Updating a key [decrease_key()] or deleting the minimum [delete_min()] both have O(log(n)) complexity due to heapify algorithms bubbling a minimum key to the front of the array or larger key back to the end with heapify_up and heapify_down. Both heapify operations have a single branching factor and due to the heap's two child structure it will always reach the end or root in log(n) time. Initilizing a heap based on a list of keys [heap_ini()] has O(nlog(n)) complexity due to iterating over each key (n) and inserting each into the heap where an insertion runs a heapify operation (with complexity log(n)).


# Prim's Algorithm Analysis with the KeyHeap

Group 21's implementation of Prim's algorithm uses the aforementioned KeyHeap to keep track of verticies and their current lowest weighted edge. We represent the number of verticies as v and the edges as e.

## Reading the graph from the file: O(e)
First we have to read in the graph from the file line by line, where each line represents an edge between to verticies. Doing this takes O(e) time.

## Disaplying initial graph: O(ve)
We display the initial graph as an adjacent list before running Prims algorithm which results in displaying each vertex and it's adjacent verticies (connected by edges). This process takes O(v + e) time due to having to iterate over each vertex and all of it's adjacent edges

## Initializing the heap: O(v)
When building the heap, we provide a list of key values with each key `FLOAT_MAX` except for a single vertex initialized to zero and inserted first in the list. Using the KeyHeap's init function [heap_ini()] will only take O(v) complexity due to all values but one value being the same, and since the zero value will be inserted first, no heapifying will happen and only insertions into the array occur.

## Iterating over all verticies and popping from the heap: O(vlogv)
All verticies must be visited. We pop the minimum value from the heap and mark it as visited. Since the pop algorithm from KeyHeap takes a log(n) time, and we pop each vertex, this process results in a O(vlogv) time complexity

## Iterating over a vertex's adjacent verticies: O(elogv)
Once popped from the heap, we check each of the edges in the adjacent vertex list. We decrease the key values of the adjacent verticies accordingly based on the new weight discovered from the popped vertex. Since we have to check each edge and decreasing the vertex value in the minimum KeyHeap takes O(logv) time, we result in an O(elogv) time for this process.

## Displaying the final MST: O(e)
After running the algorithm, we display the graph in an appropriate format which requires iterating over all edges in the MST. This takes O(e) time.



