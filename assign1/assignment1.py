"""
Name: Poon Yeong Shian
ID: 30696003
"""
import random
import time
import math


# Q1
def max_list(lst):
    """
    Provide the maximum element from the list given
    :param lst: a list of integers
    :return: the maximum element from the list given
        complexity:
            time: O(n), n is the size of the list
            auxiliary space: O(1)
    """
    max_item = lst[0]
    for item in lst:
        if item > max_item:
            max_item = item
    return max_item


def stable_counting_sort(lst, col, base):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort a given list of integers into ascending numerical order according to given base and col
    :param lst: list of non-negative integers
    :param col: col is an integer
    :param base: base is an integer, with value >= 2
    :return: sorted list according to the col
    complexity:
            time: O(n + base), n is the length of lst, base is the value of base
            auxiliary space: O(n + base), n is the length of lst, base is the value of base
    """
    # find the maximum
    max_item = base - 1

    # initialize count array and need to +1 because we have no choice but include index 0
    count_array = [None] * (max_item + 1)

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array
    for item in lst:
        digit = item // base ** col % base
        count_array[digit].append(item)

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            lst[index] = frequency[j]
            index += 1

    return lst


def num_rad_sort(nums, b):
    """
    # referred to the lecture recording https://youtu.be/Zw5IxI_ccGY, viewed on 11th Aug 2021
    Sort a given list of integers into ascending numerical order, given base.
    :param nums: list of unsorted non-negative integers
    :param b: base is an integer, with value >= 2
    :return: sorted list
    complexity:
            time: O((n + b) * Math.log(M,b)), n is the length of nums, b is the value of b,
                  M is the numerical value of the maximum element of nums
            auxiliary space: O(n), n is the length of nums
    """
    if len(nums) == 0 or len(nums) == 1:
        return nums
    # find the maximum
    max_item = max_list(nums)

    # find the number of column
    col = 1
    if max_item != 0:
        col = math.floor(math.log(max_item, b) + 1) + 1

    # loop through each col and perform counting sort
    for i in range(col):
        nums = stable_counting_sort(nums, i, b)

    return nums


# Q2
def base_timer(num_list, base_list):
    """
    This is a function that generate a list of run time, given a integer list and a integer base list
    :param num_list: integer number of list
    :param base_list: integer base number of list
    :return: list of run time
    """
    run_time_lst = []
    for i in base_list:
        start = time.time()
        num_rad_sort(num_list, i)
        time_taken = time.time() - start
        run_time_lst.append(time_taken)
    return run_time_lst


def max_string_len(lst):
    """
    Provide the maximum len element from the list given
    :param lst: a list of string
    :return: the string element with the maximum length in lst
        complexity:
            time: O(n), n is the size of the lst
            auxiliary space: O(1)
    """
    # initialise max_item
    max_item = lst[0]

    # loop through the lst
    for item in lst:
        if len(item) > len(max_item):
            max_item = item
    return max_item


def len_counting_sort(lst):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort a given list of string into ascending order according to the length of its element.
    :param lst: list of string
    :return: sorted string list according to the length of its element
    complexity:
            time: O(n + m), n is the length of lst, m is the length of the maximum element
            auxiliary space: O(n + m), n is the length of lst, m is the length of the maximum element
    """
    # find the element with the maximum length in lst
    max_item = max_string_len(lst)

    # initialize count array and need to +1 because we have no choice but include index 0
    count_array = [None] * (len(max_item) + 1)

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array
    for item in lst:
        count_array[len(item)].append(item)

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            lst[index] = frequency[j]
            index += 1

    return lst


