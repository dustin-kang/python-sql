"""
49

그룹 애너그램

문자열 배열을 받아 애너그램 단위로 그룹핑하라.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

? Anagram(애너그램)
 >> 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다. 
 >> 문전박대 -> 대박전문 
"""

import collections


strs = ["eat","tea","tan","ate","nat","bat"]
lst = []

anagrams = collections.defaultdict(list) # 추가되는 값이 list 자료형 형식임.

for word in strs:
        anagrams[''.join(sorted(word))].append(word) # 단어를 정렬하여 애너그램에 join 함.

print(anagrams)

