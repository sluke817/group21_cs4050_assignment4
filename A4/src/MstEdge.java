public class MstEdge implements Comparable<MstEdge>{
    public int source; // i
    public int dest; // j
    public double weight; // w

    public MstEdge(int s, int d, int w) {
        source = s;
        dest = d;
        weight = w;
    }

    @Override
    public int compareTo(MstEdge o) {
        return Double.compare(weight, o.weight);
    }
}
