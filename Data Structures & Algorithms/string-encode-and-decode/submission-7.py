class Solution:

    def encode(self, strs: List[str]) -> str:
        masterStr: str = ""
        count: int = 0
        for s in strs:
            count = len(s)
            masterStr = masterStr + f"{count}#" + s
        return masterStr

    def decode(self, s: str) -> List[str]:
        final: list[str] = []
        lengths: list[int] = []
        startAt: int = 0
        endAt: int = 0
        i: int = 0 #pointer to keep our place in the string
        j: int = 0
        k: int = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            k = j
            k = k + length + 1
            final.append(s[j+1:k])
            i = k
        return final


        



