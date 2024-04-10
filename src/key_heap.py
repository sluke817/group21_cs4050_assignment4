from typing import Any

"""
Notes on KeyHeap and complexity:
    - Type/class used for KeyHeap must implement __gt__ function! (All primitive types already do this, Python does not have compareTo)
    - len() function = O(1)
    - in operator on dictionary has average O(1) time (Python hashes it's dictionaries), where O(n) complexity on lists
    - min() = O(n)
"""

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
        self.heap_arr: list[KeyHeapElement] = []
        self.id_set: dict[int, int] = {}

    def swap(self, indexA, indexB) -> None:  # O(1)
        # update indexes in the id set to allow O(1) access with ID
        self.id_set[self.heap_arr[indexA].id] = indexB
        self.id_set[self.heap_arr[indexB].id] = indexA

        # swap elements
        self.heap_arr[indexA], self.heap_arr[indexB] = (
            self.heap_arr[indexB],
            self.heap_arr[indexA],
        )

    def heapify_down(self, starting_index: int) -> None:  # O(logn)
        # while the parent is larger than the child, swap them
        child_index: int = starting_index
        parent_index: int = int(starting_index // 2) # floor division
        last_index = len(self.heap_arr) - 1

        if (
            child_index < last_index
            and child_index >= 0
            and parent_index >= 0
            and self.heap_arr[child_index].key > self.heap_arr[parent_index].key
        ):
            self.swap(parent_index, child_index)
            self.heapify_down(parent_index)

    def heapify_up(self, starting_index: int = 0) -> None:  # O(logn)
        # while a child is smaller than the parent, swap for largest child
        last_index = len(self.heap_arr) - 1
        smallest_index = starting_index
        left = starting_index * 2
        right = starting_index * 2 + 1

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

        if smallest_index != starting_index:
            self.swap(smallest_index, starting_index)
            self.heapify_up(starting_index=smallest_index)

    def insert(self, key: Any, id: int) -> None:  # O(logn)
        if id not in self.id_set:
            self.id_set[id] = len(self.heap_arr) - 1
            self.heap_arr.append(KeyHeapElement(key=key, id=id))
            self.heapify_down(starting_index=len(self.heap_arr) - 1)
        else:
            raise KeyHeapException("ID already exists in heap!")

    # A4 Doc Functions !!!

    def heap_ini(self, keys: list[Any], n: int) -> None:  # O(nlogn)
        for i in range(len(keys)):
            self.insert(key=keys[i], id=i + 1)

    def in_heap(self, id: int) -> bool:  # O(1)
        return True if id in self.id_set else False

    def min_key(self) -> Any:  # O(1)
        if len(self.heap_arr) > 0:
            return self.heap_arr[0].key
        else:
            return None

    def min_id(self) -> int:  # O(n)
        if len(self.heap_arr) > 0:
            return self.heap_arr[0].id
        else:
            return None

    def key(self, id: int) -> Any:  # O(1)
        if id in self.id_set:
            return self.heap_arr[self.id_set[id]].key
        else:
            raise KeyHeapException("ID does not exist in heap!")

    def delete_min(self) -> None:  # O(logn)
        if len(self.heap_arr) > 0:
            self.swap(0, len(self.heap_arr) - 1)  # swap the first and last element
            self.heap_arr.pop()  # remove the last element
            self.heapify_up(starting_index=0)  # re-heapify the heap

    def decrease_key(self, id: int, new_key: Any) -> bool:  # O(logn)
        if id in self.id_set and self.heap_arr[self.id_set[id]].key > new_key:
            self.heap_arr[self.id_set[id]].key = new_key
            self.swap(
                self.id_set[id], len(self.heap_arr) - 1
            )  # swap element and last element
            self.heapify_down(
                starting_index=len(self.heap_arr) - 1
            )  # heapify from the end
            return True
        else:
            return False
