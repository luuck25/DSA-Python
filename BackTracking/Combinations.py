class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        def comb(start,path):

            if len(path) == k:
                result.append(path[:])
                return


            for i in range(start , n+1):
                path.append(i)
                comb(i+1,path)
                path.pop()
            return

        comb(1,[])  

        return result          

        