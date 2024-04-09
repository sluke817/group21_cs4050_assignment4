
public class MinHeap<T extends Comparable<T>> {
    private class KeyElement implements Comparable<KeyElement>{
        public int id;
        public T key;
        public int current_heap_index;

        public KeyElement(int id_val, T key_val, int index_val) {
            id = id_val;
            key = key_val;
            current_heap_index = index_val;
        }

        @Override
        public int compareTo(KeyElement o) {
            if(o == null) {
                return -1;
            }
            else {
                return key.compareTo(o.key);
            }
        }
    }

    /*
        A heap that follows the structure of parent = n, left = 2n, right = 2n+1
     */
    private KeyElement[] heap_arr;
    /*
        An array to quickly access the key elements of the heap based on ID
     */
    private KeyElement[] indexed_keys;
    private int count;

    private MinHeap(int size) {

    }

    // swaps two elements of the array
    private void swap(int indexA, int indexB) {
        KeyElement tmp = heap_arr[indexA];

        heap_arr[indexA] = heap_arr[indexB];
        heap_arr[indexA].current_heap_index = indexA;

        heap_arr[indexB] = tmp;
        heap_arr[indexB].current_heap_index = indexB;
    }

    // doubles the length of the arr if space runs out
    private void extend_arr() {
        KeyElement[] extended_heap = (KeyElement[]) new Comparable[heap_arr.length * 2];
        System.arraycopy(heap_arr, 0, extended_heap, 0, heap_arr.length); // manual array copy is ugly
        heap_arr = extended_heap;

        KeyElement[] extended_index = (KeyElement[]) new Comparable[indexed_keys.length * 2];
        System.arraycopy(indexed_keys, 0, extended_index, 0, indexed_keys.length);
        indexed_keys = extended_index;
    }

    private void heapify_forwards(int index) {
        int left = 2 * index;
        int right = 2 * index + 1;
        int smallest_index = index;
        int last_index = count - 1;
        if (left <= last_index && heap_arr[left] != null) {
            if(heap_arr[smallest_index] == null || heap_arr[left].key.compareTo(heap_arr[smallest_index].key) < 0) {
                smallest_index = left;
            }
        }
        if (right <= last_index && heap_arr[right] != null) {
            if(heap_arr[smallest_index] == null || heap_arr[right].key.compareTo(heap_arr[smallest_index].key) < 0) {
                smallest_index = right;
            }
        }
        if (smallest_index != index) {
            swap(index, smallest_index);
            heapify_forwards(smallest_index);
        }
    }

    private void heapify_backwards(int index) {
        int parent = (index - 1) / 2;

        while (index > 0 && parent > 0 && heap_arr[index].compareTo(heap_arr[parent]) < 0) {
            swap(index, parent);
            index = parent;
            parent = (index - 1) / 2;
        }
    }

    private void insert(KeyElement key) {
        if(key.id <= count && indexed_keys[key.id] == null) {

        }
    }

    private KeyElement get_key_element(int id) {
        if(id >= 0 && id < count) {
            return indexed_keys[id];
        }
        else {
            throw new IllegalArgumentException("Illegal ID value.");
        }
    }

    // heap_ini
    public MinHeap(T[] keys, int n) {
        indexed_keys = (KeyElement[]) new Comparable[n];
        heap_arr = (KeyElement[]) new Comparable[n];
        for(int i = 0; i < n; i++) {
            KeyElement new_key_element = new KeyElement(i, keys[i], count);
            if (count >= heap_arr.length) {
                extend_arr();
            }
            heap_arr[count] = new_key_element;
            heapify_backwards((count));
            indexed_keys[i] = new_key_element;
            count++;
        }
    }

    public boolean in_heap(int id) {
        return id < count && id >= 0 && indexed_keys[id] != null;
    }

    public T min_key() {
        if(count > 0) {
            return heap_arr[0].key;
        }
        else {
            return null;
        }
    }

    public int min_id() {
        if(count > 0) {
            int index_tracer = 0;
            while(index_tracer < count && indexed_keys[index_tracer] != null) {
                index_tracer++;
            }
            return index_tracer;
        }
        else {
            return -1;
        }
    }

    public T key(int id) {
        T retval = null;
        if(id < count && id >= 0) {
            retval = indexed_keys[id].key;
        }
        return retval;
    }

    public void delete_min() {
        if(count > 0) {
            heap_arr[0] = null;
            heapify_forwards(0);
            count--;
        }
    }

    public void decrease_key(int id, T new_key) {
        KeyElement item = get_key_element(id);
        if (item != null && new_key.compareTo(item.key) < 0) {
            item.key = new_key;
            heapify_backwards(item.current_heap_index);
        }
    }

    public int size() {
        return count;
    }

}
