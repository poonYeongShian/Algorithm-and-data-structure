""" Test cases for FIT2004 Assignment 4 Question 2 """
import unittest
from assignment4 import WordGraph

__author__ = "Pan Wei Hung"

class Debug:
    """
        Simple class to debug path
    """
    def __init__(self, words) -> None:
        self.words = words

    def print_path(self, path):
        """
            Simple method to print path for debugging
        """
        output = "\n"
        if path is not None:
            for elem in path:
                output += str(self.words[elem]) + " "
            output += "\n"
        return output

class TestWordGraph(unittest.TestCase):
    def setUp(self) -> None:
        words = ["aaa","bbb","bab","aaf","aaz","baz","caa","cac",
"dac","dad","ead","eae","bae","abf","bbf"]
        self.print = Debug(words)
        self.wordGraph = WordGraph(words)

    def test1(self):
        start = 0
        end = 1
        detour = [12]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [0, 6, 7, 8, 9, 10, 11, 12, 2, 1]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test2(self):
        start = 0
        end = 1
        detour = [2]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [0, 3, 13, 14, 1, 2, 1]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test3(self):
        start = 0
        end = 3
        detour = [13]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [0, 3, 13, 3]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test4(self):
        start = 0
        end = 3
        detour = [8, 9]
        target = self.wordGraph.constrained_ladder(start, end, detour)
        
        expected = [0, 6, 7, 8, 7, 6, 0, 3]
        self.assertEqual(target, expected, 
        msg="Included one detour point but failed to get the detour point with shortest distance, \nexpected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test5(self):
        start = 0
        end = 3
        detour = [8, 9]
        target = self.wordGraph.constrained_ladder(start, end, detour)
        
        expected = [0, 6, 7, 8, 7, 6, 0, 3]
        self.assertEqual(target, expected, 
        msg="Included one detour point but failed to get the detour point with shortest distance, \nexpected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

class TestNoPath(unittest.TestCase):
    def setUp(self) -> None:
                #  0     1     2     3     4     5     6     7     8     9     10
        words = ["aaa","aad","dad","daa","aca","acc","aab","abb","zzz","zza","bzz"]
        self.print = Debug(words)
        self.wordGraph = WordGraph(words)

    def test1(self):
        """
            Test detour start and end not connected, path should be None
        """
        start = 0
        end = 8
        detour = [9]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = None
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test2(self):
        """
            Test detour start and end connected, detour not connected, path should be None
        """
        start = 0
        end = 3
        detour = [8]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = None
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test3(self):
        """
            Test detour start and end connected, one of the detour not connected, path should be None
        """
        start = 0
        end = 3
        detour = [8,6]
        target = self.wordGraph.constrained_ladder(start, end, detour)
                  #  0     1     2     3     4     5     6     7     8     9     10
        # words = ["aaa","aad","dad","daa","aca","acc","aab","abb","zzz","zza","bzz"]

        expected = [0, 6, 0, 3]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test4(self):
        """
            Test detour start and end connected, all of the detour not connected, path should be None
        """
        start = 0
        end = 3
        detour = [8,9,10]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = None
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

class TestSmallCase(unittest.TestCase):
    def setUp(self) -> None:
                #   0        1        2        3        4        5        6
        words = ["aaaaaa","aaaaab","caaaaa","adaaaa","bdaaaa","bdcaaa","aaacaa"]
        self.print = Debug(words)
        self.wordGraph = WordGraph(words)
        """
            (2)caaaaa----\
            (1)aaaaab-----(0)aaaaaa-----(3)adaaaa-----(4)bdaaaa-----(5)bdcaaa
            (6)aaacaa----/
        """
        
    def test1(self):
        start = 0
        end = 5
        detour = [1,2,6]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [0,1,0,3,4,5]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test2(self):
        start = 4
        end = 5
        detour = [1,2,6]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [4,3,0,1,0,3,4,5]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test3(self):
        """
            Test if detour point included start or end
        """
        start = 4
        end = 5
        detour = [4,6]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [4,5]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))

    def test4(self):
        """
            Test if detour point included both start and end
        """
        start = 4
        end = 5
        detour = [4,5,6]
        target = self.wordGraph.constrained_ladder(start, end, detour)

        expected = [4,5]
        self.assertEqual(target, expected,msg="expected path: {expected}\nactual path: {actual}".format(expected = self.print.print_path(expected), actual = self.print.print_path(target)))
 

if __name__ == "__main__":
    unittest.main()