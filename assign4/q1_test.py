""" Test cases for FIT2004 Assignment 4 Question 1 """
import unittest
from assignment4 import WordGraph

class TestWordGraph(unittest.TestCase):
    def setUp(self) -> None:
        words = ["aaa","aad","dad","daa","aca","acc","aab","abb"]
        self.wordGraph = WordGraph(words)

    def test1(self):
        target = self.wordGraph.best_start_word([2,7,5])
        expected = 0
        self.assertEqual(target, expected)
    
    def test2(self):
        target = self.wordGraph.best_start_word([6,2])
        expected = 1
        self.assertEqual(target, expected)

    def test3(self):
        target = self.wordGraph.best_start_word([0,4,5])
        expected = 4
        self.assertEqual(target, expected)

    def test4(self):
        target = self.wordGraph.best_start_word([3,5,7])
        expected = 0
        self.assertEqual(target, expected)

    def test5(self):
        target = self.wordGraph.best_start_word([1,2,3])
        expected = 2
        self.assertEqual(target, expected)


class TestIsolatedVertex(unittest.TestCase):
    def setUp(self) -> None:
        words = ["aaa","aad","dad","daa","aca","acc","aab","abb","zzz","zza"]
        self.wordGraph = WordGraph(words)

    def test1(self):
        target = self.wordGraph.best_start_word([0,9])
        expected = -1
        self.assertEqual(target, expected, msg="unable to identify isolated vertex")

    def test2(self):
        target = self.wordGraph.best_start_word([0,8])
        expected = -1
        self.assertEqual(target, expected, msg="unable to identify isolated vertex")

    def test3(self):
        target = self.wordGraph.best_start_word([0,8,9])
        expected = -1
        self.assertEqual(target, expected, msg="unable to identify isolated vertex")


class TestIsolatedVertices(unittest.TestCase):
    def setUp(self) -> None:
        words = ["aaa","aad","dad","daa","aca","acc","aab","abb","zzz","zza","kkk","fff"]
        self.wordGraph = WordGraph(words)

    def test1(self):
        target = self.wordGraph.best_start_word([0,9,10,11])
        expected = -1
        self.assertEqual(target, expected, msg="unable to identify isolated vertices")

    def test2(self):
        target = self.wordGraph.best_start_word([8,9])
        expected = 8
        self.assertEqual(target, expected)

    def test3(self):
        target = self.wordGraph.best_start_word([9,10,11])
        expected = -1
        self.assertEqual(target, expected, msg="unable to identify isolated vertices")


if __name__ == "__main__":
    unittest.main()
