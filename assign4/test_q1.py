""" Unit tests for Task 1 of FIT2004 Assignment 3 """

__author__ = "Arthur Lee"

import unittest
import random
from assignment4 import WordGraph


class TestTargetWords(unittest.TestCase):
    PROVIDED = WordGraph(["aaa", "aad", "dad", "daa", "aca", "acc", "aab", "abb"])
    # EMPTY = WordGraph([])
    SINGLE_WORD = WordGraph(["foreveralone"])
    NO_EDGES = WordGraph(["aa", "bb", "dd", "zz", "xx", "ff", "uu", "oo"])
    DISCONNECTED = WordGraph(["ggggg", "ggzgg", "abbbb", "ggjgg", "ggzgj", "agzgj", "bbbbb", "bbbbd", "bbbbc"])
    ALL_SINGLE_CHAR = []
    ALL_DOUBLE_CHAR = []

    @classmethod
    def setUpClass(cls):
        lowercase = [chr(i) for i in range(97, 123)]
        cls.ALL_SINGLE_CHAR = lowercase
        for i in range(len(lowercase)):
            for j in range(len(lowercase)):
                cls.ALL_DOUBLE_CHAR.append("".join([lowercase[i], lowercase[j]]))
        cls.ALL_SINGLE_CHAR = WordGraph(cls.ALL_SINGLE_CHAR)
        cls.ALL_DOUBLE_CHAR = WordGraph(cls.ALL_DOUBLE_CHAR)

    def test_provided_1(self):
        """ First Provided Example """
        g = self.PROVIDED
        expected = 0
        actual = g.best_start_word([2, 7, 5])
        self.assertEqual(expected, actual)

    def test_provided_2(self):
        """ Second Provided Example """
        g = self.PROVIDED
        expected = 1
        actual = g.best_start_word([6, 2])
        self.assertEqual(expected, actual)

    def test_provided_3(self):
        """ Third Provided Example """
        g = self.PROVIDED
        expected = 4
        actual = g.best_start_word([0, 4, 5])
        self.assertEqual(expected, actual)

    # def test_empty_everything(self):
    #     """ Wordset and Target Words are empty """
    #     g = self.EMPTY
    #     target_words = []
    #     expected = -1
    #     actual = g.best_start_word(target_words)
    #     self.assertEqual(expected, actual)
    #
    # def test_empty_targets(self):
    #     """ No target words. No appropriate start word """
    #     g = self.PROVIDED
    #     target_words = []
    #     expected = -1
    #     actual = g.best_start_word(target_words)
    #     self.assertEqual(expected, actual)

    def test_single_word(self):
        """ Only one word in wordset. Can only go to yourself. """
        g = self.SINGLE_WORD
        target_words = [0]
        expected = 0
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_to_yourself_no_edges(self):
        """ The best word to yourself is yourself. Test for graph with multiple vertices, no edges """
        g = self.NO_EDGES
        target_words = [3]
        expected = 3
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_to_yourself_connected(self):
        """ The best word to yourself is yourself. Test for connected graph """
        g = self.PROVIDED
        target_words = [7]
        expected = 7
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_no_appropriate_start_word_no_edges(self):
        """ When the graph is disconnected and no best word that is connected to all targets """
        g = self.NO_EDGES
        target_words = [3, 1, 2, 4, 5, 6, 7, 0]
        expected = -1
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_no_appropriate_start_word_disconnected(self):
        """ When the graph is disconnected and no best word that is connected to all targets """
        g = self.NO_EDGES
        target_words = [1, 2, 0, 7, 4, 5]
        expected = -1
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_appropriate_start_word_disconnected(self):
        """ When the graph is disconnected but there is a valid best start word """
        g = self.DISCONNECTED
        target_words = [2, 7, 8]
        expected = 6
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_multiple_start_words(self):
        """ More than one valid start word """
        g = self.DISCONNECTED
        target_words = [3, 1, 0]
        expected = [0, 1, 3]
        actual = g.best_start_word(target_words)
        self.assertIn(actual, expected)

    def test_all_words(self):
        """ Best start to go to all words """
        g = self.PROVIDED
        target_words = [0, 1, 2, 3, 4, 5, 6, 7]
        expected = 0
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_all_single_char_combinations(self):
        """ All combinations of single lowercase letters """
        g = self.ALL_SINGLE_CHAR
        random.seed("SINGLE")
        target_words = random.sample([i for i in range(26)], 5)
        expected = 0    # I got 0, tell me if you got something else
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)

    def test_all_double_char_combinations(self):
        """ All combinations of double lowercase letters """
        g = self.ALL_DOUBLE_CHAR
        random.seed("DOUBLE")
        target_words = random.sample([i for i in range(676)], 10)
        expected = 0    # I got 0, tell me if you got something else
        actual = g.best_start_word(target_words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
