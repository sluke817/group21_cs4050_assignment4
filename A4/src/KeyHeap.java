import java.security.Key;

public class KeyHeap <T extends Comparable<T>> {
    private class KeyElement implements Comparable<KeyElement>{
        public int id;
        public T key;

        public KeyElement(int i, T k) {
            key = k;
            id = i;
        }

        @Override
        public int compareTo(KeyElement o) {
            return key.compareTo(o.key);
        }
    }

    private KeyElement[] heap_arr;
    private int count;

    // swaps two elements of the array
    private void swap(int indexA, int indexB) {
        KeyElement tmp = heap_arr[indexA];
        heap_arr[indexA] = heap_arr[indexB];
        heap_arr[indexB] = tmp;
    }

    // doubles the length of the arr if space runs out
    private void extend_arr() {
        KeyElement[] extended_arr = (KeyElement[]) new Comparable[heap_arr.length * 2];
        System.arraycopy(heap_arr, 0, extended_arr, 0, heap_arr.length); // manual array copy is ugly
        heap_arr = extended_arr;
    }

    private void heapify_from_end(int index) {
        int parent = (index - 1) / 2;

        while (index > 0 && heap_arr[index].compareTo(heap_arr[parent]) < 0) {
            swap(index, parent);
            index = parent;
            parent = (index - 1) / 2;
        }
    }

    private void insert(KeyElement key) {
        if(count >= heap_arr.length) {
            extend_arr();
        }
        heap_arr[count] = key;
        heapify_from_end((count));
        count++;
    }

    private KeyElement get_element(int id) {
        for(KeyElement item: heap_arr) {
            if(item.id == id) {
                return item;
            }
        }
        return null;
    }

    public void heap_ini(T[] keys, int n) {
        for(int i = 0; i < n; i++) {
            insert(new KeyElement(i, keys[i]));
        }
    }

    public boolean in_heap(int id) {
        for(KeyElement item : heap_arr) {
            if(id == item.id) {
                return true;
            }
        }
        return false;
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
            int min_id = heap_arr[0].id;
            for (int i = 1; i < heap_arr.length; i++) {
                if (heap_arr[i].id < min_id) {
                    min_id = heap_arr[i].id;
                }
            }
            return min_id;
        }
        else {
            return 0;
        }
    }



    public T key(int id) {
        KeyElement item = get_element(id);
        if(item != null) {
            return item.key;
        }
        else {
            return null;
        }
    }

    // basically shift all to the left 1 unit
    public void delete_min() {
        if(count > 1) {
            for(int i = 0; i < count - 1; i++) {
                heap_arr[i] = heap_arr[i+1];
            }
            count--;
        }
        else if(count == 1) {
            heap_arr[0] = null;
            count = 0;
        }
    }

    public void decrease_key(int id, T new_key) {
        KeyElement item = get_element(id);
        if(item != null && item.key.compareTo(new_key) < 0) {
            item.key = new_key;
        }
    }

    public int size() {
        return count;
    }

}
