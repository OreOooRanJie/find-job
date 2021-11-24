"""
editor: 冉洁
time: 2021/11/14 22:01
选择排序：
遍历所有元素，将最值往一边放
"""


class SelectSort(object):
    """选择排序"""
    def __init__(self):
        pass

    def select_sort(self, input):
        """
        选择排序
        :param input: 待排序数列
        :return: 有序数列
        """
        # [1, 3, 2, 4, 6, 5]
        length = len(input)
        for i in range(length):
            min_index = i
            for j in range(i, length):
                if input[i] > input[j]:
                    min_index = j
            input[i], input[min_index] = input[min_index], input[i]
        return input


if __name__ == "__main__":
    data = [1, 3, 2, 4, 6, 5]
    select_sort = SelectSort()
    print(select_sort.select_sort(data))