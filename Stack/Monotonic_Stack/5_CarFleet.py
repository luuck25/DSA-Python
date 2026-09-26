class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=[]

        for pos,speed in zip(position,speed):

            time = (target - pos) / speed

            cars.append((pos,time))

        cars.sort(reverse=True)

        st = []

        for _,time in cars:

            if not st or time > st[-1]:
                st.append(time)
        return len(st)        


        