class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsList = []
        anagramDict = {}
        for word in strs:
            sortedWord:str = "".join(sorted(word))
            if sortedWord in anagramDict:
                anagramDict[sortedWord].append(word)
            else:
                anagramDict[sortedWord] = [word]
        for key in anagramDict:
            gramGrams = anagramDict[key]
            anagramsList.append(gramGrams)
        return anagramsList

