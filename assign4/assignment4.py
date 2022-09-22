import math
import copy
from ctypes import py_object
from typing import TypeVar, Generic

T = TypeVar('T')


class ArrayR(Generic[T]):
    """
    This is a Referential array class,
    refer to FIT2085 Week 12 materials
    """
    def __init__(self, length: int) -> None:
        """ Creates an array of references to objects of the given length
        :complexity: O(length) for best/worst case to initialise to None
        :pre: length > 0
        """
        if length <= 0:
            raise ValueError("Array length should be larger than 0.")
        self.array = (length * py_object)()  # initialises the space
        self.array[:] = [None for _ in range(length)]

    def __len__(self) -> int:
        """ Returns the length of the array
        :complexity: O(1)
        """
        return len(self.array)

    def __getitem__(self, index: int) -> T:
        """ Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the object in position index to value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        self.array[index] = value


class Heap(Generic[T]):
    """
    This is a Heap class,
    refer to FIT2085 Week 12 materials
    """
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
            self.the_array[1] = self.the_array[self.length + 1]
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


class Edge:
    """
    This is an Edge class,
    # referred to the lecture recording https://www.youtube.com/watch?v=XF4IRYeIdPU, viewed on 14th Oct 2021
    """
    def __init__(self, u, v, w, d):
        self.u = u
        self.v = v
        self.w = w
        self.weighted = d

    def __str__(self):
        """
        This function display the value of Edge class object when printed
        """
        ret = str(self.u) + "," + str(self.v) + "," + str(self.w) + " weighted: " + str(self.weighted)
        return ret


class Vertex:
    """
    This is a Vertex class,
    # referred to the lecture recording https://www.youtube.com/watch?v=XF4IRYeIdPU, viewed on 14th Oct 2021
    """
    def __init__(self, id):
        self.id = id
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
        # for distance
        self.distance = math.inf
        self.previous = None
        self.heap_index = 0

    def add_edge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        """
        This function display the value of Vertex class object when printed
        """
        ret = ""
        if self.previous is not None:
            ret = str(self.id) + " distance: " + str(self.distance) + "  previous: " + str(self.previous.id)
        else:
            ret = str(self.id) + " distance: " + str(self.distance) + "  previous: " + str(None)

        for edge in self.edges:
            ret = ret + "\n with edges " + str(edge)
        return ret

    def added_to_queue(self):
        self.discovered = True

    def visit_node(self):
        self.visited = True


class WordGraph:
    """
    This is a WordGraph class,
    # referred to the lecture recording https://www.youtube.com/watch?v=XF4IRYeIdPU, viewed on 14th Oct 2021
    """
    def __init__(self, words):
        """
        This function initialize WordGraph class
        :param words: a list words and it contains only lowercase a-z characters, and will all be the same length
            complexity:
                time: O(MN^2), N is the number of item in words, M is the length of each item in words
                auxiliary space: O(K), where K is the number of words
        """
        num_of_vertices = len(words)
        self.vertices = [None] * num_of_vertices

        for i in range(num_of_vertices):
            self.vertices[i] = Vertex(i)

        length_of_every_key = len(words[0])
        edges = []
        # assign edges to the all of the vertices
        for i in range(num_of_vertices):
            for j in range(i, num_of_vertices):
                counter = 0
                distance = 0
                for k in range(length_of_every_key):
                    if words[i][k] != words[j][k]:
                        counter += 1
                        # calculate the alphabetic distances
                        distance = abs(ord(words[j][k]) - ord(words[i][k]))
                # if the number of character between two words is one, then add edges to them
                if counter == 1:
                    edges.append((i, j, 1, distance))
        self.add_edges(edges, False)

    def __str__(self):
        ret = ""
        for vertex in self.vertices:
            ret = ret + "Vertex " + str(vertex) + "\n"
        return ret

    def add_edges(self, argv_edges, is_direct):
        """ Add edges to the vertices"""
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            d = edge[3]
            current_edge = Edge(u, v, w, d)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            if not is_direct:
                current_edge = Edge(v, u, w, d)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def reset_all(self):
        """
        reset all the value of vertices
        """
        for vertex in self.vertices:
            vertex.distance = math.inf
            vertex.discovered = False
            vertex.visited = False
            vertex.heap_index = 0
            vertex.previous = None

    def dijkstra(self, source, destination: Vertex):
        """
        Find the shortest distance between the source and destination
        :param source: source vertex
        :param destination: destination vertex
        :return: shortest distance from source vertex to destination vertex
            complexity:
                time: O(E log V), E is the of edges
                auxiliary space: O(V), V is the number of vertices
        """
        source.distance = 0
        # initialize heap
        discovered = Heap(len(self.vertices))
        discovered.add((source, source.distance))

        while len(discovered) > 0:
            # get min from heap
            u = discovered.get_min()
            u[0].visited = True
            if u[0] is destination:
                return u[0].distance

            # perform edge relaxation on all adjacent vertices
            for edge in u[0].edges:
                v = self.vertices[edge.v]

                if v.discovered == False and v is not source:
                    v.discovered = True      # v is discovered, adding it to heap
                    v.distance = u[1] + edge.weighted
                    v.previous = u[0]
                    discovered.add((v, v.distance))

                if v.visited == False:
                    if v.distance > u[1] + edge.weighted:
                        v.distance = u[1] + edge.weighted
                        v.previous = u[0]
                        discovered.update(v, v.distance)  # Update the v in heap with new distance

    def floyd_warshall(self):
        """
        Floyd-Warshall Algorithm build a matrix of all-pairs shortest distances
        :return: matrix all-pairs shortest distances
            complexity:
                time: O(V^3), V is the number of vertices
                auxiliary space: O(V^2), V is the number of vertices
        """
        count_vertex = len(self.vertices)

        # initialize adjacency matrix the distance from a vertex to itself be 0 and others to be inf
        matrix = [[0 if i == j else math.inf for i in range(count_vertex)] for j in range(count_vertex)]

        # insert the edges into matrix
        for vertex in self.vertices:
            for edge in vertex.edges:
                u = edge.u
                v = edge.v
                w = edge.w
                matrix[u][v] = w

        # perform floyd_warshall algorithm
        for k in range(count_vertex):
            for i in range(count_vertex):
                for j in range(count_vertex):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        return matrix

    def best_start_word(self, target_words):
        """
        Finding the central point between target_words
        :param target_words: target_words is a list of indices of words in the graph.
        :return: the index of the word for which the longest word ladder to any of
                 the words in target_words is as short as possible
            complexity:
                time: O(V^3), V is the number of vertices
                auxiliary space: O(V^2), V is the number of vertices
        """
        # check target_words only contains one target
        if len(target_words) == 1:
            if len(self.vertices[target_words[0]].edges) == 0:
                return target_words[0]
            return target_words[0]

        # create an all pair matrix
        matrix = self.floyd_warshall()
        minimum = math.inf
        max_dist, min_dist = math.inf, math.inf
        index = 0
        # loop through vertices
        for i in range(len(self.vertices)):
            lst = []
            # loop through target words
            for j in target_words:
                # check whether the item exist or the graph is disconnected
                if not 0 <= j <= len(self.vertices):
                    return -1
                if i in target_words:
                    if matrix[i][j] == math.inf:
                        return -1
                lst.append(matrix[i][j])
            temp1 = max(lst)
            temp2 = min(lst)
            # find the distance different between max distance and min distance from a point to other target point
            diff_between_min_max = temp1 - temp2
            if temp1 < min_dist or temp2 < max_dist and diff_between_min_max < minimum:
                min_dist = temp1
                max_dist = temp2
                index = i

            if diff_between_min_max < minimum:
                minimum = diff_between_min_max
                index = i
        return index

    def constrained_ladder(self, start, target, constraint_words):
        """
        This function compute minimum the path taken from start to target and pass through at least one detour.
        :param start: start indices
        :param target: target indices
        :param constraint_words:
        :return: the list of indices of vertices (in order) corresponding to words
                 representing the word ladder which starts with start, ends with end and contains at least one word from constraint_words (it may contain more than one, and
                 the word can appear at any point in the word ladder, including the first or last word)
            complexity:
                time: DlogW + WlogW, D is the number of pairs of words in WordGraph which differ by exactly one letter
                                     W is the number of words in WordGraph
                auxiliary space: O(1)
        """
        minimum = math.inf
        temp = None
        ret = []
        for i in range(len(constraint_words)):
            # get minimum distance from start to detour
            distance_start_to_detour = self.dijkstra(self.vertices[start], self.vertices[constraint_words[i]])
            detour_vertex = copy.deepcopy(self.vertices[constraint_words[i]])
            self.reset_all()

            # get minimum distance from detour to target
            distance_detour_to_end = self.dijkstra(self.vertices[constraint_words[i]], self.vertices[target])
            target_vertex = copy.deepcopy(self.vertices[target])
            self.reset_all()

            # check whether the distances is valid
            if distance_detour_to_end is None or distance_start_to_detour is None:
                if i == len(constraint_words) - 1:
                    return None
            else:
                total_distance = distance_start_to_detour + distance_detour_to_end
                # check whether the distance is minimum compare to other detour
                if total_distance < minimum:
                    minimum = total_distance
                    temp = (detour_vertex, target_vertex)

        # path from start to detour
        current = temp[0]
        ret.insert(0, current.id)
        while current.previous is not None:
            current = current.previous
            ret.insert(0, current.id)

        # path from detour to target
        length_temp = len(ret)
        current = temp[1]
        ret.insert(length_temp, current.id)
        while current.previous is not None:
            current = current.previous
            if current.id != temp[0].id:
                ret.insert(length_temp, current.id)

        return ret





