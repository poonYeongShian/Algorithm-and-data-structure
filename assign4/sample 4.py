"""
File for Question 1 and 2 of FIT2004 S1/2021 Assignment 4
"""
__author__ = "Chan Wai Han"

from typing import List, Tuple
import heapq

# Graph class
# this is an adjacency list
class Graph:
    """ Class called Graph.
    
    Non-abstract class called Graph which initializes a graph.
    
    Constants: None
    
    Non-abstract methods:
        __init__ initializes a graph.
        __str__ returns a string describing the graph.
        reset resets the values in the graph.
        add_edges adds edges to the vertices of the graph.
        dijkstra performs the dijkstra algorithm.
        
    Abstract methods:
        None
    """
    def __init__(self, V: List[int]) -> None:
        """ Initializes a graph as an adjacency list.

        Arguments:
            V (List[int]): the vertices to be added into the graph.
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            vertices: a list of vertices to be added into the graph.
        
        Returns:
            None
            
        Complexity:
            Best-case: O(N), where N is the number of vertices.
            Worst-case: O(N), where N is the number of vertices.
        """
        # array
        self.vertices = [None] * len(V)
        for i in range(len(V)):
            self.vertices[i] = Vertex(V[i])
                
    def __str__(self) -> str:
        """ Returns a string describing the graph.

        Arguments:
            None
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            return_string: a string describing the graph.

        Returns:
            str: return_string, a string describing the graph.
            
        Complexity:
            Best-case: O(N), where N is the number of vertices.
            Worst-case: O(N), where N is the number of vertices.
        """
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + "\n"
        return return_string
    
    def reset(self) -> None:
        """ Resets the values in the graph.

        Complexity:
            Best-case: O(N), where N is the number of vertices.
            Worst-case: O(N), where N is the number of vertices.
        """
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = 0
            vertex.previous = None
    
    def add_edges(self, argv_edges: List[Tuple[int, int, int]], argv_direct:bool=True) -> None:
        """ Adds edges to the vertices of the graph.

        Arguments:
            argv_edges (List[Tuple[int, int, int]]): the edges to be added to the vertex
            argv_direct (bool, optional): boolean value to determine if graph is directed or undirected.
                                          Defaults to True.
        
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            u: source vertex
            v: destination vertex
            w: weight of vertex (cost)

        Returns:
            None
            
        Complexity:
            Best-case: O(N), where N is the number of edges.
            Worst-case: O(N), where N is the number of edges.
        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            # add u to v
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            if not argv_direct:
                # add v to u
                current_edge = Edge(v,u,w)
                current_vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)
                
    def dijkstra(self, n: int, source, destination) -> Tuple[int, List[int]]:
        """ Performs the dijkstra algorithm.

        Raises:
            None
            
        Constants:
            None
            
        Variables:
            counter: a counter
            discovered: min heap of discovered vertices
            path: list of cities travelled
            cost: cost at a city

        Arguments:
            n (int): the number of vertices in the graph.
            source (Vertex): the source vertex.
            destination (Vertex): the destinataion vertex.

        Returns:
            Tuple[int, List[int]]: cost of delivery and list representing cities travelled.
        
        Complexity:
            Best-case: O(Rlog(N)), where R is the total number of roads (edges),
                       and N is the totala number of cities (vertices)
                       Serving and heapifying uses log(N) time.
                       Iterating through each edge of a vertex takes up O(R).
            Worst-case: O(Rlog(N)), where R is the total number of roads (edges),
                        and N is the totala number of cities (vertices)
                        Serving and heapifying uses log(N) time.
                        Iterating through each edge of a vertex takes up O(R).
        """
        counter = 0
        source.distance = 0
        discovered = []    # min heap
        path = []
        discovered.append((source.distance, counter, source))
        counter += 1
        heapq.heapify(discovered)
        while len(discovered) > 0:
            # serve from
            u = heapq.heappop(discovered)[2]
            u.visited = True
            if u == destination:
                cost = u.distance
                path.insert(0, u.id)
                begin = u.previous
                while begin != source and begin != None:
                    path.insert(0, begin.id)
                    begin = begin.previous
                if begin != None:
                    path.insert(0, begin.id)
                return (cost, path)
            # perform edge relaxation on all adjacent vertices
            for edge in u.edges:
                v = self.vertices[edge.v]
                if v.discovered == False:    # means distance is still \inf
                    v.discovered = True    # means I have discovered v, adding it to queue
                    v.distance = u.distance + edge.w
                    v.previous = u
                    discovered.append((v.distance, counter, v))
                    counter += 1
                    heapq.heapify(discovered)
                # it is in heap, but not yet finalize
                if v.visited == False:
                    # find a shorter route, change it
                    if v.distance > u.distance + edge.w:
                        # update distance
                        v.distance = u.distance + edge.w
                        v.previous = u
                        # update heap
                        for i in range(len(discovered)):
                            if discovered[i][2] == v:
                                discovered[i] = (v.distance, counter, v)
                                counter += 1
                        heapq.heapify(discovered)
        
class Vertex:
    """ Class called Vertex.
    
    Non-abstract class called Vertex which initializes a vertex in a graph.
    
    Constants: None
    
    Non-abstract methods:
        __init__ initializes a vertex.
        __str__ returns a string describing the vertex.
        add_edge adds an edge to the vertex.
        
    Abstract methods:
        None
    """
    def __init__(self, id: int) -> None:
        """ Initializes a graph as an adjacency list.

        Arguments:
            id (int): the vertex id
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            id: the vertex id
            edges: the edges of the vertex
            discovered: used for traversal, if vertex has been discovered
            visited: used for traversal, if vertex has been visited
            distance: essentially the weight total from previous vertex to current vertex
            previous: previous vertex that added the weight to the current vertex
        
        Returns:
            None
            
        Complexity:
            Best-case: O(1)
            Worst-case: O(1)
        """
        self.id = id
        # list
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
        # distance
        self.distance = float('inf')
        # backtracking / where I was from
        self.previous = None

    def __str__(self) -> str:
        """ Returns a string describing the vertex.

        Arguments:
            None
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            return_string: a string describing the vertex.

        Returns:
            str: return_string, a string describing the vertex.
            
        Complexity:
            Best-case: O(N), where N is the number of edges.
            Worst-case: O(N), where N is the number of edges.
        """
        return_string = str(self.id)
        for edge in self.edges:
            return_string += "\n with edge " + str(edge)
        return return_string
    
    def add_edge(self, edge:Tuple[int, int, int]) -> None:
        """ Adds an edge to the vertex.

        Arguments:
            edge (Tuple[int, int, int]): the edge to be added to the vertex.
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            None

        Returns:
            None
            
        Complexity:
            Best-case: O(1)
            Worst-case: O(1)
        """
        self.edges.append(edge)

class Edge:
    """ Class called Edge.
    
    Non-abstract class called Edge which initializes an edge in a vertex.
    
    Constants: None
    
    Non-abstract methods:
        __init__ initializes an edge.
        __str__ returns a string describing the edge.
        
    Abstract methods:
        None
    """
    def __init__(self, u: int, v: int, w: int) -> None:
        """ Initializes an edge.

        Arguments:
            u (int): source vertex
            v (int): destination vertex
            w (int): weight of vertex (cost)
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            u: source vertex
            v: destination vertex
            w: weight of vertex (cost)
        
        Returns:
            None
            
        Complexity:
            Best-case: O(1)
            Worst-case: O(1)
        """
        self.u = u
        self.v = v
        self.w = w
        
    def __str__(self):
        """ Returns a string describing the edge.

        Arguments:
            None
            
        Raises:
            None
            
        Constants:
            None
            
        Variables:
            return_string: a string describing the edge.

        Returns:
            str: return_string, a string describing the edge.
            
        Complexity:
            Best-case: O(1)
            Worst-case: O(1)
        """
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string



# Question 1
def best_trades(prices: List[int], starting_liquid: int, max_trades: int, townspeople: List[int]) -> int or float:
    """ Returns the maximum value that can be obtained after performing at most
    max_trades trades.

    Arguments:
        prices (List[int]): prices of each type of liquid
        starting_liquid (int): liquid ID of starting liquid
        max_trades (int): maximum trades allowed to make
        townspeople (List[int]): people willing to make trade for different liquids
        
    Raises:
        TypeError: if type(prices[i]) != int and type(prices[i]) != float
        TypeError: if type(starting_liquid) != int
        ValueError: if starting_liquid < 0
        TypeError: if type(max_trades) != int
        ValueError: if max_trades < 0
        TypeError: if type(townspeople) != list
        ValueError: if len(townspeople) == 0
        TypeError: if type(townspeople[i]) != list
        ValueError: if len(townspeople[i]) == 0
        TypeError: if type(townspeople[i][j]) != tuple
        ValueError: if len(townspeople[i][j]) != 3

    Constants:
        None
        
    Variables:
        vertices: vertices to be added to the graph.
        my_graph: the graph created.
        edges: edges to be aadded into vertices of graph.
        total_litres: total_litres collected.
        total_price: total price of liquid owned.
        max_price: maximum price of liquid owned.
        counter: counts number of iterations.
        same_i: checks if iteration is at the same i.
    
    Returns:
        int or float: max_price, maximum value that you can obtain after performing at most max_trades.
    
    Complexity:
        Best-case: O(T * M), where T is the total number of trades available (edges),
                   and where M is the max_trades (number of iterations).
                   Occurs when Bellman-Ford's algorithm is performed.
        Worst-case: O(T * M), where T is the total number of trades available (edges),
                    and where M is the max_trades (number of iterations).
                    Occurs when Bellman-Ford's algorithm is performed.
    """
    # check prices pre-condition
    for i in range(len(prices)):
        if type(prices[i]) != int and type(prices[i]) != float:
            raise TypeError("prices should only contain integers or floats")
        
    # check starting_liquid pre-condition
    if type(starting_liquid) != int:
        raise TypeError("starting_liquid should be an integer")
    if starting_liquid < 0:
        raise ValueError("starting_liquid should be a non-negative integer")
    
    # check max_trades pre-condition
    if type(max_trades) != int:
        raise TypeError("max_trades should be an integer")
    if max_trades < 0:
        raise ValueError("max_trades should be a non-negative integer")
    
    # check townspeople pre-condition
    if type(townspeople) != list:
        raise TypeError("townspeople should be a list")
    if len(townspeople) == 0:
        raise ValueError("townspeople should be a list of non-empty lists")
    for i in range(len(townspeople)):
        if type(townspeople[i]) != list:
            raise TypeError("townspeople should be a list of lists")
        if len(townspeople[i]) == 0:
            raise ValueError("townspeople should be a list of non-empty lists")
    for i in range(len(townspeople)):
        for j in range(len(townspeople[i])):
            if type(townspeople[i][j]) != tuple:
                raise TypeError("townspeople should be a list of non-empty lists containing tuples")
            if len(townspeople[i][j]) != 3:
                raise ValueError("townspeople should be a list of non-empty lists containing 3 element tuples")
    
    vertices = []
    # create a graph based on number of types of liquids
    for i in range(len(prices)):
        vertices.append(i)
        
    my_graph = Graph(vertices)
    
    # add edges O(T)
    edges = []
    for i in range(len(townspeople)):
        for j in range(len(townspeople[i])):
            edges.append((townspeople[i][j][0], townspeople[i][j][1], townspeople[i][j][2]))
    my_graph.add_edges(edges)

    total_litres = 1
    total_price = prices[starting_liquid]
    max_price = 0
    counter = 0
    
    # initialize values from staring_liquid to all other vertices as -1
    temp = [(-1,-1,-1)] * len(my_graph.vertices)
    temp[starting_liquid] = (total_litres, total_litres * total_price, starting_liquid)
    
    # relax edges
    # counter is O(M)
    # Bellman-Ford
    while True:
        if counter > max_trades:
            break
        for i in range(len(my_graph.vertices) - 1):
            if counter > max_trades:
                break
            same_i = False
            for j in range(len(my_graph.vertices[i].edges)):
                if same_i == False:
                    counter += 1
                if counter > max_trades:
                    break
                same_i = True
                u = my_graph.vertices[i].edges[j].u
                v = my_graph.vertices[i].edges[j].v
                w = my_graph.vertices[i].edges[j].w
                frm = u
                total_litres = temp[frm][0]
                total_litres *= w
                total_price = prices[v] * total_litres
                temp[v] = (total_litres, total_price, frm)
                if total_price > max_price:
                    max_price = total_price
            
    return max_price



# Question 2
def opt_delivery(n: int, roads: List[Tuple[int, int, int]], start: int, end: int, delivery: Tuple[int, int, int]) -> Tuple[int or float, List[int]]:
    """ Returns a tuple stating the cost of travelling from start city to end city
    and the route taken.

    Arguments:
        n (int): number of cities
        roads (List[Tuple[int, int, int]]): list of tuples representing roads between cities, as well as the cost of travelling.
        start (int): represents the start city
        end (int): represents the end city
        delivery (Tuple[int, int, int]): tuple representing the pickup city, delivery city, and the revenue that can be made.

    Raises:
        TypeError: if type(n) != int
        ValueError: if n < 0
        TypeError: if type(roads) != list
        TypeError: if type(roads[i]) != tuple
        ValueError: if roads[i][j] < 0
        TypeError: if type(start) != int
        ValueError: if start < 0
        ValueError: if start >= n
        TypeError: if type(end) != int
        ValueError: if end < 0
        ValueError: if start >= n
        TypeError: if type(delivery) != tuple
        ValueError: if len(delivery) != 3
        
    Constants:
        None
        
    Variables:
        vertices: vertices to be added to the graph.
        my_graph: the graph created.
        edges: edges to be aadded into vertices of graph.
        path: route taken from source city to destination city.
        pickup: to keep track of pickup city.
        deliver: to keep track of deliver city.
        counter: to keep track of pickup city and deliver city.
        total_cost_delivery: total cost of going from start city to end city.
        new_cost: new_cost to replace old cost
        a: dijkstra return value of least cost of travelling through city.
        b: dijkstra return value of least cost of travelling from start city to pickup city.
        c: dijkstra return value of least cost of travelling from pickup city to deliver city.
        d: dijkstra: return value of least cost of travelling from deliver city to end city.
        ans: cost of travelling from start city to end city and the route taken.

    Returns:
        Tuple[int or float, List[int]]: ans, the cost of travelling from start city to end city
                                             and the route taken.
    
    Complexity:
        Best-case: O(Rlog(N)), where R is the total number of roads, and where N is the total number of cities.
                   Occurs when Dijkstra algorithm is performed.
        Worst-case: O(Rlog(N)), where R is the total number of roads, and where N is the total number of cities.
                    Occurs when Dijkstra algorithm is performed.
    """
    # check n pre-condition
    if type(n) != int:
        raise TypeError("n should be an integer")
    if n < 0:
        raise ValueError("n should be a non-negative integer")
    # check roads pre-condition
    if type(roads) != list:
        raise TypeError("roads should be a list")
    for i in range(len(roads)):
        if type(roads[i]) != tuple:
            raise TypeError("roads should be a list of tuples")
    for i in range(len(roads)):
        for j in range(len(roads[i])):
            if roads[i][j] < 0:
                raise ValueError("roads should be a list of tuples containing non-negative values")
    # check start pre-condition
    if type(start) != int:
        raise TypeError("start should be an integer")
    if start < 0:
        raise ValueError("start should be a non-negative integer")
    if start >= n:
        raise ValueError("start should be an integer in the range [0..n-1]")
    # check end pre-condition
    if type(end) != int:
        raise TypeError("end should be an integer")
    if end < 0:
        raise ValueError("end should be a non-negative integer")
    if start >= n:
        raise ValueError("end should be an integer in the range [0..n-1]")
    # check delivery pre-condition
    if type(delivery) != tuple:
        raise TypeError("delivery should be a tuple")
    if len(delivery) != 3:
        raise ValueError("delivery should be a tuple containing 3 values")

    # create graph
    vertices = []
    # create a graph based on number of cities
    for i in range(n):
        vertices.append(i)
        
    my_graph = Graph(vertices)
    
    # add edges O(R)
    edges = []
    for i in range(len(roads)):
        edges.append((roads[i][0], roads[i][1], roads[i][2]))
    my_graph.add_edges(edges, False)
    
    # shortest distance using Dijkstra
    a = my_graph.dijkstra(n, my_graph.vertices[start], my_graph.vertices[end])
    
    # check if went through delivery along the way
    path = a[1]
    pickup = 0
    deliver = 0
    counter = 0
    total_cost_delivery = a[0]
    new_cost = 0
    for i in range(len(path)):
        if path[i] == delivery[0] and pickup == 0:
            counter += 1
            pickup = counter
        if path[i] == delivery[1] and deliver == 0:
            counter += 1
            deliver = counter
            
    if pickup == 1 and deliver == 2:
        new_cost = a[0] - delivery[2]
        ans = (new_cost, a[1])
        
    else:
        my_graph.reset()
        b = my_graph.dijkstra(n, my_graph.vertices[start], my_graph.vertices[delivery[0]])
        my_graph.reset()
        c = my_graph.dijkstra(n, my_graph.vertices[delivery[0]], my_graph.vertices[delivery[1]])
        my_graph.reset()
        d = my_graph.dijkstra(n, my_graph.vertices[delivery[1]], my_graph.vertices[end])
        total_cost_delivery = b[0] + c[0] + d[0]
        total_cost_delivery -= delivery[2]
        new_path = []
        for i in range(len(b[1])):
            new_path.append(b[1][i])
        for i in range(1, len(c[1])):
            new_path.append(c[1][i])
        for i in range(1, len(d[1])):
            new_path.append(d[1][i])
    
        # compare no delivery with delivery
        if a[0] <= total_cost_delivery:
            ans = a
        else:
            ans = (total_cost_delivery, new_path)
    
    return ans
