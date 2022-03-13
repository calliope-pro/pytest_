def inc(x: int):
    return x + 1

class MyException(Exception):
    pass

def raiseMyExceptionIf100(x: int):
    if x == 100:
        raise MyException("x can't be 100.")
    return x


