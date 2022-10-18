import random


def merge(arr1, arr2):
    res = []
    start1, start2 = 0, 0
    while start1 < len(arr1) and start2 < len(arr2):
        if arr1[start1] < arr2[start2]:
            res.append(arr1[start1])
            start1 += 1
        else:
            res.append(arr2[start2])
            start2 += 1
    if start1 == len(arr1):
        res += arr2[start2:]
    if start2 == len(arr2):
        res += arr1[start1:]
    return res


def bottom_to_up(arr):
    # 首先计算数组长度
    lenth = len(arr)

    # 定义子数组长度
    sub_arr_lenth = 1

    start = 0

    res = []
    while sub_arr_lenth < lenth:
        while start < lenth:
            arr1 = arr[start:sub_arr_lenth + start]
            arr2 = arr[sub_arr_lenth + start: min(start + 2 * sub_arr_lenth, lenth)]
            if arr1 and arr2:
                res += merge(arr1, arr2)
            elif arr1:
                res += merge(res, arr1)
            else:
                res += merge(res, arr2)
            start = start + 2 * sub_arr_lenth
        sub_arr_lenth <<= 1
        start = 0
        arr = res
        res = []

    return arr


def up_to_down(arr):
    return helper(arr, 0, len(arr) - 1)


def helper(arr, low, high):
    if low >= high:
        return [arr[low]]

    mid = low + ((high - low) >> 1)
    arr1 = helper(arr, low, mid)
    arr2 = helper(arr, mid + 1, high)
    return merge(arr1, arr2)


arr = [random.randint(0, 20) for i in range(0, 10)]

print(up_to_down(arr))
