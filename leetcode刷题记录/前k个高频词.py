"""
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
"""

import collections
import heapq


class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word


class Solution:
    def topKFrequent(self, words, k):

        cnt = collections.Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]
