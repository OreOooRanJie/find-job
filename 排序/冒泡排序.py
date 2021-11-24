"""
editor: 冉洁
time: 2021/11/14 22:01
冒泡排序：
遍历所有元素，然后两两比较，把较大数往右移（通过相互交换的方式）
"""


class MpSort(object):
    """冒泡排序"""

    def mp_sort(self, input):
        """
        冒泡排序
        :param input:
        :return:
        """
        length = len(input)
        for i in range(length):
            for j in range(length - i - 1):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]
        return input


if __name__ == "__main__":
    data = [1, 3, 2, 4, 6, 5]
    mp_sort = MpSort()
    print(mp_sort.mp_sort(data))
