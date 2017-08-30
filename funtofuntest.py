def funtest1():
    arg = 2
    print(arg)
    return arg

def funtest2(childfun):
    childfun()


funtest2(funtest12)
