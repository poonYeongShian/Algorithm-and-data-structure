""" Heap implemented using an array"""
__author__ = "Brendon Taylor"
__docformat__ = 'reStructuredText'

from typing import Generic
from referential_array import ArrayR, T


class Heap(Generic[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)

    def get_min(self):
        """
        Removes the maximum element from the heap, returning it.
        :pre: Heap is non-empty.
        """
        if self.length == 0:
            raise IndexError

        max_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)

        return max_elt

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1<= k <= self.length
        """
        while k > 1 and self.the_array[k][1] < self.the_array[k // 2][1]:
            # self.swap(k, k // 2)   10/10/2021
            self.the_array[k][0].heap_index, self.the_array[k // 2][0].heap_index = k // 2, k

            self.the_array[k], self.the_array[k // 2] = self.the_array[k // 2], self.the_array[k]
            k = k // 2

    def add(self, element: T) -> bool:
        """
        Swaps elements while rising
        """
        has_space_left = not self.is_full()

        if has_space_left:
            self.length += 1
            # add 10/10/2021 e.g (vertex, 2)
            element[0].heap_index = self.length
            self.the_array[self.length] = element
            # print(self.the_array[self.length], self.length)
            self.rise(self.length)

        return has_space_left

    def rise2(self, k: int, element: T) -> int:
        """
        Rise element at index k to its correct position
        :pre: 1<= k <= self.length
        """
        while k > 1 and element > self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        return k

    def add2(self, element: T) -> bool:
        """
        Alternative implementation using shuffling to create
        a hole to perform only one swap at the end
        """
        has_space_left = not self.is_full()
        if has_space_left:
            self.length += 1
            self.the_array[self.rise2(self.length, element)] = element
        return has_space_left

    def add3(self, element: T) -> bool:
        """
        Combined into one method
        More efficient but less readable
        """
        has_space_left = not self.is_full()

        if has_space_left:
            self.length += 1
            k = self.length
            while k > 1 and element > self.the_array[k // 2]:
                self.the_array[k] = self.the_array[k // 2]
                k = k // 2

            self.the_array[k] = element

        return has_space_left

    def smallest_child(self, k: int) -> int:
        """
        Returns the index of the largest child of k.
        pre: 2*k <= self.length (at least one child)
        """
        #                                   e.g (vertex, 2)
        if 2 * k == self.length or self.the_array[2 * k][1] < self.the_array[2 * k + 1][1]:
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position """
        while 2 * k <= self.length:
            child = self.smallest_child(k)
            if self.the_array[k][1] < self.the_array[child][1]:
                break
            # self.swap(child, k)
            self.the_array[k][0].heap_index, self.the_array[child][0].heap_index = child, k

            self.the_array[k], self.the_array[child] = self.the_array[child], self.the_array[k]
            k = child

    def create_heap(self, max_size: int, an_array: ArrayR[T] = None) -> None:
        """
        If elements are known in advance, they are in an_array
        Assume that max_size=len(an_array) if given
        """
        self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)
        self.length = max_size

        if an_array is not None:
            # copy an_array to self.the_array (shift by 1)
            for i in range(self.length):
                self.the_array[i + 1] = an_array[i]

            # heapify every parent
            for i in range(max_size // 2, 0, -1):
                self.sink(i)

    def update(self, some_vertex, distance):
        k = some_vertex.heap_index
        self.the_array[k] = (some_vertex, distance)
        self.rise(k)

if __name__ == '__main__':
    # items = [int(x) for x in input('Enter a list of numbers: ').strip().split()]
    items = [("ha",4),("ha",3),("ha",1),("ha",7),("ha",5),("ha",6),("ha",9),("ha",6)]
    heap = Heap(len(items))

    for item in items:
        heap.add(item)

    # print(heap.the_array[1])
    # print(heap.the_array[2])
    # print(heap.the_array[3])
    # print(heap.the_array[4])
    # print(heap.the_array[5])
    # print(heap.the_array[6])
    # print(heap.the_array[7])
    while len(heap) > 0:
        print("Get min: " + str(heap.get_min()), " /Number of items : " + str(len(heap)))