def len_counting_sort2(lst, start_index):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort lst according to the length of start_index element which in tuple and start_index
    allow us to choose first or second element.

    :param start_index: choose an element 0 is a persons name, 1 is things this person likes
    :param lst: lst is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: sorted list according to the length of name or length this person likes
    complexity:
            time: O(n + m), n is the length of lst, m is the length of element with the maximum length
            auxiliary space: O(n + m), n is the length of lst, m is the length of element with the maximum length
    """
    # find the element with maximum length
    if start_index == 1:
        max_item = get_max_len_from_tuple_of_list(lst)
    else:
        max_item = max_string_len2(lst, start_index)

    # initialize count array and need to +1 because we have no choice but include index 0
    count_array = [None] * (max_item + 1)

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array
    for item in lst:
        count_array[len(item[start_index])].append(item)

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            lst[index] = frequency[j]
            index += 1

    return lst


def len_counting_sort3(lst, start_index):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort a given list of integers into ascending order according to length of lst[i][start_index][0]), i is 0 to len(lst)-1.
    allow us to choose first or second element.

    :param start_index: choose an element 0 is a persons name, 1 is things this person likes
    :param lst: lst is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: sorted list according to length of lst[start_index][0])
    complexity:
            time: O(n + m), n is the length of lst, m is the length the maximum length length of lst[i][start_index][0]), i is 0 to len(lst)-1.
            auxiliary space: O(n + m), n is the length of lst, m is the length the maximum length length of lst[i][start_index][0]), i is 0 to len(lst)-1.
    """
    # find the element with maximum length
    max_item = max_string_len2(lst, start_index)

    # initialize count array and need to +1 because we have no choice but include index 0
    count_array = [None] * (max_item + 1)

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array
    for item in lst:
        count_array[len(item[start_index][0])].append(item)

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            lst[index] = frequency[j]
            index += 1

    return lst


