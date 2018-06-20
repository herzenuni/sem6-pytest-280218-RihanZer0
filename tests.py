import pytest
from hypothesis import given
import hypothesis.strategies as st

def diction(keys, values):
    try:
        if type(keys) is not list or type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result

#asserts
def test_assert():
    assert diction([1, 2, 3, 4],['a','b','c'])=={1: 'a', 2: 'b', 3: 'c', 4: None}
    assert diction([1,2,3], 3)==None
    assert diction(3,['a','b','c'])==None
    assert diction([],['a','b','c'])=={}

#param
@pytest.mark.parametrize("a,b,expected",[
    ([1,2,3],['a','b','c','d'], {1: 'a', 2: 'b', 3: 'c'}),
    ([1,2,3], 3, None),
    (3,['a','b','c'],None),
    ([],['a','b','c'],{})
])
def test_param(a, b, expected):
    assert diction(a,b)==expected
    assert diction([1,2,3], 3)==None
    assert diction(3,['a','b','c'])==None
    assert diction([],['a','b','c'])=={}

#hypothesis
@given(st.lists(), st.lists())
def test_diction(a, b):
    assert type(diction(a,b)) == dict
    assert len(diction(a,b)) == len(a)