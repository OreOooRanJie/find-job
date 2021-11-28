"""
editor: 冉洁
time: 2021/11/14 22:01
插入排序：
第i个数，依次与前i-1个数进行比较，若input[i]>input[i+1],则进行交换
这里可以理解为可变的数组做及时停止的冒泡排序，因为，如果排序到i的时候，实际上之前的i-1个数已经排序完毕
例如，[1, 3, 2, 4, 6, 5]
开始的数组为[1], 不需要排序
第二步数组为[1,3],不需要排序
第三步数组为[1,3,2]，需要排序，即“2”与“3”比较，交换，变为[1,2,3]
第四步数组为[1,2,3,4]，不需要排序
"""


class InsertSort(object):
    """插入排序"""

    def mp_sort(self, input):
        """
        冒泡排序
        :param input:
        :return:
        """
        # [1, 3, 2, 4, 6, 5]

        length = len(input)
        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if input[j+1] < input[j]:
                    input[i], input[j] = input[j], input[i]
                else:
                    break
        return input


if __name__ == "__main__":
    data = [1, 3, 2, 4, 6, 5]
    mp_sort = InsertSort()
    print(mp_sort.mp_sort(data))
