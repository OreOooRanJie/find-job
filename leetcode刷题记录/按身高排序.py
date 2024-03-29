"""
给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。

对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。

请按身高 降序 顺序返回对应的名字数组 names 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sort-the-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        tuple_tmp = zip(names, heights)
        tuple_tmp = sorted(tuple_tmp, key=lambda x: x[1], reverse=True)
        return [item[0] for item in tuple_tmp]

if __name__ == "__main__":
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    solution = Solution()
    my_res = solution.sortPeople(names, heights)
    print(my_res)
