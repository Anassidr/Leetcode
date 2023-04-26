


#  no redundant calculations 
def fibo(n: int, map={}):
    if n in map:
        return map[n]
    map[0] = 0
    map[1] = 1
    map[2] = 1 
    map[n] = fibo(n-1)+fibo(n-2) 
    return map[n]

print(fibo(1000))