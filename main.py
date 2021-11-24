class MapSum(object):

    def __init__(self):
        self.list = []
        self.key_memory = []

    def insert(self, key: str, val: int) -> None:
        if key not in self.key_memory:
            dict = {
                key: val
            }
            self.list.append(dict)
        else:
            for item in self.list:
                for ky in item.keys():
                    if ky == key:
                        item[ky] = val

    def sum(self, prefix: str) -> int:
        """
        [{key:value}]
        :param prefix:
        :return:
        """
        sum = 0
        if not prefix:
            return 0
        for lt in self.list:
            for key in lt.keys():
                if key.split(prefix)[0] == "":
                    sum += lt.get(key)
        return sum

test = MapSum()
test.insert("apple", 1)
test.sum("ap")