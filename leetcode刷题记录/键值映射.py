"""
实现一个 MapSum 类，支持两个方法，insert和sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

author: ranjie
"""


class MapSum(object):
    """暴力解法"""
    def __init__(self):
        self.list = []
        self.key_memory = []

    def insert(self, key: str, val: int) -> None:
        if key not in self.key_memory:
            dict = {
                key: val
            }
            self.list.append(dict)
            self.key_memory.append(key)
        else:
            for item in self.list:
                for ky in item.keys():
                    if ky == key:
                        item[ky] = val

class Trie(object):
    """ 前缀树 """

    def __init__(self):
        pass
    def trie(self):
        pass