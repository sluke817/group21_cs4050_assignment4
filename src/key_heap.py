from typing import Any

# Helper classes


class KeyHeapException(Exception):
    def __init__(self, message="Invalid operation on KeyHeap"):
        self.message = message
        super().__init__(self.message)


class KeyHeapElement:
    def __init__(self, key, id):
        self.key = key
        self.id = id

    def __str__(self):
        return f"ID: {self.id}, Key: {self.key}"


class KeyHeap:

    # Helper functions

    def __init__(self):
        self.heap_arr: list[KeyHeapElement] = []  # heap array representation
        self.id_set: dict[
            int, int
        ] = (
            {}
        )  # keeps track of the id value and the current index of the id in the heap (allows key() to have O(1) access time)

    def swap(self, heapIndexA, heapIndexB) -> None:  # O(1)
        # update indexes in the id set
        self.id_set[self.heap_arr[heapIndexA].id] = heapIndexB
        self.id_set[self.heap_arr[heapIndexB].id] = heapIndexA

        # swap elements
        tmp = self.heap_arr[heapIndexA]
        self.heap_arr[heapIndexA] = self.heap_arr[heapIndexB]
        self.heap_arr[heapIndexB] = tmp

    def print_heap(self): # debugging helper
        print("Current heap order: ")
        for element in self.heap_arr:
            print(element)

        print(f"ID set: {self.id_set}")

    def size(self):
        return len(self.heap_arr)

    def heapify_down(self, starting_index: int) -> None:  # O(logn)
        # while the parent is larger than the child, swap them
        child_index: int = starting_index
        parent_index: int = int(starting_index // 2)  # floor division
        last_index = len(self.heap_arr) - 1

        # if the parent is larger, swap and keep heapifying towards start
        if (
            child_index < last_index
            and child_index >= 0
            and parent_index >= 0
            and self.heap_arr[child_index].key < self.heap_arr[parent_index].key
        ):
            self.swap(parent_index, child_index)
            self.heapify_down(parent_index)

    def heapify_up(self, starting_index: int = 0) -> None:  # O(logn)
        # while a child is smaller than the parent, swap for largest child
        last_index = len(self.heap_arr) - 1
        smallest_index = starting_index
        left = starting_index * 2
        right = starting_index * 2 + 1

        # find the smallest of the 3 (parent, left, right)
        if (
            smallest_index <= last_index
            and left <= last_index
            and self.heap_arr[smallest_index].key > self.heap_arr[left].key
        ):
            smallest_index = left
        if (
            smallest_index <= last_index
            and right <= last_index
            and self.heap_arr[smallest_index].key > self.heap_arr[right].key
        ):
            smallest_index = right

        # if smallest is not the parent (starting_index), swap for smallest and keep heapifying
        if smallest_index != starting_index:
            self.swap(smallest_index, starting_index)
            self.heapify_up(starting_index=smallest_index)

    def insert(self, key: Any, id: int) -> None:  # O(logn)
        # put it at the end, then heapify from end
        if id not in self.id_set:
            self.id_set[id] = len(self.heap_arr)
            self.heap_arr.append(KeyHeapElement(key=key, id=id))
            self.heapify_down(starting_index=len(self.heap_arr) - 1)
        else:
            raise KeyHeapException("ID already exists in heap!")

    # A4 Doc Functions !!!

    def heap_ini(self, keys: list[Any], n: int) -> None:  # O(nlogn)
        for i in range(len(keys)):  # O(n)
            self.insert(key=keys[i], id=i + 1)  # O(logn)

    def in_heap(self, id: int) -> bool:  # O(1)
        return True if id in self.id_set else False

    def min_key(self) -> Any:  # O(1)
        if len(self.heap_arr) > 0:
            return self.heap_arr[0].key
        else:
            return None

    def min_id(self) -> int:  # O(1)
        if len(self.heap_arr) > 0:
            return self.heap_arr[0].id
        else:
            return None

    def key(self, id: int) -> Any:  # O(1)
        if id in self.id_set:
            return self.heap_arr[self.id_set[id]].key
        else:
            raise KeyHeapException(f"ID {id} does not exist in heap!")

    def delete_min(self) -> None:  # O(logn)
        if len(self.heap_arr) > 0:
            self.swap(0, len(self.heap_arr) - 1)  # swap the first and last element
            deleted_element = self.heap_arr.pop()  # remove the last element
            self.id_set.pop(deleted_element.id)  # remove from index set
            self.heapify_up(starting_index=0)  # re-heapify the heap

    def decrease_key(self, id: int, new_key: Any) -> None:  # O(logn)
        # update only if smaller, then bubble the smallest to the front of the heap
        if id in self.id_set:
            if new_key < self.heap_arr[self.id_set[id]].key:
                self.heap_arr[self.id_set[id]].key = new_key
                self.heapify_down(
                    starting_index=self.id_set[id]
                )  # heapify down to beginning of heap
        else:
            raise KeyHeapException(f"ID {id} does not exist in heap!")
