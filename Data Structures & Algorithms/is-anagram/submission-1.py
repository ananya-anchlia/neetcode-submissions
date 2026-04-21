class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
    #     if len(s) != len (t):
    #         return False
    #     x = 0
    #     s_dict = {}
    #     while x != len(s):
    #         char = s[x]
    #         s_dict[char] = x
    #     t_char_list = list(t)
    #     for letter in t:
    #         if letter not in s:
    #             return False
    #     return True

        