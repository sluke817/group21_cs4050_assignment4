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
        if(weight < o.weight) {
            return -1;
        } else if (weight > o.weight) {
            return 1;
        }
        else {
            return 0;
        }
    }
}
