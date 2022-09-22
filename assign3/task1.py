"""
Name: POON YEONG SHIAN
ID: 30696003
"""


class Node:
    """
    Node class
    # referred to the lecture recording https://www.youtube.com/watch?v=0oD2Ar1bxbE, viewed on 22th Sep 2021
    """
    def __init__(self, size=27, level=None, frequency=0):
        """
        This is the method will run when you declared Node object
        :param size: the size of the list where the node link to
        :param level: level of the node
        :param frequency: the frequency of prefix
        """
        # class attributes
        self.link = [None] * size
        self.level = level
        self.frequency = frequency
        self.is_end = False
        self.terminal = 0


class Trie:
    """
    Trie class
    # referred to the lecture recording https://www.youtube.com/watch?v=0oD2Ar1bxbE, viewed on 22th Sep 2021
    """
    def __init__(self):
        # class attributes
        self.root = Node(level=0)
        self.is_unique = True

    def search(self, my_string, total):
        """
        This function traverse through trie and return the number of words in text which are lexicographically greater than the ith element
        :param my_string: my_string consisting only of lowercase a-z characters.
        :param total: frequency of words inserted into the Trie
        :return: the number of words in text which are lexicographically greater than the ith element
            complexity:
                time: O(T) time, where T is the number of character in my_string
                auxiliary space: O(1)
        """
        # initialize the current to root
        current = self.root

        # raise exception when my_string is None
        if my_string is None:
            raise Exception("string no exist")
        # loop through my_string
        for i in range(len(my_string)):
            index = ord(my_string[i]) - 97 + 1
            if current.link[index] is not None:
                # if path exist
                for j in range(index):
                    # current link at j exist
                    if current.link[j] is not None:
                        total -= current.link[j].frequency
                current = current.link[index]
            else:
                # if path does not exist
                raise Exception(str(my_string) + " no exist")

        # if the current.link at 0 is a terminal
        if current.link[0] is not None:
            return total - current.link[0].terminal

        return total

    def insert_rec(self, my_string):
        """
        This function insert my_string into the Trie
        :param my_string: my_string consisting only of lowercase a-z characters.
            complexity:
                time: O(T) time, where T is the number of character in my_string
                auxiliary space: O(1)
        """
        current = self.root
        current.frequency += 1
        self.insert_rec_aux(current, my_string)

    def insert_rec_aux(self, current, my_string):
        """
        This is an insert_rec auxiliary function
        :param my_string: my_string consisting only of lowercase a-z characters.
        :param current: current is the current node
            complexity:
                time: O(T) time, where T is the number of character in my_string
                auxiliary space: O(T), where T is the number of characters in my_string
        """
        # base case
        if len(my_string) == current.level:
            index = 0
            if current.link[index] is not None:
                # if terminal exist
                current = current.link[index]
                current.frequency += 1
                current.is_end = True
                current.terminal += 1
            else:
                # if terminal does not exist, create new node
                current.link[index] = Node(level=current.level + 1)
                current = current.link[index]
                current.frequency += 1
                current.is_end = True
                current.terminal += 1
        else:
            index = ord(my_string[current.level]) - 97 + 1
            if current.link[index] is not None:
                # if path exist
                current = current.link[index]
                current.frequency += 1
            else:
                # if path does not exist, create new node
                current.link[index] = Node(level=current.level + 1)
                current = current.link[index]
                current.frequency += 1
            # recursion
            self.insert_rec_aux(current, my_string)


def lex_pos(text, queries):
    """
    This function determining how many words in a text appear lexicographically later than a given word
    :param text: an unsorted list of strings
    :param queries: a list of strings consisting only of lowercase a-z characters. Each string in queries
                    is a prefix of some string in text
    :return: a list of numbers. The ith number in this list is the number of words in text
             which are lexicographically greater than the ith element of queries

        complexity:
            time: O(T + Q) time, where T is the sum of the number of characters in all strings in text
                                       Q is the total number of characters in queries
            auxiliary space:O(MN) where M is the size of array in each node of the trie which is 27
                                        N is the total number of keys in trie
    """
    # create a trie
    trie = Trie()
    ret = []
    #  loop through every item in text list
    for i in range(len(text)):
        if text[i] == "":
            continue
        trie.insert_rec(text[i])
    total_frequency = trie.root.frequency
    # loop through every item in queries
    for j in range(len(queries)):
        ret.append(trie.search(queries[j], total_frequency))
    return ret



