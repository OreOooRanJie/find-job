"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_note_map, magazine_map = {}, {}
        for i in magazine:
            if i not in magazine_map:
                magazine_map[i] = 1
            else:
                magazine_map[i] += 1

        for i in ransomNote:
            if i not in ransom_note_map:
                ransom_note_map[i] = 1
            else:
                ransom_note_map[i] += 1

        for key, value in ransom_note_map.items():
            if not magazine_map.get(key):
                return False
            if value > magazine_map.get(key):
                return False
        return True


