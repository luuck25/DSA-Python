


squares = [i*i for i in range(5)]

print(squares)

even = [i for i in range(10) if i%2 ==0]

print(even)

results = ["Even" if i % 2 == 0 else "ODD" for i in range(10)]

print(results)


square = lambda x : x * x