def alpha_counting_sort(data, col):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort a given list of string into ascending alphabetic order according to given col
    :param data: data is a string list
    :param col: col is an integer
    :return: sorted string list according to the col
    complexity:
            time: O(n), n is the number of elements in data
            auxiliary space: O(n), n is the number of elements in data
    """
    base = 26
    # initialize count array
    count_array = [None] * base

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array, loop each element from top to bottom
    for j in range(len(data)):
        if len(data[j]) >= col + 1 and ord(data[j][col]) >= 97:
            digit = ord(data[j][col]) - 97
            count_array[digit].append(data[j])
        else:
            count_array[0].append(data[j])

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            data[index] = frequency[j]
            index += 1
    return data


def alpha_radix_sort(list1):
    """
    # referred to the lecture recording https://youtu.be/Zw5IxI_ccGY, viewed on 11th Aug 2021
    Sort a given list of string into ascending string order
    :param list1: list of unsorted string
    :return: sorted string list
    complexity:
            time: O(n * col), n is number of element in list1
                             col is length of the maximum element in list1
            auxiliary space: O(n), n is the length of nums
    """
    # find the string with maximum length from the list
    max_len = max_string_len(list1)

    # sort the list in ascending order according to its length
    list1 = len_counting_sort(list1)

    # loop each each col from right to left
    for col in range(len(max_len) - 1, -1, -1):
        list1 = alpha_counting_sort(list1, col)

    return list1


def beta_counting_sort(data, col, index):
    """
    # referred to the lecture recording https://youtu.be/Ww0kYGWij58, viewed on 11th Aug 2021
    Sort a given list of string into ascending alphabetic order according to first element or second element
    of the element of the data, given col.
    :param index: choose an element 0 is a persons name, 1 is things this person likes
    :param data: data is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :param col: col is an integer
    :return: Sorted list of tuple by its name and a given col
    complexity:
            time: O(n), n is the number of elements in data
            auxiliary space: O(n), n is the number of elements in data
    """

    base = 26

    # initialize count array
    count_array = [None] * base

    # declared all the element in the array to be an empty list
    for i in range(len(count_array)):
        count_array[i] = []

    # update the count array, loop each element from right to left
    if index == 0:
        for j in range(len(data)):
            if len(data[j][index]) >= col + 1 and ord(data[j][index][col]) >= 97:
                digit = ord(data[j][index][col]) - 97
                count_array[digit].append(data[j])
            else:
                count_array[0].append(data[j])
    else:
        for j in range(len(data)):
            if len(data[j][index][0]) >= col + 1 and ord(data[j][index][0][col]) >= 97:
                digit = ord(data[j][index][0][col]) - 97
                count_array[digit].append(data[j])
            else:
                count_array[0].append(data[j])

    # update the input array
    index = 0

    # loop through the count array to rebuild the entire list
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(len(frequency)):
            data[index] = frequency[j]
            index += 1
    return data


def beta_radix_sort(list1, index):
    """
    # referred to the lecture recording https://youtu.be/Zw5IxI_ccGY, viewed on 11th Aug 2021
    # sort the list1 in ascending order according to their name
    :param index: 0 is name, 1 is thing that person like
    :param list1: list1 is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: sorted list1 in ascending order according to their name
    complexity:
            time: O(n * col), n is number of element in list1
                             col is length of the maximum string element in list1
            auxiliary space: O(n), n is the length of nums
    """
    # get the max string from the list
    max_len = max_string_len2(list1, index)

    # sorted list1 in ascending order according to their length of index
    list1 = len_counting_sort3(list1, index)

    # loop each each col from right to left
    for col in range(max_len - 1, -1, -1):
        list1 = beta_counting_sort(list1, col, index)

    return list1


def max_string_len2(lst, index):
    """
    provide the maximum length of name in lst
    :param index: 0 is the name, 1 is thing they like
    :param lst: data is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: maximum name of lst
        complexity:
            time: O(n), n is the size of the lst
            auxiliary space: O(1)
    """
    if index == 0:
        # get the max length element in the first item of the lst
        max_item_len = len(lst[0][index])
        for i in range(1, len(lst)):
            if len(lst[i][index]) > max_item_len:
                max_item_len = len(lst[i][index])
    else:
        # get the max length element in the first which is in the second item of the tuple
        max_item_len = len(lst[0][index][0])
        for i in range(1, len(lst)):
            if len(lst[i][index][0]) > max_item_len:
                max_item_len = len(lst[i][index][0])

    return max_item_len


def get_max_len_from_tuple_of_list(lst):
    """
    provide the max length of the things this person likes in lst
    :param lst: lst is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: max length of the things this person likes
        complexity:
            time: O(n), n is the size of the lst
            auxiliary space: O(1)
    """
    maximum = len(lst[0][1])
    for i in range(len(lst)):
        if len(lst[i][1]) > maximum:
            maximum = len(lst[i][1])
    return maximum


def grouping2(lst):
    """
    group all the names of the people who like exactly those things
    :param lst: lst is a sorted list
    :return: all the names of the people who like exactly those things in list and return a list of list
    complexity:
            time: O(N) N is the number of elements in lst
            auxiliary space: O(k), k is the size of inner list
    """
    # initialise inner list
    new_list = []

    # initialise outer list
    new_list2 = []
    j = 0

    # put names of the people who like exactly those things same list
    for i in range(0, len(lst)):
        if lst[i][1] == lst[j][1]:
            new_list.append(lst[i][0])
        else:
            j = i
            new_list2.append(new_list)
            new_list = [lst[j][0]]
        if i == len(lst) - 1:
            new_list2.append(new_list)

    return new_list2


def interest_groups(data):
    """
    grouping the all the names of the people who like exactly those things into list of list.
    :param data: data is a list, where each element is a 2-element tuple. The first element is their name.
                 The second element is represents the things this
                 person likes.
    :return: a list of list which contains all the names of the people who like exactly those things.
    complexity:
            time: O(N*M) N is the number of elements in data.
                        M is the maximum number of characters among all sets of liked things.
            auxiliary space: O(n), n is the length of data
    """
    if len(data) == 0:
        return []
    # sort the data in ascending order according to their name
    new_data = beta_radix_sort(data, 0)

    # initialise a empty string
    new_data1 = []

    # # loop through every element of data, sort data according name and rebuild the list of tuple
    # for i in range(len(data)):
    #     sort_item = alpha_radix_sort(new_data[i][1])
    #     new_data1.append((data[i][0], sort_item))
    #
    # # sort new_data1 according to the length of second element in tuple
    # new_data1 = len_counting_sort2(new_data1, 1)
    #
    # # sort new_data1 according to the first item in the second element of the tuple
    # new_data1 = beta_radix_sort(new_data1, 1)
    #
    # # group all the names of the people who like exactly those things
    # new_data1 = grouping2(new_data1)

    return new_data


data = [("nuka", ["birds", "napping"]),
("hadley", ["napping birds", "nash equilibria"]),
("yaffe", ["rainy evenings", "the colour red", "birds"]),
("laurie", ["napping", "birds"]),
("kamalani", ["birds", "rainy evenings", "the colour red"])]
print(interest_groups(data))
