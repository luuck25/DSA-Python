

def perm_fun(arr_input):

    result = []
    def perm(remaining_arr:list[int],path:list[int]):

        if len(remaining_arr) == 0:
            result.append(path)
            return


        for i in range(len(remaining_arr)):
            path.append(remaining_arr[i])
            new_input = remaining_arr[i+1:]
            perm(new_input,path) 
        return       




    for i in range(len(arr_input)):

        path = []
        path.append(arr_input[i])
        perm(arr_input[i+1:],path)

print(perm_fun([1,2,3]))        
    