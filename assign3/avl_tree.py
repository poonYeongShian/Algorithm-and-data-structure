"""
Name: Poon Yeong Shian
ID: 30696003
"""
# import random, math

outputdebug = False


def debug(msg):
    if outputdebug:
        print(msg)


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        tree = self.node

        newnode = Node(key)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")

        elif key < tree.key:
            self.node.left.insert(key)

        elif key > tree.key:
            self.node.right.insert(key)

        else:
            debug("Key [" + str(key) + "] already in tree.")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.key) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.key == key:
                debug("Deleting ... " + str(key))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        debug("Found replacement for " + str(key) + " -> " + str(replacement.key))
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if (self.node != None):
            print('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]",
                  'L' if self.is_leaf() else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

    def uncorrupted_merge(self, other, corrupted):
        """
        This function remove corrupted items from an AVL tree and insert the remaining to the other tree
        :param other: is the other AVL tree
        :param corrupted: is a list of keys
            complexity:
                time: O(L log N), L is the corrupted items one of the AVL tree. N is the number of nodes.
                space: O(N), N is the number of nodes
        """
        # left avl with all item smaller than self avl
        left_avl = other
        if other.node is None:
            return

        # right avl with all item larger than t1
        right_avl = AVLTree()
        right_avl.node = self.node

        # create a avl tree
        root_avl = AVLTree()

        if self.node is None:
            for corrupt_item in corrupted:
                other.delete(corrupt_item)
            self.node = other.node
            return

        # assign key to the root of root_avl
        root_avl.node = Node((left_avl.node.key + right_avl.node.key) / 2)

        # assign the left_avl and right_avl to be the avl subtree of the root_avl
        root_avl.node.left = left_avl
        root_avl.node.right = right_avl

        # remove corrupted item from left_avl
        for corrupt_item in corrupted:
            root_avl.node.left.delete(corrupt_item)

        # get successor node of the root
        temp_successor = root_avl.logical_successor(root_avl.node)
        temp_predecessor = root_avl.logical_predecessor(root_avl.node)

        # check difference between successor and predecessor
        diff = temp_successor.key - temp_predecessor.key
        if diff > 10000:
            # delete predecessor node from right_avl
            root_avl.node.left.delete(temp_predecessor.key)

            # replace the root key with the predecessor key
            root_avl.node.key = temp_predecessor.key
        else:
            # delete successor node from right_avl
            root_avl.node.right.delete(temp_successor.key)

            # replace the root key with the successor key
            root_avl.node.key = temp_successor.key

        self.node = root_avl.node

        # check balanced
        if not self.check_balanced():
            self.rebalance()

# Usage example
# if __name__ == "__main__":
#
#     t1 = AVLTree()
#     lst1 = [1, 2, 3, 5, 4]
#     for i in lst1:
#         t1.insert(i)
#
#     t2 = AVLTree()
#     lst2 = [6, 7, 8, 9, 10]
#     for i in lst2:
#         t2.insert(i)
#
#     corrupted = [1, 3, 5]
#     t2.uncorrupted_merge(t1, corrupted)
#     print(t2.inorder_traverse())
