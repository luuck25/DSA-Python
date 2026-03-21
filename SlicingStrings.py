


# sequence[start : stop : step]

name = "lakesh"

# index 1 to end
print(name[1:]) 

# start 0 end all length, step 1 - print entire string
print(name[::])

# start 0 end -> end 3-1 , step 1

print(name[:3])

# start - 0, end 3

print(name[0:4])


# negative index

# entire string reverse - start 0 , end -> all length , -1 step mean from reverse
print(name[::-1])



# start 0, end. -> 3 char from end
print(name[:-3])

# start 3rd char frm end , len, step 1
print(name[-3::])

