""" Unit tests for Task 1 of FIT2004 Assignment 3 """

__author__ = "Arthur Lee"

import unittest
from assignment4 import WordGraph


class TestConstrainedLadder(unittest.TestCase):
    PROVIDED = WordGraph(["aaa", "bbb", "bab", "aaf", "aaz", "baz", "caa", "cac", "dac", "dad", "ead", "eae", "bae", "abf", "bbf"])
    SINGLE_WORD = WordGraph(["foreveralone"])
    NO_EDGES = WordGraph(["aaaaaaa", "ddddddd", "ttttttt", "ooooooo", "iiiiiii", "qqqqqqq", "ppppppp", "lllllll"])
    DISCONNECTED = WordGraph(["zzzz", "lzzz", "zzyz", "zzza", "bbbb", "bbcb", "zzta", "bdbb", "bdcb"])
    ALL_SINGLE_CHAR = []
    ALL_DOUBLE_CHAR = []
    ALL_TRIPLE_CHAR = []

    @classmethod
    def setUpClass(cls):
        lowercase = [chr(i) for i in range(97, 123)]
        cls.ALL_SINGLE_CHAR = lowercase
        for i in range(len(lowercase)):
            for j in range(len(lowercase)):
                cls.ALL_DOUBLE_CHAR.append("".join([lowercase[i], lowercase[j]]))
        for i in range(len(lowercase)):
            for j in range(len(lowercase)):
                for k in range(len(lowercase)):
                    cls.ALL_TRIPLE_CHAR.append("".join([lowercase[i], lowercase[j], lowercase[k]]))
        cls.ALL_SINGLE_CHAR = WordGraph(cls.ALL_SINGLE_CHAR)
        cls.ALL_DOUBLE_CHAR = WordGraph(cls.ALL_DOUBLE_CHAR)
        cls.ALL_TRIPLE_CHAR = WordGraph(cls.ALL_TRIPLE_CHAR)

    def test_provided_1(self):
        """ First Provided Example """
        start = 0
        end = 1
        detour = [12]
        g = self.PROVIDED
        expected = [0, 6, 7, 8, 9, 10, 11, 12, 2, 1]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_provided_2(self):
        """ Second Provided Example """
        start = 0
        end = 1
        detour = [2]
        g = self.PROVIDED
        expected = [0, 3, 13, 14, 1, 2, 1]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_single_word_to_itself(self):
        """ Only possible path to yourself in a single vertex graph is from yourself to yourself passing yourself """
        start = 0
        end = 0
        detour = [0]
        g = self.SINGLE_WORD
        expected = [0]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_no_edges_to_yourself_pass_yourself(self):
        """ Graph has no edges, go to yourself passing by yourself """
        start = 4
        end = 4
        detour = [0, 7, 6, 3, 4]
        g = self.NO_EDGES
        expected = [4]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_no_edges_to_yourself_invalid_detours(self):
        """ Graph has no edges, try to go to yourself but need to pass by impossible to reach words """
        start = 6
        end = 6
        detour = [7, 5, 4, 3, 2, 1, 0]
        g = self.NO_EDGES
        expected = None
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_no_edges_go_somewhere_impossible(self):
        """ Graph has no edges, try to go to another word. Impossible """
        start = 3
        end = 1
        detour = [3]
        g = self.NO_EDGES
        expected = None
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_disconnected_impossible_destination_impossible_detours(self):
        """ Graph is split in two. Impossible to reach destination, impossible to reach detours """
        start = 0
        end = 7
        detour = [3, 1]
        g = self.DISCONNECTED
        expected = None
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_ideal_path_has_no_detours(self):
        """ Detours are the source and destination themselves """
        start = 0
        end = 2
        detour = [2, 0]
        g = self.DISCONNECTED
        expected = [0, 2]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_more_than_one_ideal_path(self):
        """ More than one possible ideal path """
        start = 4
        end = 8
        detour = [5, 7]
        g = self.DISCONNECTED
        expected = [[4, 7, 8], [4, 5, 8]]
        actual = g.constrained_ladder(start, end, detour)
        self.assertIn(actual, expected)

    def test_all_possible_detours(self):
        """ Every word is listed as a detour, best would be not to use detour """
        start = 0
        end = 2
        detour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        g = self.PROVIDED
        expected = [0, 3, 13, 14, 1, 2]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_all_possible_detours_exclude_source_and_destination(self):
        """  Every word is listed as a detour excluding source and destination, true shortest detour problem """
        start = 0
        end = 2
        detour = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        g = self.PROVIDED
        expected = [0, 3, 13, 14, 1, 2]
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_all_single_char_combinations(self):
        """ All combinations of single lowercase letters """
        start = 0
        end = 16
        detour = [1, 4, 7, 3, 9, 5]
        g = self.ALL_SINGLE_CHAR
        expected = [0, 1, 16]    # I got this, tell me if you got something else
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_all_double_char_combinations(self):
        """ All combinations of double lowercase letters """
        start = 6
        end = 473
        detour = [3, 4, 19, 22, 30, 31, 34, 35, 42, 47, 49, 58, 64, 73, 74, 76, 82, 86, 91, 94, 102, 107, 123, 125, 157, 168, 170, 182, 185, 186, 189, 192, 199, 204, 209, 231, 250, 251, 260, 262, 276, 279, 288, 299, 300, 307, 308, 318, 320, 322, 327, 339, 360, 382, 384, 387, 388, 423, 438, 462, 463, 467, 469, 471, 472, 478, 480, 482, 488, 491, 492, 502, 503, 506, 511, 516, 517, 519, 520, 521, 526, 530, 534, 550, 551, 562, 563, 569, 587, 589, 600, 605, 615, 620, 627, 642, 648, 664, 666, 675]
        g = self.ALL_DOUBLE_CHAR
        expected = [6, 5, 31, 473]    # I got this, tell me if you got something else
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)

    def test_all_triple_char_combinations(self):
        """ All combinations of triple lowercase letters """
        start = 17491
        end = 13496
        detour = [4859, 1374, 5697, 9415, 9556, 6426, 2052, 4417, 13232, 12090, 3784, 17265, 3978, 573, 6397, 16978, 16164, 3817, 14289, 12603, 911, 13296, 2599, 1364, 9509, 13433, 13468, 11760, 1609, 4896, 14923, 11923, 16278, 8669, 11893, 3556, 17054, 2954, 17367, 4449, 15223, 16043, 4080, 17199, 9814, 3416, 3092, 13952, 2878, 11323, 14602, 15429, 3136, 7557, 12102, 12529, 3426, 14703, 8200, 15744, 2186, 779, 15764, 9282, 5653, 1118, 10625, 12668, 10971, 2023, 9011, 16390, 8794, 12054, 2586, 6225, 2727, 12986, 17530, 693, 16230, 10034, 3892, 7060, 16112, 3887, 12278, 1421, 13808, 2790, 12348, 16029, 14300, 14479, 2928, 10723, 13861, 14101, 787, 9860, 6519, 5348, 11305, 773, 15966, 7163, 7994, 8344, 14378, 14587, 14598, 5544, 8963, 6956, 14753, 15844, 4511, 12080, 7095, 9579, 14745, 9510, 972, 4767, 14418, 10284, 702, 8918, 17050, 2712, 4083, 9648, 11437, 3772, 16727, 15314, 2382, 1353, 7906, 16368, 10616, 12327, 13694, 10576, 10523, 11248, 1780, 12783, 5361, 9928, 5797, 17245, 9462, 10814, 15703, 9075, 6747, 5576, 15473, 4634, 742, 9149, 7271, 14207, 12129, 16109, 16104, 13203, 10273, 5391, 4873, 8957, 13268, 1950, 14812, 7754, 8051, 8387, 6318, 7479, 5719, 7873, 2896, 5993, 2998, 5325, 4620, 2629, 8221, 2224, 11669, 3320, 7318, 14215, 13578, 4459, 11644, 14790, 3467, 3798, 2770, 9311, 4117, 14366, 8280, 7896, 7442, 12240, 6953, 15181, 7484, 16115, 2806, 14881, 12363, 15380, 4949, 15730, 15166, 15271, 11199, 10855, 16500, 5780, 925, 13024, 8919, 5691, 7329, 2548, 967, 2021, 1153, 7306, 9255, 16501, 15304, 3062, 10649, 15641, 8425, 15621, 7833, 14876, 16077, 3993, 17212, 12522, 4287, 15147, 12686, 10003, 9476, 13245, 7297, 9723, 11898, 1131, 8939, 7937, 2936, 5117, 5927, 2783, 8105, 14510, 7819, 2742, 15051, 14359, 12060, 3442, 4041, 14165, 40, 5499, 12288, 12550, 8063, 4828, 4254, 8182, 5081, 16629, 4389, 11780, 3968, 16895, 4155, 468, 2242, 3000, 15155, 7083, 12371, 16602, 883, 13152, 4421, 12124, 17448, 11529, 10088, 15243, 6998, 6752, 11306, 13122, 15175, 9488, 13150, 6307, 3689, 17415, 5816, 4650, 9851, 1149, 8174, 12375, 6119, 10538, 3251, 6701, 4200, 6335, 11365, 8191, 1829, 1813, 5826, 14765, 9870, 6403, 2538, 13592, 1306, 280, 11202, 5798, 1577, 6255, 12445, 11313, 15129, 7424, 3434, 7116, 17418, 11769, 8071, 1643, 12211, 2701, 2836, 9534, 8117, 3673, 4821, 13385, 9546, 16295, 11011, 6027, 16840, 13883, 15675, 13573, 15308, 8866, 408, 16867, 7389, 5958, 17316, 7494, 5636, 7576, 5031, 597, 11576, 10352, 10245, 15960, 14939, 10172, 8050, 16061, 11537, 15880, 9715, 4336, 876, 11908, 3218, 10765, 13848, 13216, 13153, 12600, 5358, 11031, 9279, 2920, 8922, 12013, 8862, 11574, 14130, 16417, 16117, 15315, 8252, 854, 11253, 6606, 11955, 14986, 7646, 168, 1086, 8660, 4314, 17071, 16835, 11458, 16944, 16726, 11419, 3899, 1581, 5068, 9060, 13941, 9489, 11343, 13761, 12201, 16666, 12040, 6846, 7379, 7899, 8571, 10014, 1763, 14147, 7215, 13007, 8478, 7469, 10412, 9700, 6140, 9984, 5778, 8891, 8251, 2173, 12104, 13673, 13410, 16969, 8437, 14224, 2193, 16266, 4847, 6256, 8515, 11683, 17413, 3225, 2033, 8359, 5850, 1838, 15265, 9782, 1933, 16232, 7300, 1191, 12119, 6910, 11708, 15089, 17499, 14420, 9833, 11757, 1809, 11777, 14731, 9785, 2187, 9059, 2698, 12436, 10643, 7252, 14815, 8856, 6872, 466, 6682, 9071, 14524, 14213, 477, 10131, 12897, 5079, 9091, 11157, 11996, 1748, 14615, 3571, 6790, 2453, 7198, 17301, 11443, 14522, 5095, 11609, 15064, 1597, 364, 8158, 5885, 644, 3303, 2385, 3283, 11556, 6144, 10778, 6611, 4980, 5086, 15689, 15749, 5980, 6543, 16, 4865, 15445, 7367, 2428, 14885, 17217, 6717, 8326, 13316, 1955, 2768, 10945, 11541, 5585, 15328, 2349, 5509, 1012, 2151, 8619, 14589, 9840, 15427, 1069, 16032, 10983, 13457, 16322, 9447, 1432, 688, 1398, 9000, 6448, 17416, 9618, 8298, 5465, 10950, 9177, 7617, 5743, 6744, 5164, 5030, 15742, 3078, 16901, 6530, 8686, 868, 6896, 9142, 7655, 5546, 9588, 10256, 15312, 2305, 12537, 471, 820, 7022, 2062, 7993, 13923, 12952, 7177, 9171, 10961, 10121, 8361, 441, 12949, 5445, 13552, 4810, 16336, 1524, 1286, 5689, 3213, 10001, 9077, 76, 8099, 643, 10672, 8471, 11017, 3682, 2617, 2218, 10368, 8529, 3259, 6841, 16976, 15897, 14450, 17247, 13704, 1975, 12684, 14456, 3305, 2222, 14514, 1794, 3509, 13459, 15056, 1416, 11244, 6648, 16590, 13585, 11772, 12203, 3169, 13987, 12988, 7269, 13136, 2707, 9344, 7957, 9898, 11015, 14424, 9998, 7267, 15823, 4850, 758, 1982, 536, 6692, 11239, 12984, 17294, 9383, 6460, 13409, 7600, 11314, 9197, 1954, 209, 10510, 10727, 16641, 3452, 5766, 1979, 10300, 7161, 7872, 16250, 10233, 10102, 9578, 4855, 13937, 5542, 4210, 9035, 7820, 2709, 12308, 14051, 7543, 1448, 12708, 1884, 2887, 781, 8342, 8584, 405, 16617, 6783, 3889, 16801, 2926, 10633, 14271, 17086, 14673, 2855, 14159, 12206, 5558, 16588, 4915, 1209, 6870, 13680, 14948, 12423, 14832, 7775, 1454, 16742, 4097, 12818, 9464, 7385, 12392, 17055, 6129, 13642, 6474, 6415, 8658, 7973, 84, 5155, 4948, 1497, 6221, 14493, 1500, 8445, 17354, 8978, 15094, 13265, 15071, 180, 863, 11086, 15266, 14556, 3232, 15285, 3446, 17349, 9883, 164, 11918, 3084, 4357, 11452, 9852, 13647, 7737, 15927, 8222, 4144, 15957, 1583, 8260, 1902, 2638, 5772, 8137, 8303, 4629, 1238, 16732, 15394, 7539, 909, 9379, 14007, 2431, 4118, 2708, 17351, 10650, 11562, 14751, 9438, 6561, 13805, 8692, 13175, 3771, 7622, 10197, 1444, 7877, 9717, 10682, 10048, 12755, 15883, 17495, 2513, 2997, 2490, 9051, 6287, 5492, 5161, 15502, 2514, 5575, 15894, 14647, 10125, 10869, 14915, 1526, 5406, 8366, 57, 16387, 4822, 13372, 5613, 4816, 2761, 6360, 14451, 5702, 12451, 11284, 16967, 7485, 17256, 956, 14655, 6976, 16885, 1816, 16447, 918, 4595, 15627, 6279, 10527, 10922, 8310, 14124, 11927, 16309, 8932, 12019, 14362, 4793, 8159, 9511, 11575, 7678, 12193, 15574, 14349, 12585, 11948, 13859, 12107, 10093, 9259, 2781, 5839, 16861, 6927, 1133, 11560, 816, 6589, 14240, 1686, 11550, 3065, 750, 12169, 3400, 3838, 7537, 3451, 15344, 14798, 10736, 5604, 10531, 2812, 10032, 15856, 431, 490, 6306, 5692, 6510, 3751, 16538, 14850, 12250, 14491, 14388, 16675, 2117, 3277, 15138, 9401, 9761, 15376, 6490, 14164, 6121, 3448, 9122, 13774, 10562, 10693, 4566, 14664, 5967, 4587, 14893, 11315, 14433, 4088, 16404, 593, 4902, 3529, 16966, 2753, 17510, 16198, 15907, 16187, 15015, 13803, 8928, 6827, 6328, 9493, 11079, 13207, 8569, 375, 14225, 10503, 10788, 11833, 1483, 793, 7107, 7690, 8081, 1480, 9857, 11400, 4570, 1820, 12773, 12568]
        g = self.ALL_TRIPLE_CHAR
        expected = [17491, 17490, 17516, 16164, 16148, 13444, 13496]    # I got this, tell me if you got something else
        actual = g.constrained_ladder(start, end, detour)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
