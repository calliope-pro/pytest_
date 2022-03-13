import pytest

from target_sample import MyException, inc, raiseMyExceptionIf100


def test_inc_1():
    assert inc(3) == 5

# success
def test_inc_2():
    assert inc(4) == 5

def test_inc_3():
    assert inc(5) == 5

# success
def test_raiseMyExceptionIf100_1():
    assert raiseMyExceptionIf100(70) == 70

# success
def test_raiseMyExceptionIf100_2():
    assert raiseMyExceptionIf100(500) == 500

# success
def test_raiseMyExceptionIf100_err_msg():
    # MyExceptionがraiseされたときmatchに合致するか
    with pytest.raises(MyException, match="x can't be 100."):
        raiseMyExceptionIf100(100)


