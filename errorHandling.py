def find_minimum(a, b):
    add=a+b
    sub=a-b
    mul=a*b
    div=0
    try:
        div=a/b
    except:
        div=0
    a=min(add,sub,mul,div)
    print(a)
    
find_minimum(5,-5)

