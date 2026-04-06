class Solution:
    def frequencySort(self, s: str) -> str:

        counter = Counter(s)

        mp = defaultdict(list)

        for ch, count in counter.items():
            mp[count].append(ch)   

        result = []

        for count in range(len(s),0,-1):

            for ch in mp[count]:
                result.append(ch * count)
        
        return "".join(result)              

        