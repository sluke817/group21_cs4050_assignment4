import java.util.ArrayList;
import java.util.List;

public class PrimsAlgorithm {

    public static List<MstEdge> primsMST(MstEdge[] edge_list, int vertices_count) {
        MinHeap edge_heap = new MinHeap(edge_list, edge_list.length);
        List<MstEdge> MST = new ArrayList<>();

        boolean[] in_mst = new boolean[vertices_count]; // index corresponds to verticies' number - 1

        while(edge_heap.size() > 0) {
            MstEdge smallest_edge = (MstEdge) edge_heap.min_key();
            if(!in_mst[smallest_edge.dest]) {
                MST.add(smallest_edge);
                in_mst[smallest_edge.dest] = true;
                for(MstEdge edge : graph.get(smallest_edge.dest)) {

                }
            }
        }


    }


}
